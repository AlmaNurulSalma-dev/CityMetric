"""
CityMetric - Phase 3: ARFF Conversion + K-Means Clustering

Two outputs:
  1. weka/cities.arff          — load this into WEKA GUI for official clustering
  2. data/processed/cities_clustered.csv — sklearn K-Means results (same pipeline)

When you run WEKA SimpleKMeans, replace weka/weka_cluster_assignments.txt
with the exported WEKA output, then re-run the bottom section to merge.
"""

import warnings
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")   # non-interactive backend (no display needed)
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

warnings.filterwarnings("ignore")

ROOT     = Path(__file__).resolve().parent.parent
PROC_OUT = ROOT / "data" / "processed"
WEKA_DIR = ROOT / "weka"
VIZ_DIR  = ROOT / "output"
WEKA_DIR.mkdir(parents=True, exist_ok=True)
VIZ_DIR.mkdir(parents=True, exist_ok=True)

# Features used for clustering (startup_score excluded — no real data)
CLUSTER_FEATURES = [
    "affordability_score",
    "digital_score",
    "urban_score",
    "innovation_score",
    "talent_score",
    "growth_score",
]

# Pastel cluster colours matching project Y2K aesthetic
CLUSTER_COLORS = {
    0: "#FFB6D9",   # pastel pink
    1: "#C8A2E8",   # pastel purple
    2: "#B4D7FF",   # pastel blue
    3: "#FFE8B6",   # pastel peach
    4: "#B4FFD7",   # pastel mint
}


# ===============================================================================
# PART A — ARFF CONVERSION  (input file for WEKA GUI)
# ===============================================================================

def convert_to_arff(df):
    print("\n[A] Converting to ARFF format for WEKA...")

    lines = [
        "@relation city_opportunity",
        "",
    ]
    # Attributes
    lines.append("@attribute city string")
    lines.append("@attribute country string")
    lines.append("@attribute region string")
    for feat in CLUSTER_FEATURES:
        lines.append(f"@attribute {feat} numeric")
    lines.append("")
    lines.append("@data")

    # Data rows
    for _, row in df.iterrows():
        city    = str(row["city"]).replace("'", "")
        country = str(row["country"]).replace("'", "")
        region  = str(row["region"]).replace("'", "")
        vals    = ",".join(f"{row[f]:.4f}" for f in CLUSTER_FEATURES)
        lines.append(f"'{city}','{country}','{region}',{vals}")

    arff_path = WEKA_DIR / "cities.arff"
    with open(arff_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"    Saved: {arff_path}")
    print(f"    Rows: {len(df)}  |  Features: {len(CLUSTER_FEATURES)}")
    print(f"\n    --- WEKA INSTRUCTIONS ---")
    print(f"    1. Open WEKA GUI Chooser -> Explorer")
    print(f"    2. Preprocess tab -> Open file -> {arff_path}")
    print(f"    3. Cluster tab -> Choose -> SimpleKMeans")
    print(f"    4. Set numClusters=5, seed=42")
    print(f"    5. Cluster mode: 'Use training set'")
    print(f"    6. Start -> copy results to {WEKA_DIR / 'weka_cluster_output.txt'}")
    print(f"    -------------------------")


# ===============================================================================
# PART B — FIND OPTIMAL K  (Elbow + Silhouette)
# ===============================================================================

def find_optimal_k(X_scaled, df):
    print("\n[B] Finding optimal K (Elbow + Silhouette)...")

    inertias, silhouettes = [], []
    k_range = range(2, 11)

    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(X_scaled)
        inertias.append(km.inertia_)
        silhouettes.append(silhouette_score(X_scaled, labels))
        print(f"    K={k}  inertia={km.inertia_:.1f}  silhouette={silhouette_score(X_scaled, labels):.3f}")

    best_k = k_range[int(np.argmax(silhouettes))]
    print(f"\n    Best K by silhouette score: K={best_k}")

    # ── Plot elbow + silhouette ───────────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    fig.patch.set_facecolor("#FFF0F8")

    ax1.plot(list(k_range), inertias, "o-", color="#C8A2E8", linewidth=2, markersize=8)
    ax1.axvline(x=best_k, color="#FF6B9D", linestyle="--", alpha=0.7, label=f"K={best_k}")
    ax1.set_title("Elbow Curve", fontsize=13, fontweight="bold")
    ax1.set_xlabel("Number of Clusters (K)")
    ax1.set_ylabel("Inertia (WCSS)")
    ax1.set_facecolor("#FFF8FC")
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(list(k_range), silhouettes, "o-", color="#FFB6D9", linewidth=2, markersize=8)
    ax2.axvline(x=best_k, color="#C8A2E8", linestyle="--", alpha=0.7, label=f"K={best_k}")
    ax2.set_title("Silhouette Score", fontsize=13, fontweight="bold")
    ax2.set_xlabel("Number of Clusters (K)")
    ax2.set_ylabel("Silhouette Score")
    ax2.set_facecolor("#FFF8FC")
    ax2.legend()
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    out = VIZ_DIR / "elbow_silhouette.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"    Saved: {out.name}")

    return best_k


