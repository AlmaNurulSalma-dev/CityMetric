"""
CityMetric - Phase 2: Data Preprocessing & Feature Engineering
Cleans the master city list, handles missing values, builds 7 composite
dimension scores (0-10), and outputs cities_features.csv ready for WEKA.
"""

import warnings
import pandas as pd
import numpy as np
from pathlib import Path

warnings.filterwarnings('ignore')

ROOT      = Path(__file__).resolve().parent.parent
RAW_OUT   = ROOT / "data" / "raw"
PROC_OUT  = ROOT / "data" / "processed"
PROC_OUT.mkdir(parents=True, exist_ok=True)


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def minmax(series, invert=False, scale=10):
    """Min-Max normalise a Series to [0, scale]. NaN stays NaN."""
    lo, hi = series.min(), series.max()
    if hi == lo:
        return pd.Series(scale / 2, index=series.index)
    norm = (series - lo) / (hi - lo) * scale
    return (scale - norm) if invert else norm


def fill_missing(df, col, method="median", group_col=None):
    """Fill NaN in col using median/mean, optionally within a group."""
    if col not in df.columns:
        return df
    if group_col and group_col in df.columns:
        df[col] = df.groupby(group_col)[col].transform(
            lambda x: x.fillna(x.median() if method == "median" else x.mean())
        )
    df[col] = df[col].fillna(
        df[col].median() if method == "median" else df[col].mean()
    )
    return df


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1 — Load & deduplicate
# ═══════════════════════════════════════════════════════════════════════════════

def load_and_deduplicate():
    print("\n[1/4] Loading master city list...")
    df = pd.read_csv(RAW_OUT / "master_city_list_raw.csv")
    print(f"    Loaded: {len(df)} rows x {len(df.columns)} columns")

    before = len(df)
    df = df.drop_duplicates(subset=["city"], keep="first").reset_index(drop=True)
    print(f"    Removed {before - len(df)} duplicate city rows -> {len(df)} cities")
    return df


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2 — Clean & impute
# ═══════════════════════════════════════════════════════════════════════════════

def clean_and_impute(df):
    print("\n[2/4] Cleaning & imputing missing values...")

    # ── Population: fill from known values ───────────────────────────────────
    df = fill_missing(df, "population", method="median", group_col="region")

    # ── Affordability columns ─────────────────────────────────────────────────
    aff_cols = [
        "rent_1br_city_center", "rent_3br_city_center", "avg_net_salary",
        "meal_inexpensive_restaurant", "utilities_monthly_85m2",
        "price_per_m2_city_center", "internet_monthly_60mbps",
        "monthly_pass_transport",
    ]
    for col in aff_cols:
        df = fill_missing(df, col, method="median", group_col="region")

    # ── Temperature: fill with region median ──────────────────────────────────
    for col in ["avg_temp_c", "temp_std_c", "temp_trend_c"]:
        df = fill_missing(df, col, method="median", group_col="region")

    # ── World Bank indicators ─────────────────────────────────────────────────
    wb_cols = [
        "internet_users_pct", "broadband_per_100", "mobile_per_100",
        "gdp_per_capita_usd", "gini_index", "urban_pop_pct", "pop_growth_rate",
        "rd_spending_pct_gdp", "scientific_articles", "high_tech_exports_pct",
        "tertiary_enrollment_pct", "adult_literacy_pct", "edu_spending_pct_gdp",
    ]
    for col in wb_cols:
        df = fill_missing(df, col, method="median", group_col="region")

    # adult_literacy_pct is sparse — fill remaining with global median
    df = fill_missing(df, "adult_literacy_pct", method="median")

    # ── University rankings ───────────────────────────────────────────────────
    uni_cols = [
        "cwur_top_uni_score", "cwur_avg_score", "cwur_uni_count",
        "cwur_patents", "cwur_citations", "cwur_research",
        "times_top_uni_score", "times_avg_research", "times_avg_citations",
        "times_uni_count", "shanghai_top_score", "shanghai_uni_count",
    ]
    for col in uni_cols:
        if col in df.columns:
            df = fill_missing(df, col, method="median", group_col="region")

    # ── Stack Overflow ────────────────────────────────────────────────────────
    so_cols = [
        "so_developer_count", "so_employed_dev_count",
        "so_median_salary_usd", "so_senior_dev_pct",
    ]
    for col in so_cols:
        df = fill_missing(df, col, method="median", group_col="region")

    # ── Validate no nulls remain in key columns ───────────────────────────────
    key_cols = aff_cols + wb_cols + ["avg_temp_c"] + so_cols
    null_counts = {c: df[c].isna().sum() for c in key_cols if c in df.columns and df[c].isna().sum() > 0}
    if null_counts:
        print(f"    Remaining nulls after imputation: {null_counts}")
    else:
        print(f"    All key columns fully imputed.")

    # Save cleaned base
    out = PROC_OUT / "cities_cleaned.csv"
    df.to_csv(out, index=False)
    print(f"    Saved: {out.name} ({len(df)} cities x {len(df.columns)} cols)")
    return df


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3 — Feature engineering: 7 dimension scores
# ═══════════════════════════════════════════════════════════════════════════════

