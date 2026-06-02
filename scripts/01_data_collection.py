"""
CityMetric - Phase 1: Data Collection
Loads all available datasets, extracts World Bank API data,
builds a master city list, and saves everything to data/raw/.
"""

import os
import sys
import warnings
import pandas as pd
import numpy as np
from pathlib import Path

warnings.filterwarnings('ignore')

# ─── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
DATA_SRC = ROOT / "data_sources"
RAW_OUT  = ROOT / "data" / "raw"
RAW_OUT.mkdir(parents=True, exist_ok=True)

# ─── Numbeo column mapping (x1–x55 → real names) ─────────────────────────────
# Standard Numbeo cost-of-living column order (USD prices)
NUMBEO_COLS = {
    "x1":  "meal_inexpensive_restaurant",
    "x2":  "meal_2ppl_midrange",
    "x3":  "mcmeal_fastfood",
    "x4":  "domestic_beer_restaurant",
    "x5":  "imported_beer_restaurant",
    "x6":  "cappuccino",
    "x7":  "coke_pepsi",
    "x8":  "water_restaurant",
    "x9":  "milk_1L",
    "x10": "bread_500g",
    "x11": "rice_1kg",
    "x12": "eggs_12",
    "x13": "local_cheese_1kg",
    "x14": "chicken_1kg",
    "x15": "beef_1kg",
    "x16": "apples_1kg",
    "x17": "banana_1kg",
    "x18": "oranges_1kg",
    "x19": "tomato_1kg",
    "x20": "potato_1kg",
    "x21": "onion_1kg",
    "x22": "lettuce",
    "x23": "water_1_5L",
    "x24": "bottle_wine_midrange",
    "x25": "domestic_beer_0_5L_market",
    "x26": "imported_beer_0_33L_market",
    "x27": "cigarettes_20pk",
    "x28": "one_way_ticket_local",
    "x29": "monthly_pass_transport",
    "x30": "taxi_start",
    "x31": "taxi_1km",
    "x32": "taxi_1hr_waiting",
    "x33": "gasoline_1L",
    "x34": "volkswagen_golf",
    "x35": "toyota_corolla",
    "x36": "utilities_monthly_85m2",
    "x37": "mobile_monthly_1min",
    "x38": "internet_monthly_60mbps",
    "x39": "fitness_club_monthly",
    "x40": "tennis_court_1hr",
    "x41": "cinema_ticket",
    "x42": "preschool_monthly",
    "x43": "intl_primary_school_yearly",
    "x44": "jeans_levis",
    "x45": "summer_dress",
    "x46": "nike_running_shoes",
    "x47": "mens_leather_shoes",
    "x48": "rent_1br_city_center",
    "x49": "rent_1br_outside_center",
    "x50": "rent_3br_city_center",
    "x51": "rent_3br_outside_center",
    "x52": "price_per_m2_city_center",
    "x53": "price_per_m2_outside_center",
    "x54": "avg_net_salary",
    "x55": "mortgage_interest_rate",
}

# Target 60 cities – major global cities covering all regions
TARGET_CITIES = [
    # Asia-Pacific
    "Tokyo", "Shanghai", "Beijing", "Seoul", "Singapore", "Hong Kong",
    "Bangkok", "Jakarta", "Mumbai", "Delhi", "Bangalore", "Kuala Lumpur",
    "Manila", "Ho Chi Minh City", "Sydney", "Melbourne",
    # Europe
    "London", "Paris", "Berlin", "Amsterdam", "Madrid", "Barcelona",
    "Rome", "Milan", "Vienna", "Zurich", "Stockholm", "Oslo",
    "Copenhagen", "Helsinki", "Warsaw", "Prague", "Budapest", "Lisbon",
    # Americas
    "New York", "San Francisco", "Los Angeles", "Chicago", "Toronto",
    "Vancouver", "Mexico City", "Sao Paulo", "Buenos Aires", "Bogota",
    "Lima", "Santiago",
    # Middle East & Africa
    "Dubai", "Abu Dhabi", "Tel Aviv", "Istanbul", "Cairo",
    "Nairobi", "Lagos", "Johannesburg", "Casablanca",
]