# ===============================================================================
# PART C — RUN K-MEANS (K=5, matching WEKA specification)
# ===============================================================================

CLUSTER_NAMES = {
    0: "Emerging Markets",
    1: "Established Hubs",
    2: "Digital Leaders",
    3: "Balanced Cities",
    4: "Rising Stars",
}

def run_kmeans(X_scaled, df, k=5):
    print(f"\n[C] Running K-Means clustering (K={k}, seed=42)...")

    km = KMeans(n_clusters=k, random_state=42, n_init=20, max_iter=300)
    labels = km.fit_predict(X_scaled)

    sil  = silhouette_score(X_scaled, labels)
    db   = davies_bouldin_score(X_scaled, labels)
    print(f"    Silhouette score : {sil:.4f}  (target > 0.3)")
    print(f"    Davies-Bouldin   : {db:.4f}   (lower = better)")

    df = df.copy()
    df["cluster"]      = labels
    df["cluster_name"] = df["cluster"].map(CLUSTER_NAMES)

    # Re-label clusters semantically based on centroids
    centroids = df.groupby("cluster")[CLUSTER_FEATURES].mean()
    centroids["overall"] = centroids.mean(axis=1)
    ranked = centroids["overall"].rank(ascending=True).astype(int) - 1
    semantic = {
        0: "Emerging Markets",
        1: "Rising Stars",
        2: "Balanced Cities",
        3: "Digital Leaders",
        4: "Established Hubs",
    }
    df["cluster_name"] = df["cluster"].map(ranked).map(semantic)

    # Print cluster sizes
    print("\n    Cluster sizes:")
    for c in sorted(df["cluster"].unique()):
        name  = df.loc[df["cluster"] == c, "cluster_name"].iloc[0]
        cities = df.loc[df["cluster"] == c, "city"].tolist()
        print(f"      Cluster {c} [{name}] ({len(cities)} cities): {', '.join(sorted(cities))}")

    return df, km, sil, db


# ===============================================================================
# PART D — CLUSTER PROFILES & WEKA-COMPATIBLE OUTPUT
# ===============================================================================

def build_cluster_profiles(df):
    print("\n[D] Building cluster profiles...")

    profiles = (df.groupby(["cluster", "cluster_name"])[CLUSTER_FEATURES + ["opportunity_index"]]
                  .agg(["mean", "std", "min", "max"])
                  .round(3))

    out = PROC_OUT / "cluster_profiles.csv"
    profiles.to_csv(out)
    print(f"    Saved: {out.name}")

    # Also save WEKA-style assignment file (so 04_weka_results_import.py works)
    assignments = df[["city", "country", "cluster", "cluster_name"]].copy()
    assignments_path = WEKA_DIR / "weka_cluster_assignments.txt"
    with open(assignments_path, "w", encoding="utf-8") as fh:
        fh.write("=== Cluster Assignments (Python sklearn K-Means K=5) ===\n\n")
        for _, row in assignments.iterrows():
            fh.write(f"{row['city']} -> Cluster {row['cluster']} ({row['cluster_name']})\n")
    print(f"    Saved: {assignments_path.name}  (replace with WEKA output when ready)")

    # Save centroids
    centroids = df.groupby("cluster")[CLUSTER_FEATURES].mean().round(4)
    centroids_path = WEKA_DIR / "weka_cluster_centroids.txt"
    with open(centroids_path, "w", encoding="utf-8") as fh:
        fh.write("=== Cluster Centroids (sklearn K-Means K=5) ===\n\n")
        fh.write(centroids.to_string())
    print(f"    Saved: {centroids_path.name}")

    return profiles