def engineer_features(df):
    print("\n[3/4] Engineering 7 dimension scores (0-10)...")

    ft = df[["city", "country", "region", "latitude", "longitude", "population"]].copy()

    # ─────────────────────────────────────────────────────────────────────────
    # DIMENSION 1: AFFORDABILITY (higher score = more affordable)
    # Logic: high salary + low costs = affordable
    # ─────────────────────────────────────────────────────────────────────────
    # Salary-to-rent ratio (buying power)
    df["salary_to_rent"]  = df["avg_net_salary"] / (df["rent_1br_city_center"] + 1)
    # Normalised sub-scores
    s_salary  = minmax(df["avg_net_salary"])            # higher = better
    s_rent    = minmax(df["rent_1br_city_center"],   invert=True)  # lower = better
    s_food    = minmax(df["meal_inexpensive_restaurant"], invert=True)
    s_util    = minmax(df["utilities_monthly_85m2"],  invert=True)
    s_transit = minmax(df["monthly_pass_transport"],  invert=True)
    s_ratio   = minmax(df["salary_to_rent"])            # higher = better
    # Weighted average — salary-to-rent ratio carries most weight
    ft["affordability_score"] = (
        s_ratio   * 0.35 +
        s_salary  * 0.25 +
        s_rent    * 0.20 +
        s_food    * 0.10 +
        s_util    * 0.05 +
        s_transit * 0.05
    )
    print(f"    [1] Affordability — min {ft['affordability_score'].min():.2f}  max {ft['affordability_score'].max():.2f}")

    # ─────────────────────────────────────────────────────────────────────────
    # DIMENSION 2: DIGITAL INFRASTRUCTURE
    # ─────────────────────────────────────────────────────────────────────────
    s_inet   = minmax(df["internet_users_pct"])
    s_bb     = minmax(df["broadband_per_100"])
    s_mobile = minmax(df["mobile_per_100"])
    # internet_monthly_60mbps: lower price = better digital access value
    s_isprice = minmax(df["internet_monthly_60mbps"], invert=True)
    ft["digital_score"] = (
        s_inet   * 0.35 +
        s_bb     * 0.30 +
        s_mobile * 0.20 +
        s_isprice * 0.15
    )
    print(f"    [2] Digital       — min {ft['digital_score'].min():.2f}  max {ft['digital_score'].max():.2f}")

    # ─────────────────────────────────────────────────────────────────────────
    # DIMENSION 3: STARTUP ECOSYSTEM — no data, set to global average
    # Will be excluded from clustering, kept as placeholder
    # ─────────────────────────────────────────────────────────────────────────
    ft["startup_score"] = 5.0
    print(f"    [3] Startup       — no data, placeholder = 5.0 for all cities")

    # ─────────────────────────────────────────────────────────────────────────
    # DIMENSION 4: URBAN DEVELOPMENT
    # ─────────────────────────────────────────────────────────────────────────
    s_urban_pct = minmax(df["urban_pop_pct"])
    s_pop_size  = minmax(df["population"].clip(upper=df["population"].quantile(0.95)))
    # Climate comfort: penalise extremes (very hot or very cold)
    # Optimal avg temp ~18-22°C — score peaks at 20°C
    df["temp_comfort"] = 10 - minmax((df["avg_temp_c"] - 20).abs())
    s_temp_comfort = df["temp_comfort"].clip(0, 10)
    # Low temp variability = more comfortable climate
    s_temp_stable  = minmax(df["temp_std_c"], invert=True)
    ft["urban_score"] = (
        s_urban_pct    * 0.30 +
        s_pop_size     * 0.20 +
        s_temp_comfort * 0.30 +
        s_temp_stable  * 0.20
    )
    print(f"    [4] Urban         — min {ft['urban_score'].min():.2f}  max {ft['urban_score'].max():.2f}")

    # ─────────────────────────────────────────────────────────────────────────
    # DIMENSION 5: INNOVATION READINESS
    # ─────────────────────────────────────────────────────────────────────────
    s_rd        = minmax(df["rd_spending_pct_gdp"])
    s_articles  = minmax(df["scientific_articles"])
    s_hightech  = minmax(df["high_tech_exports_pct"])
    s_uni_score = minmax(df["cwur_top_uni_score"]) if "cwur_top_uni_score" in df.columns else pd.Series(5.0, index=df.index)
    s_patents   = minmax(df["cwur_patents"])        if "cwur_patents"       in df.columns else pd.Series(5.0, index=df.index)
    ft["innovation_score"] = (
        s_rd        * 0.25 +
        s_articles  * 0.25 +
        s_hightech  * 0.20 +
        s_uni_score * 0.20 +
        s_patents   * 0.10
    )
    print(f"    [5] Innovation    — min {ft['innovation_score'].min():.2f}  max {ft['innovation_score'].max():.2f}")

    # ─────────────────────────────────────────────────────────────────────────
    # DIMENSION 6: TALENT & HUMAN CAPITAL
    # ─────────────────────────────────────────────────────────────────────────
    s_edu      = minmax(df["tertiary_enrollment_pct"])
    s_literacy = minmax(df["adult_literacy_pct"])
    s_edu_spend= minmax(df["edu_spending_pct_gdp"])
    # Developer density: so_developer_count normalised by log-population
    df["dev_density"] = df["so_developer_count"] / (np.log1p(df["population"]) + 1)
    s_dev      = minmax(df["dev_density"])
    s_senior   = minmax(df["so_senior_dev_pct"])
    ft["talent_score"] = (
        s_edu       * 0.30 +
        s_literacy  * 0.20 +
        s_edu_spend * 0.15 +
        s_dev       * 0.25 +
        s_senior    * 0.10
    )
    print(f"    [6] Talent        — min {ft['talent_score'].min():.2f}  max {ft['talent_score'].max():.2f}")

    # ─────────────────────────────────────────────────────────────────────────
    # DIMENSION 7: FUTURE TRAJECTORY (growth potential)
    # ─────────────────────────────────────────────────────────────────────────
    s_gdp_cap   = minmax(df["gdp_per_capita_usd"])   # wealth level proxy
    s_pop_grow  = minmax(df["pop_growth_rate"])       # city attracting people
    s_temp_trend= minmax(df["temp_trend_c"], invert=True)  # less warming = better
    s_hightech2 = minmax(df["high_tech_exports_pct"]) # future-oriented economy
    ft["growth_score"] = (
        s_gdp_cap    * 0.30 +
        s_pop_grow   * 0.25 +
        s_hightech2  * 0.25 +
        s_temp_trend * 0.20
    )
    print(f"    [7] Growth        — min {ft['growth_score'].min():.2f}  max {ft['growth_score'].max():.2f}")

    # ─────────────────────────────────────────────────────────────────────────
    # OVERALL OPPORTUNITY INDEX (exclude startup — no data)
    # ─────────────────────────────────────────────────────────────────────────
    dims = ["affordability_score", "digital_score", "urban_score",
            "innovation_score", "talent_score", "growth_score"]
    ft["opportunity_index"] = ft[dims].mean(axis=1)
    print(f"\n    Overall opportunity index — min {ft['opportunity_index'].min():.2f}  max {ft['opportunity_index'].max():.2f}")

    # Round all scores to 2dp
    score_cols = [c for c in ft.columns if "_score" in c or c == "opportunity_index"]
    ft[score_cols] = ft[score_cols].round(2)

    return ft


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4 — Save outputs & print summary
# ═══════════════════════════════════════════════════════════════════════════════