# ─── World Bank indicator IDs ──────────────────────────────────────────────────
WB_INDICATORS = {
    # Digital
    "IT.NET.USER.ZS":  "internet_users_pct",
    "IT.NET.BBND.P2":  "broadband_per_100",
    "IT.CEL.SETS.P2":  "mobile_per_100",
    # Economic
    "NY.GDP.PCAP.CD":  "gdp_per_capita_usd",
    "SI.POV.GINI":     "gini_index",
    # Urban
    "SP.URB.TOTL.IN.ZS": "urban_pop_pct",
    "SP.POP.GROW":        "pop_growth_rate",
    # Innovation
    "GB.XPD.RSDV.GD.ZS":  "rd_spending_pct_gdp",
    "IP.JRN.ARTC.SC":     "scientific_articles",
    "TX.VAL.TECH.MF.ZS":  "high_tech_exports_pct",
    # Talent
    "SE.TER.ENRR":     "tertiary_enrollment_pct",
    "SE.ADT.LITR.ZS":  "adult_literacy_pct",
    "SE.XPD.TOTL.GD.ZS": "edu_spending_pct_gdp",
}


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1 — Cost of Living (Numbeo)
# ═══════════════════════════════════════════════════════════════════════════════

def load_cost_of_living():
    print("\n[1/6] Loading Cost of Living (Numbeo)...")
    path = DATA_SRC / "1_affordability_livability" / "01_cost_of_living_numbeo" / "data.csv"

    df = pd.read_csv(path)
    print(f"    Raw rows: {len(df):,}  |  Columns: {len(df.columns)}")

    # Keep only high-quality entries
    df = df[df["data_quality"] == 1].copy()
    print(f"    High-quality rows (data_quality=1): {len(df):,}")

    # Rename x1–x55 to real names
    df.rename(columns=NUMBEO_COLS, inplace=True)
    df.drop(columns=["data_quality"], inplace=True)

    # Standardise city/country names
    df["city"]    = df["city"].str.strip()
    df["country"] = df["country"].str.strip()

    # Filter to target cities (case-insensitive match)
    target_lower = {c.lower(): c for c in TARGET_CITIES}
    df["city_matched"] = df["city"].str.lower().map(target_lower)
    df_target = df[df["city_matched"].notna()].copy()
    df_target["city"] = df_target["city_matched"]
    df_target.drop(columns=["city_matched"], inplace=True)

    # Also keep full dataset for reference
    df.drop(columns=["city_matched"], inplace=True, errors="ignore")

    print(f"    Target cities matched: {df_target['city'].nunique()} / {len(TARGET_CITIES)}")
    print(f"    Matched: {sorted(df_target['city'].unique().tolist())}")

    out_full   = RAW_OUT / "numbeo_full.csv"
    out_target = RAW_OUT / "numbeo_target_cities.csv"
    df.to_csv(out_full, index=False)
    df_target.to_csv(out_target, index=False)
    print(f"    Saved: {out_full.name} ({len(df):,} rows)")
    print(f"    Saved: {out_target.name} ({len(df_target):,} rows)")

    return df_target


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2 — World Cities (lat/lon/population master reference)
# ═══════════════════════════════════════════════════════════════════════════════