# ===============================================================================
# PART E — VISUALISATIONS
# ===============================================================================

def plot_cluster_radar(df):
    """Radar chart showing each cluster's dimension profile."""
    print("\n[E] Creating cluster radar charts...")

    cats     = CLUSTER_FEATURES
    n_cats   = len(cats)
    angles   = np.linspace(0, 2 * np.pi, n_cats, endpoint=False).tolist()
    angles  += angles[:1]

    fig, axes = plt.subplots(1, 5, figsize=(22, 5), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("#FFF0F8")
    fig.suptitle("CityMetric — Cluster Profiles", fontsize=15, fontweight="bold", y=1.02)

    clusters = sorted(df["cluster"].unique())
    for ax, c in zip(axes, clusters):
        name   = df.loc[df["cluster"] == c, "cluster_name"].iloc[0]
        means  = df.loc[df["cluster"] == c, cats].mean().tolist()
        means += means[:1]
        color  = CLUSTER_COLORS.get(c, "#CCCCCC")

        ax.plot(angles, means, "o-", linewidth=2, color=color)
        ax.fill(angles, means, alpha=0.3, color=color)
        ax.set_xticks(angles[:-1])
        labels = ["Afford", "Digital", "Urban", "Innov", "Talent", "Growth"]
        ax.set_xticklabels(labels, size=8)
        ax.set_ylim(0, 10)
        ax.set_yticks([2, 4, 6, 8])
        ax.set_yticklabels(["2", "4", "6", "8"], size=6)
        ax.set_title(f"C{c}: {name}\n({len(df[df['cluster']==c])} cities)",
                     size=9, fontweight="bold", pad=10)
        ax.set_facecolor("#FFFAFD")
        ax.grid(color="#E8D5F0", linewidth=0.5)

    plt.tight_layout()
    out = VIZ_DIR / "cluster_radar.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"    Saved: {out.name}")


def plot_scatter_clusters(df):
    """2D scatter: Affordability vs Opportunity, coloured by cluster."""
    print("    Creating scatter plot...")
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("#FFF0F8")
    ax.set_facecolor("#FFF8FC")

    for c in sorted(df["cluster"].unique()):
        sub   = df[df["cluster"] == c]
        color = CLUSTER_COLORS.get(c, "#CCCCCC")
        name  = sub["cluster_name"].iloc[0]
        ax.scatter(sub["affordability_score"], sub["opportunity_index"],
                   c=color, s=100, alpha=0.85, edgecolors="white",
                   linewidth=0.8, label=f"C{c}: {name}", zorder=3)

    # Annotate city names
    for _, row in df.iterrows():
        ax.annotate(row["city"], (row["affordability_score"], row["opportunity_index"]),
                    fontsize=6.5, ha="center", va="bottom", alpha=0.75,
                    xytext=(0, 4), textcoords="offset points")

    ax.set_xlabel("Affordability Score", fontsize=11)
    ax.set_ylabel("Opportunity Index", fontsize=11)
    ax.set_title("City Clusters — Affordability vs Opportunity", fontsize=13, fontweight="bold")
    ax.legend(loc="lower right", fontsize=8, framealpha=0.9)
    ax.grid(alpha=0.25)

    out = VIZ_DIR / "scatter_afford_vs_opportunity.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"    Saved: {out.name}")


def plot_top_cities_bar(df):
    """Horizontal bar chart of top 20 cities by opportunity index."""
    print("    Creating rankings bar chart...")
    top = df.nlargest(20, "opportunity_index").sort_values("opportunity_index")

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#FFF0F8")
    ax.set_facecolor("#FFF8FC")

    colors = [CLUSTER_COLORS.get(c, "#CCCCCC") for c in top["cluster"]]
    bars = ax.barh(top["city"], top["opportunity_index"], color=colors,
                   edgecolor="white", linewidth=0.8)

    # Value labels
    for bar, val in zip(bars, top["opportunity_index"]):
        ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height() / 2,
                f"{val:.2f}", va="center", fontsize=8)

    # Legend
    legend_patches = [mpatches.Patch(color=CLUSTER_COLORS[c],
                      label=df.loc[df["cluster"]==c,"cluster_name"].iloc[0])
                      for c in sorted(df["cluster"].unique())]
    ax.legend(handles=legend_patches, loc="lower right", fontsize=8)

    ax.set_xlabel("Opportunity Index (0-10)", fontsize=11)
    ax.set_title("CityMetric — Top 20 Cities by Opportunity", fontsize=13, fontweight="bold")
    ax.set_xlim(0, df["opportunity_index"].max() + 0.8)
    ax.grid(axis="x", alpha=0.25)

    out = VIZ_DIR / "top20_cities_ranking.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"    Saved: {out.name}")


