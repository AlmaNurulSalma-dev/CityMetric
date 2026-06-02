"""Generate extra ARFF files for advanced WEKA analyses."""
import pandas as pd
from pathlib import Path

ROOT  = Path(r"C:\Users\kinet\OneDrive\Documents\PROJECT-ALMAAA\CityMetric")
WEKA  = ROOT / "weka"
df    = pd.read_csv(ROOT / "data/processed/cities_clustered.csv")

FEATS = ["affordability_score","digital_score","urban_score",
         "innovation_score","talent_score","growth_score"]

# ── 1. cities_with_class.arff — for J48 / Classification ─────────────────────
# Same 6 numeric features + cluster_name as class label
cluster_labels = sorted(df["cluster_name"].unique())
class_vals = ",".join(f'"{n}"' for n in cluster_labels)

lines = ["@relation city_clusters_classified", ""]
for f in FEATS:
    lines.append(f"@attribute {f} numeric")
lines.append(f"@attribute cluster_class {{{class_vals}}}")
lines += ["", "@data"]
for _, row in df.iterrows():
    vals = ",".join(f"{row[f]:.4f}" for f in FEATS)
    lines.append(f'{vals},"{row["cluster_name"]}"')

out1 = WEKA / "cities_with_class.arff"
out1.write_text("\n".join(lines), encoding="utf-8")
print(f"Saved: {out1.name}  ({len(df)} instances)")
print(f"  Class labels: {cluster_labels}")

# ── 2. cities_numeric.arff — already exists, just confirm ─────────────────────
out2 = WEKA / "cities_numeric.arff"
if out2.exists():
    print(f"Exists: {out2.name}  (use for SimpleKMeans / EM / Hierarchical)")
else:
    print(f"Missing: {out2.name} — run 03_clustering.py first")

print("\nAll WEKA input files ready:")
for f in sorted(WEKA.iterdir()):
    if f.suffix == ".arff":
        print(f"  {f.name:<35} {f.stat().st_size/1024:.1f} KB")