def load_world_cities():
    print("\n[2/6] Loading World Cities (MaxMind) for coordinates + population...")
    path = DATA_SRC / "4_urban_development" / "01_world_cities_kaggle" / "data.csv"

    # CSV column order: Country, City, AccentCity, Region, Population, Latitude, Longitude
    # We load by name then rename explicitly — never rely on usecols ordering
    df = pd.read_csv(path,
                     usecols=["City", "AccentCity", "Population", "Latitude", "Longitude"],
                     low_memory=False)
    df.rename(columns={
        "City":       "city_lower",   # already lowercase in this dataset
        "AccentCity": "city_accent",
        "Population": "population",
        "Latitude":   "latitude",
        "Longitude":  "longitude",
    }, inplace=True)

    # Drop rows missing coordinates
    df = df.dropna(subset=["latitude", "longitude"])

    # Match target cities against the lowercase City column
    target_lower = {c.lower(): c for c in TARGET_CITIES}
    df["city"] = df["city_lower"].str.strip().map(target_lower)
    df_target = df[df["city"].notna()].copy()
    df_target.drop(columns=["city_lower", "city_accent"], inplace=True)

    # When multiple entries per city (duplicates), keep the one with highest population
    df_target["population"] = pd.to_numeric(df_target["population"], errors="coerce")
    df_target = (df_target
                 .sort_values("population", ascending=False)
                 .drop_duplicates(subset=["city"], keep="first")
                 .reset_index(drop=True))

    # Manual fallback coords for cities not found in the dataset
    manual_coords = {
        "Mexico City": ("Mexico", 19.4326, -99.1332, 9209944),
    }
    found = set(df_target["city"].tolist())
    for city, (country, lat, lon, pop) in manual_coords.items():
        if city not in found:
            df_target = pd.concat([df_target, pd.DataFrame([{
                "city": city, "country_code": country,
                "population": pop, "latitude": lat, "longitude": lon,
            }])], ignore_index=True)

    print(f"    Target cities with coordinates: {len(df_target)} / {len(TARGET_CITIES)}")
    missing = sorted(set(TARGET_CITIES) - set(df_target["city"].tolist()))
    if missing:
        print(f"    Missing: {missing}")

    out = RAW_OUT / "world_cities_coords.csv"
    df_target.to_csv(out, index=False)
    print(f"    Saved: {out.name} ({len(df_target)} rows)")

    return df_target


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3 — City Temperature (climate / livability proxy)
# ═══════════════════════════════════════════════════════════════════════════════

def load_city_temperature():
    print("\n[3/6] Loading City Temperature data (1995–2020)...")
    path = DATA_SRC / "4_urban_development" / "02_city_temperature_kaggle" / "city_temperature.csv"

    df = pd.read_csv(path, low_memory=False)
    print(f"    Raw rows: {len(df):,}")

    # Remove bad temperature readings (Numbeo uses -99 as missing)
    df = df[df["AvgTemperature"] > -50].copy()

    # Convert Fahrenheit → Celsius
    df["temp_celsius"] = (df["AvgTemperature"] - 32) * 5 / 9

    # Filter to target cities
    target_lower = {c.lower(): c for c in TARGET_CITIES}
    df["city_matched"] = df["City"].str.strip().str.lower().map(target_lower)
    df_target = df[df["city_matched"].notna()].copy()
    df_target["city"] = df_target["city_matched"]

    # Aggregate: mean temp + std dev per city (across all years → climate profile)
    climate = (df_target.groupby("city")["temp_celsius"]
               .agg(avg_temp_c="mean", temp_std_c="std")
               .reset_index())

    # Optionally: growth trend — compare 1995-2000 avg vs 2015-2020 avg
    early = df_target[df_target["Year"].between(1995, 2000)].groupby("city")["temp_celsius"].mean().rename("temp_early")
    late  = df_target[df_target["Year"].between(2015, 2020)].groupby("city")["temp_celsius"].mean().rename("temp_late")
    trend = pd.concat([early, late], axis=1).dropna()
    trend["temp_trend_c"] = trend["temp_late"] - trend["temp_early"]
    trend = trend[["temp_trend_c"]].reset_index()

    climate = climate.merge(trend, on="city", how="left")

    print(f"    Cities with temperature data: {len(climate)} / {len(TARGET_CITIES)}")
    print(f"    Cities found: {sorted(climate['city'].tolist())}")

    out = RAW_OUT / "city_temperature_summary.csv"
    climate.to_csv(out, index=False)
    print(f"    Saved: {out.name} ({len(climate)} rows)")

    return climate


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4 — University Rankings (innovation proxy)
# ═══════════════════════════════════════════════════════════════════════════════