def save_and_report(ft):
    print("\n[4/4] Saving outputs & summary...")

    out = PROC_OUT / "cities_features.csv"
    ft.to_csv(out, index=False)
    print(f"    Saved: {out.name} ({len(ft)} cities x {len(ft.columns)} cols)")

    # Top 10 by opportunity index
    top10 = ft.nlargest(10, "opportunity_index")[
        ["city", "country", "opportunity_index",
         "affordability_score", "digital_score",
         "innovation_score", "talent_score", "growth_score"]
    ].reset_index(drop=True)
    top10.index += 1

    print("\n    TOP 10 CITIES BY OPPORTUNITY INDEX:")
    print("    " + "-" * 80)
    header = f"    {'#':<4} {'City':<20} {'Country':<18} {'Opp':>5} {'Aff':>5} {'Dig':>5} {'Inn':>5} {'Tal':>5} {'Grw':>5}"
    print(header)
    print("    " + "-" * 80)
    for i, row in top10.iterrows():
        print(f"    {i:<4} {row['city']:<20} {row['country']:<18} "
              f"{row['opportunity_index']:>5.2f} "
              f"{row['affordability_score']:>5.2f} "
              f"{row['digital_score']:>5.2f} "
              f"{row['innovation_score']:>5.2f} "
              f"{row['talent_score']:>5.2f} "
              f"{row['growth_score']:>5.2f}")

    # Score stats per dimension
    print("\n    DIMENSION SCORE STATISTICS:")
    dims = ["affordability_score", "digital_score", "urban_score",
            "innovation_score", "talent_score", "growth_score", "opportunity_index"]
    stats = ft[dims].describe().loc[["mean", "std", "min", "max"]].round(2)
    print("    " + stats.to_string().replace("\n", "\n    "))

    # Regional averages
    print("\n    REGIONAL AVERAGES (opportunity_index):")
    reg = ft.groupby("region")["opportunity_index"].agg(["mean","count"]).round(2)
    reg.columns = ["avg_score", "n_cities"]
    print("    " + reg.sort_values("avg_score", ascending=False).to_string().replace("\n", "\n    "))

    return ft


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  CityMetric — Phase 2: Preprocessing & Feature Engineering")
    print("=" * 60)

    df = load_and_deduplicate()
    df = clean_and_impute(df)
    ft = engineer_features(df)
    save_and_report(ft)

    print("\n" + "=" * 60)
    print("  Phase 2 COMPLETE")
    print("  Files saved to:", PROC_OUT)
    for f in sorted(PROC_OUT.iterdir()):
        print(f"    {f.name:<40} {f.stat().st_size/1024:.1f} KB")
    print("=" * 60)
    print("\n  Next step: run scripts/03_arff_conversion.py  (for WEKA)")


if __name__ == "__main__":
    main()