# ===============================================================================
# MAIN
# ===============================================================================

def main():
    print("=" * 60)
    print("  CityMetric — Phase 3: ARFF + Clustering")
    print("=" * 60)

    # Load features
    df = pd.read_csv(PROC_OUT / "cities_features.csv")
    print(f"  Loaded cities_features.csv: {len(df)} cities")

    # ── Scale features for clustering ─────────────────────────────────────────
    scaler   = MinMaxScaler()
    X_scaled = scaler.fit_transform(df[CLUSTER_FEATURES])

    # ── A: ARFF ───────────────────────────────────────────────────────────────
    convert_to_arff(df)

    # ── B: Optimal K ──────────────────────────────────────────────────────────
    best_k = find_optimal_k(X_scaled, df)

    # ── C: K-Means K=5 (project spec + WEKA requirement) ─────────────────────
    df_clustered, km_model, sil, db = run_kmeans(X_scaled, df, k=5)

    # ── D: Profiles & WEKA-format output ──────────────────────────────────────
    build_cluster_profiles(df_clustered)

    # ── E: Visualisations ────────────────────────────────────────────────────
    plot_cluster_radar(df_clustered)
    plot_scatter_clusters(df_clustered)
    plot_top_cities_bar(df_clustered)

    # ── Save final clustered dataset ──────────────────────────────────────────
    out = PROC_OUT / "cities_clustered.csv"
    df_clustered.to_csv(out, index=False)
    print(f"\n    Saved: {out.name} ({len(df_clustered)} cities)")

    # ── Save evaluation metrics ───────────────────────────────────────────────
    metrics_path = WEKA_DIR / "weka_evaluation_metrics.txt"
    with open(metrics_path, "w", encoding="utf-8") as fh:
        fh.write("=== CityMetric Clustering Evaluation ===\n\n")
        fh.write(f"Algorithm   : K-Means (sklearn, replicates WEKA SimpleKMeans)\n")
        fh.write(f"K           : 5\n")
        fh.write(f"Seed        : 42\n")
        fh.write(f"Features    : {', '.join(CLUSTER_FEATURES)}\n")
        fh.write(f"Cities      : {len(df_clustered)}\n\n")
        fh.write(f"Silhouette Score  : {sil:.4f}  (range -1 to 1, higher=better, target>0.3)\n")
        fh.write(f"Davies-Bouldin    : {db:.4f}  (lower=better)\n\n")
        fh.write("Cluster sizes:\n")
        for c in sorted(df_clustered["cluster"].unique()):
            name = df_clustered.loc[df_clustered["cluster"]==c,"cluster_name"].iloc[0]
            n    = len(df_clustered[df_clustered["cluster"]==c])
            fh.write(f"  Cluster {c} [{name}]: {n} cities\n")
    print(f"    Saved: {metrics_path.name}")

    print("\n" + "=" * 60)
    print("  Phase 3 COMPLETE")
    print(f"  Silhouette: {sil:.4f}  |  Davies-Bouldin: {db:.4f}")
    print()
    print("  Files in weka/:")
    for f in sorted(WEKA_DIR.iterdir()):
        print(f"    {f.name:<45} {f.stat().st_size/1024:.1f} KB")
    print()
    print("  Files in output/:")
    for f in sorted(VIZ_DIR.iterdir()):
        print(f"    {f.name:<45} {f.stat().st_size/1024:.1f} KB")
    print("=" * 60)
    print("\n  Next: run scripts/04_visualization.py")
    print("  Or:   load weka/cities.arff in WEKA GUI and run SimpleKMeans K=5")


if __name__ == "__main__":
    main()