def load_university_rankings():
    print("\n[4/6] Loading University Rankings...")
    base = DATA_SRC / "5_innovation_readiness" / "01_university_rankings_kaggle"

    # ── CWUR ──────────────────────────────────────────────────────────────────
    cwur = pd.read_csv(base / "cwurData.csv")
    # Use latest year per institution
    cwur = cwur.sort_values("year").drop_duplicates(subset=["institution"], keep="last")
    cwur_country = (cwur.groupby("country")
                    .agg(
                        cwur_top_uni_score=("score", "max"),
                        cwur_avg_score=("score", "mean"),
                        cwur_uni_count=("institution", "count"),
                        cwur_patents=("patents", "mean"),
                        cwur_citations=("citations", "mean"),
                        cwur_research=("publications", "mean"),
                    )
                    .reset_index())

    # ── Times ─────────────────────────────────────────────────────────────────
    times = pd.read_csv(base / "timesData.csv")
    times["total_score"] = pd.to_numeric(times["total_score"], errors="coerce")
    times = times.sort_values("year").drop_duplicates(subset=["university_name"], keep="last")
    times_country = (times.groupby("country")
                     .agg(
                         times_top_uni_score=("total_score", "max"),
                         times_avg_research=("research", "mean"),
                         times_avg_citations=("citations", "mean"),
                         times_uni_count=("university_name", "count"),
                     )
                     .reset_index())
    times_country.rename(columns={"country": "country_times"}, inplace=True)

    # ── Shanghai ──────────────────────────────────────────────────────────────
    shanghai = pd.read_csv(base / "shanghaiData.csv")
    shanghai["total_score"] = pd.to_numeric(shanghai["total_score"], errors="coerce")
    # Shanghai doesn't have country — join via school_and_country_table
    school_country = pd.read_csv(base / "school_and_country_table.csv")
    shanghai = shanghai.merge(school_country, left_on="university_name", right_on="school_name", how="left")
    shanghai = shanghai.sort_values("year").drop_duplicates(subset=["university_name"], keep="last")
    shanghai_country = (shanghai.dropna(subset=["country"])
                        .groupby("country")
                        .agg(
                            shanghai_top_score=("total_score", "max"),
                            shanghai_uni_count=("university_name", "count"),
                        )
                        .reset_index())

    # ── Merge all three by country ────────────────────────────────────────────
    uni = cwur_country.copy()
    uni = uni.merge(times_country.rename(columns={"country_times": "country"}),
                    on="country", how="outer")
    uni = uni.merge(shanghai_country, on="country", how="outer")

    print(f"    Countries with university data: {len(uni)}")
    print(f"    Columns: {list(uni.columns)}")

    out = RAW_OUT / "university_rankings_by_country.csv"
    uni.to_csv(out, index=False)
    print(f"    Saved: {out.name} ({len(uni)} rows)")

    return uni


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 5 — Stack Overflow Survey (tech talent proxy)
# ═══════════════════════════════════════════════════════════════════════════════

def load_stackoverflow():
    print("\n[5/6] Loading Stack Overflow Survey (tech talent proxy)...")
    path = DATA_SRC / "6_talent_human_capital" / "01_stackoverflow_survey_official" / "data.csv"

    # Only load columns we need — file is large
    cols_needed = ["Country", "Employment", "YearsCode", "DevType",
                   "EdLevel", "ConvertedCompYearly", "RemoteWork"]
    df = pd.read_csv(path, usecols=cols_needed, engine="python", on_bad_lines="skip")
    print(f"    Total respondents: {len(df):,}")

    # Remove blank country
    df = df[df["Country"].notna() & (df["Country"] != "NA")].copy()
    print(f"    With country data: {len(df):,}  |  Countries: {df['Country'].nunique()}")

    # Developer count per country
    devs_per_country = df.groupby("Country").size().rename("so_developer_count").reset_index()

    # Employed developers only
    employed = df[df["Employment"].str.contains("Employed", na=False)]
    employed_count = employed.groupby("Country").size().rename("so_employed_dev_count").reset_index()

    # Median salary (where available)
    df["salary"] = pd.to_numeric(df["ConvertedCompYearly"], errors="coerce")
    salary = df.groupby("Country")["salary"].median().rename("so_median_salary_usd").reset_index()

    # Senior developer % (10+ years experience)
    df["years"] = pd.to_numeric(df["YearsCode"].replace("More than 50 years", "51")
                                               .replace("Less than 1 year", "0"),
                                errors="coerce")
    senior_pct = (df.groupby("Country")["years"]
                  .apply(lambda x: (x >= 10).sum() / len(x) * 100)
                  .rename("so_senior_dev_pct")
                  .reset_index())

    # Merge
    so = devs_per_country.merge(employed_count, on="Country", how="left")
    so = so.merge(salary, on="Country", how="left")
    so = so.merge(senior_pct, on="Country", how="left")
    so.rename(columns={"Country": "country"}, inplace=True)

    print(f"    Countries in output: {len(so)}")

    out = RAW_OUT / "stackoverflow_by_country.csv"
    so.to_csv(out, index=False)
    print(f"    Saved: {out.name} ({len(so)} rows)")

    return so


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 6 — World Bank API
# ═══════════════════════════════════════════════════════════════════════════════

