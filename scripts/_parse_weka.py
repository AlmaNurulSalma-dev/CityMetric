import pandas as pd
from pathlib import Path

ROOT  = Path(r"C:\Users\kinet\OneDrive\Documents\PROJECT-ALMAAA\CityMetric")
FEATS = ["affordability_score","digital_score","urban_score",
         "innovation_score","talent_score","growth_score"]

# ── Read WEKA output ARFF ────────────────────────────────────────────────────
arff_lines = (ROOT / "weka/cities_clustered_weka.arff").read_text().splitlines()
data_start  = next(i for i,l in enumerate(arff_lines) if l.strip().lower() == "@data") + 1
data_rows   = [l for l in arff_lines[data_start:] if l.strip()]

weka_clusters = [row.strip().split(",")[-1].strip() for row in data_rows]

# ── Map to city names (same row order as ARFF input) ─────────────────────────
df = pd.read_csv(ROOT / "data/processed/cities_features.csv")
df["weka_cluster_raw"] = weka_clusters
df["weka_cluster_id"]  = df["weka_cluster_raw"].str.replace("cluster","").astype(int) - 1

# ── Print assignments ─────────────────────────────────────────────────────────
print("WEKA SimpleKMeans K=5 - City Assignments")
print("=" * 55)
for c in sorted(df["weka_cluster_id"].unique()):
    cities = sorted(df.loc[df["weka_cluster_id"]==c, "city"].tolist())
    print(f"\n  Cluster {c} ({len(cities)} cities):")
    print(f"    {', '.join(cities)}")

# ── Save assignment text file ─────────────────────────────────────────────────
lines = [
    "=== WEKA SimpleKMeans K=5 Cluster Assignments ===",
    "Algorithm  : weka.clusterers.SimpleKMeans",
    "Parameters : numClusters=5, seed=42, maxIterations=300",
    "Distance   : EuclideanDistance",
    "Input file : weka/cities_numeric.arff",
    "",
]
for c in sorted(df["weka_cluster_id"].unique()):
    sub = df[df["weka_cluster_id"]==c].sort_values("city")
    lines.append(f"--- Cluster {c} ({len(sub)} cities) ---")
    for _, row in sub.iterrows():
        lines.append(f"  {row['city']} ({row['country']}) -> Cluster {c}")
    lines.append("")

(ROOT / "weka/weka_cluster_assignments.txt").write_text("\n".join(lines), encoding="utf-8")
print("\nSaved: weka_cluster_assignments.txt")

# ── Save clustered CSV ────────────────────────────────────────────────────────
df.to_csv(ROOT / "weka/cities_weka_clustered.csv", index=False)
print("Saved: cities_weka_clustered.csv")

# ── Cluster size summary ──────────────────────────────────────────────────────
print(f"\nCluster sizes: {df.groupby('weka_cluster_id').size().to_dict()}")