def load_worldbank():
    print("\n[6/6] Extracting World Bank API data...")
    try:
        import wbdata
    except ImportError:
        print("    WARNING: wbdata not installed. Run: pip install wbdata")
        placeholder = pd.DataFrame(columns=["country"] + list(WB_INDICATORS.values()))
        placeholder.to_csv(RAW_OUT / "worldbank_indicators.csv", index=False)
        return placeholder

    # ISO2 codes for our 55 target countries only — much faster than "all"
    TARGET_ISO2 = [
        "JP", "CN", "KR", "SG", "HK", "TH", "ID", "IN", "MY", "PH", "VN",
        "AU", "GB", "FR", "DE", "NL", "ES", "IT", "AT", "CH", "SE", "NO",
        "DK", "FI", "PL", "CZ", "HU", "PT", "US", "CA", "MX", "BR", "AR",
        "CO", "PE", "CL", "AE", "IL", "TR", "EG", "KE", "NG", "ZA", "MA",
    ]

    # wbdata 1.1+ uses string dates
    date_range = ("2018", "2023")

    all_frames = []
    for indicator_id, col_name in WB_INDICATORS.items():
        try:
            df = wbdata.get_dataframe(
                {indicator_id: col_name},
                country=TARGET_ISO2,
                date=date_range,
            )
            df = df.reset_index()
            # Normalise column names (wbdata version differences)
            df.columns = [c.lower() for c in df.columns]
            country_col = next((c for c in df.columns if "country" in c), None)
            if country_col and country_col != "country":
                df.rename(columns={country_col: "country"}, inplace=True)
            # Average 2018-2023 per country
            df = df.groupby("country")[col_name].mean().reset_index()
            df = df[df[col_name].notna()]
            all_frames.append(df)
            print(f"    [OK] {col_name} — {len(df)} countries")
        except Exception as e:
            print(f"    [!!] {col_name} ({indicator_id}): {e}")

    if all_frames:
        wb = all_frames[0]
        for frame in all_frames[1:]:
            wb = wb.merge(frame, on="country", how="outer")
        print(f"    World Bank: {len(wb)} countries, {len(wb.columns)-1} indicators")
        out = RAW_OUT / "worldbank_indicators.csv"
        wb.to_csv(out, index=False)
        print(f"    Saved: {out.name}")
        return wb
    else:
        print("    No World Bank data retrieved.")
        placeholder = pd.DataFrame(columns=["country"] + list(WB_INDICATORS.values()))
        placeholder.to_csv(RAW_OUT / "worldbank_indicators.csv", index=False)
        return placeholder


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 7 — Build Master City List
# ═══════════════════════════════════════════════════════════════════════════════

# Country name mappings — different datasets use different spellings
COUNTRY_ALIASES = {
    "United States of America": "USA",
    "United States":             "USA",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "Korea, Republic of":        "South Korea",
    "Viet Nam":                  "Vietnam",
    "Russian Federation":        "Russia",
    "Iran, Islamic Republic of": "Iran",
    "Taiwan, Province of China": "Taiwan",
    "Hong Kong SAR, China":      "Hong Kong",
    "China, Hong Kong SAR":      "Hong Kong",
    "Czech Republic":            "Czechia",
}

# City → Country mapping for our target cities
CITY_COUNTRY = {
    "Tokyo": "Japan", "Shanghai": "China", "Beijing": "China",
    "Seoul": "South Korea", "Singapore": "Singapore", "Hong Kong": "Hong Kong",
    "Bangkok": "Thailand", "Jakarta": "Indonesia", "Mumbai": "India",
    "Delhi": "India", "Bangalore": "India", "Kuala Lumpur": "Malaysia",
    "Manila": "Philippines", "Ho Chi Minh City": "Vietnam",
    "Sydney": "Australia", "Melbourne": "Australia",
    "London": "United Kingdom", "Paris": "France", "Berlin": "Germany",
    "Amsterdam": "Netherlands", "Madrid": "Spain", "Barcelona": "Spain",
    "Rome": "Italy", "Milan": "Italy", "Vienna": "Austria",
    "Zurich": "Switzerland", "Stockholm": "Sweden", "Oslo": "Norway",
    "Copenhagen": "Denmark", "Helsinki": "Finland", "Warsaw": "Poland",
    "Prague": "Czechia", "Budapest": "Hungary", "Lisbon": "Portugal",
    "New York": "USA", "San Francisco": "USA", "Los Angeles": "USA",
    "Chicago": "USA", "Toronto": "Canada", "Vancouver": "Canada",
    "Mexico City": "Mexico", "Sao Paulo": "Brazil", "Buenos Aires": "Argentina",
    "Bogota": "Colombia", "Lima": "Peru", "Santiago": "Chile",
    "Dubai": "UAE", "Abu Dhabi": "UAE", "Tel Aviv": "Israel",
    "Istanbul": "Turkey", "Cairo": "Egypt", "Nairobi": "Kenya",
    "Lagos": "Nigeria", "Johannesburg": "South Africa", "Casablanca": "Morocco",
}

# Region mapping
CITY_REGION = {
    "Tokyo": "Asia-Pacific", "Shanghai": "Asia-Pacific", "Beijing": "Asia-Pacific",
    "Seoul": "Asia-Pacific", "Singapore": "Asia-Pacific", "Hong Kong": "Asia-Pacific",
    "Bangkok": "Asia-Pacific", "Jakarta": "Asia-Pacific", "Mumbai": "Asia-Pacific",
    "Delhi": "Asia-Pacific", "Bangalore": "Asia-Pacific", "Kuala Lumpur": "Asia-Pacific",
    "Manila": "Asia-Pacific", "Ho Chi Minh City": "Asia-Pacific",
    "Sydney": "Asia-Pacific", "Melbourne": "Asia-Pacific",
    "London": "Europe", "Paris": "Europe", "Berlin": "Europe",
    "Amsterdam": "Europe", "Madrid": "Europe", "Barcelona": "Europe",
    "Rome": "Europe", "Milan": "Europe", "Vienna": "Europe",
    "Zurich": "Europe", "Stockholm": "Europe", "Oslo": "Europe",
    "Copenhagen": "Europe", "Helsinki": "Europe", "Warsaw": "Europe",
    "Prague": "Europe", "Budapest": "Europe", "Lisbon": "Europe",
    "New York": "Americas", "San Francisco": "Americas", "Los Angeles": "Americas",
    "Chicago": "Americas", "Toronto": "Americas", "Vancouver": "Americas",
    "Mexico City": "Americas", "Sao Paulo": "Americas", "Buenos Aires": "Americas",
    "Bogota": "Americas", "Lima": "Americas", "Santiago": "Americas",
    "Dubai": "Middle East", "Abu Dhabi": "Middle East", "Tel Aviv": "Middle East",
    "Istanbul": "Middle East", "Cairo": "Africa & Middle East",
    "Nairobi": "Africa & Middle East", "Lagos": "Africa & Middle East",
    "Johannesburg": "Africa & Middle East", "Casablanca": "Africa & Middle East",
}


def build_master_city_list(coords_df, col_df, wb_df, temp_df, uni_df, so_df):
    print("\n[7/7] Building Master City List...")

    # Start from coordinates (all target cities with lat/lon)
    master = pd.DataFrame({
        "city":   TARGET_CITIES,
        "country": [CITY_COUNTRY[c] for c in TARGET_CITIES],
        "region":  [CITY_REGION[c]  for c in TARGET_CITIES],
    })

    # ── Merge coordinates ─────────────────────────────────────────────────────
    coords_clean = coords_df[["city", "latitude", "longitude", "population"]].copy()
    master = master.merge(coords_clean, on="city", how="left")

    # ── Merge Numbeo affordability ────────────────────────────────────────────
    numbeo_cols = ["city", "rent_1br_city_center", "rent_3br_city_center",
                   "avg_net_salary", "meal_inexpensive_restaurant",
                   "utilities_monthly_85m2", "price_per_m2_city_center",
                   "internet_monthly_60mbps", "monthly_pass_transport"]
    available_numbeo = [c for c in numbeo_cols if c in col_df.columns]
    master = master.merge(col_df[available_numbeo], on="city", how="left")

    # ── Merge temperature ─────────────────────────────────────────────────────
    master = master.merge(temp_df, on="city", how="left")

    # ── Normalise World Bank country names ───────────────────────────────────
    if len(wb_df) > 0 and "country" in wb_df.columns:
        wb_df["country_norm"] = wb_df["country"].replace(COUNTRY_ALIASES)
        wb_merge = wb_df.drop(columns=["country"]).rename(columns={"country_norm": "country"})
        master = master.merge(wb_merge, on="country", how="left")

    # ── Merge university rankings ─────────────────────────────────────────────
    if len(uni_df) > 0 and "country" in uni_df.columns:
        uni_copy = uni_df.copy()
        uni_copy["country_norm"] = uni_copy["country"].replace(COUNTRY_ALIASES)
        uni_merge = (uni_copy.drop(columns=["country"])
                             .rename(columns={"country_norm": "country"})
                             .drop_duplicates(subset=["country"]))
        master = master.merge(uni_merge, on="country", how="left")

    # ── Merge Stack Overflow ──────────────────────────────────────────────────
    if len(so_df) > 0 and "country" in so_df.columns:
        so_copy = so_df.copy()
        so_copy["country_norm"] = so_copy["country"].replace(COUNTRY_ALIASES)
        so_merge = so_copy.drop(columns=["country"]).rename(columns={"country_norm": "country"})
        master = master.merge(so_merge, on="country", how="left")

    # ── Data completeness check ───────────────────────────────────────────────
    total_cells = master.shape[0] * (master.shape[1] - 3)  # exclude city/country/region
    filled_cells = master.drop(columns=["city", "country", "region"]).notna().sum().sum()
    completeness = filled_cells / total_cells * 100 if total_cells > 0 else 0

    print(f"    Master city list: {len(master)} cities")
    print(f"    Columns: {len(master.columns)}")
    print(f"    Data completeness: {completeness:.1f}%")
    print(f"\n    Per-column fill rate:")
    for col in master.columns:
        if col not in ("city", "country", "region"):
            pct = master[col].notna().mean() * 100
            status = "OK" if pct >= 50 else "!!"
            print(f"      [{status}] {col}: {pct:.0f}%")

    out = RAW_OUT / "master_city_list_raw.csv"
    master.to_csv(out, index=False)
    print(f"\n    Saved: {out.name} ({len(master)} cities × {len(master.columns)} columns)")

    return master


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  CityMetric — Phase 1: Data Collection")
    print("=" * 60)
    print(f"  Output directory: {RAW_OUT}")

    col_df   = load_cost_of_living()
    coords_df = load_world_cities()
    temp_df  = load_city_temperature()
    uni_df   = load_university_rankings()
    so_df    = load_stackoverflow()
    wb_df    = load_worldbank()
    master   = build_master_city_list(coords_df, col_df, wb_df, temp_df, uni_df, so_df)

    print("\n" + "=" * 60)
    print("  Phase 1 COMPLETE")
    print(f"  Files saved to: {RAW_OUT}")
    print("  Files created:")
    for f in sorted(RAW_OUT.iterdir()):
        size_kb = f.stat().st_size / 1024
        print(f"    {f.name:<45} {size_kb:>8.1f} KB")
    print("=" * 60)
    print("\n  Next step: run scripts/02_data_preprocessing.py")


if __name__ == "__main__":
    main()
