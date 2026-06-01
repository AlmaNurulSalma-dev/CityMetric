# 🎯 CITYMETRIC - PROJECT SETUP GUIDE

## 📁 COMPLETE FOLDER STRUCTURE FOR CITYMETRIC

Follow this structure when setting up your project:

```
citymetric/
│
├── 📁 data_sources/  ← Download datasets here
│   ├── 01_affordability_cost_of_living/
│   │   ├── metadata.txt
│   │   └── cost_of_living.csv
│   │
│   ├── 02_digital_worldbank_api/
│   │   ├── metadata.txt
│   │   ├── internet_penetration.csv
│   │   ├── broadband_subscriptions.csv
│   │   └── mobile_subscriptions.csv
│   │
│   ├── 03_urban_world_cities/
│   │   ├── metadata.txt
│   │   └── worldcities.csv
│   │
│   ├── 04_urban_city_temperature/
│   │   ├── metadata.txt
│   │   └── city_temperature.csv
│   │
│   ├── 05_innovation_university_rankings/
│   │   ├── metadata.txt
│   │   └── university_rankings.csv
│   │
│   └── 06_talent_stackoverflow_survey/
│       ├── metadata.txt
│       └── survey_results_public.csv
│
├── 📁 data/  ← Processed data at each stage
│   ├── raw/
│   │   └── (Copy of data_sources CSVs)
│   │
│   ├── processed/
│   │   ├── cities_cleaned.csv
│   │   ├── cities_features.csv
│   │   ├── cities.arff (FOR WEKA)
│   │   └── cities_clustered_weka.csv (FROM WEKA)
│   │
│   └── final/
│       ├── citymetric_index_final.csv
│       ├── cities_clusters.csv
│       ├── cluster_profiles.csv
│       └── feature_analysis.csv
│
├── 📁 scripts/  ← Claude Code Python artifacts
│   ├── 01_data_collection.py
│   ├── 02_data_preprocessing.py
│   ├── 03_feature_engineering.py
│   ├── 04_arff_conversion.py (CONVERT CSV → ARFF for WEKA)
│   ├── 05_weka_results_import.py (IMPORT WEKA results)
│   ├── 06_visualizations.py
│   └── 07_streamlit_app.py
│
├── 📁 output/
│   ├── citymetric_map_interactive.html (Folium map)
│   ├── citymetric_charts_analysis.html (Plotly charts)
│   ├── citymetric_cluster_analysis_report.pdf
│   └── visualizations/
│       ├── radar_chart_cluster_profiles.png
│       ├── correlation_heatmap.png
│       ├── silhouette_analysis.png
│       └── city_rankings.png
│
├── 📁 docs/
│   ├── README.md (overview)
│   ├── METHODOLOGY.md (technical approach)
│   ├── DATA_SOURCES.md (source documentation)
│   ├── FINDINGS.md (key insights)
│   ├── CODE_STRUCTURE.md (developer guide)
│   ├── DEPLOYMENT.md (how to deploy)
│   ├── Data_Dictionary.txt (column definitions)
│   └── CITYMETRIC_Analysis_Report.pdf
│
├── 📁 weka/  ← WEKA FILES (IMPORTANT!)
│   ├── cities.arff (INPUT to WEKA)
│   ├── weka_cluster_assignments.txt (FROM WEKA)
│   ├── weka_cluster_centroids.txt (FROM WEKA)
│   ├── weka_evaluation_metrics.txt (FROM WEKA)
│   └── weka_visualization.png (screenshot from WEKA)
│
├── .gitignore
├── requirements.txt
├── streamlit_app.py (main dashboard)
├── README.md (root level)
└── PROJECT_STRUCTURE.md (this file)
```

---

## ⚡ QUICK SETUP CHECKLIST

### Step 1: Create Main Folder
```bash
mkdir citymetric
cd citymetric
```

### Step 2: Create Subfolders
```bash
# Data folders
mkdir -p data_sources/{01_affordability_cost_of_living,02_digital_worldbank_api,03_urban_world_cities,04_urban_city_temperature,05_innovation_university_rankings,06_talent_stackoverflow_survey}
mkdir -p data/{raw,processed,final}

# Code & output
mkdir -p scripts output docs weka

# Create metadata.txt in each data_sources folder
touch data_sources/01_affordability_cost_of_living/metadata.txt
touch data_sources/02_digital_worldbank_api/metadata.txt
touch data_sources/03_urban_world_cities/metadata.txt
touch data_sources/04_urban_city_temperature/metadata.txt
touch data_sources/05_innovation_university_rankings/metadata.txt
touch data_sources/06_talent_stackoverflow_survey/metadata.txt
```

### Step 3: Download Datasets
Follow the `DATA_DOWNLOAD_GUIDE.md` to download 6 datasets into corresponding folders

### Step 4: GitHub Setup
```bash
git init
git add .
git commit -m "Initial CityMetric project setup"
git branch -M main
git remote add origin https://github.com/[username]/citymetric
git push -u origin main
```

### Step 5: Create README.md
Create `citymetric/README.md` (at root level) with project overview

---

## 📥 WHAT GOES IN EACH FOLDER

### data_sources/
```
Raw CSV files directly from Kaggle/APIs
✅ No processing
✅ Original format from sources
✅ Metadata documentation for each
```

### data/raw/
```
Copy of data_sources for backup
✅ Safety copy of original files
✅ Before any processing
```

### data/processed/
```
After data cleaning & feature engineering
✅ cities_cleaned.csv (after validation)
✅ cities_features.csv (after feature engineering)
✅ cities.arff (WEKA input format)
✅ cities_clustered_weka.csv (AFTER running WEKA)
```

### data/final/
```
Final analysis-ready datasets
✅ citymetric_index_final.csv (master dataset)
✅ cities_clusters.csv (with cluster assignments)
✅ cluster_profiles.csv (statistics per cluster)
✅ feature_analysis.csv (importance metrics)
```

### scripts/
```
Claude Code Python artifacts
✅ 01_data_collection.py
✅ 02_data_preprocessing.py
✅ 03_feature_engineering.py
✅ 04_arff_conversion.py (CSV → ARFF for WEKA)
✅ 05_weka_results_import.py (WEKA → CSV)
✅ 06_visualizations.py
✅ 07_streamlit_app.py
```

### output/
```
Generated deliverables
✅ Interactive HTML maps
✅ Interactive HTML charts
✅ PDF reports
✅ PNG visualizations
```

### weka/
```
WEKA clustering files (NEW FOLDER!)
✅ cities.arff (INPUT - send to WEKA)
✅ weka_cluster_assignments.txt (OUTPUT - from WEKA)
✅ weka_cluster_centroids.txt (OUTPUT - from WEKA)
✅ weka_evaluation_metrics.txt (OUTPUT - from WEKA)
✅ weka_visualization.png (screenshot from WEKA GUI)
```

### docs/
```
All documentation
✅ README.md
✅ METHODOLOGY.md
✅ DATA_SOURCES.md
✅ FINDINGS.md
✅ CODE_STRUCTURE.md
✅ DEPLOYMENT.md
✅ Data_Dictionary.txt
✅ CITYMETRIC_Analysis_Report.pdf
```

---

## 🎯 NAMING CONVENTIONS

### File Naming
```
✅ All output files prefixed with "citymetric_"
   Examples:
   - citymetric_map_interactive.html
   - citymetric_charts_analysis.html
   - citymetric_cluster_analysis_report.pdf
   - citymetric_index_final.csv

✅ Data files clear and descriptive
   Examples:
   - cities_cleaned.csv
   - cities_features.csv
   - cities_clustered_weka.csv
   - cluster_profiles.csv

✅ WEKA files clearly marked
   Examples:
   - cities.arff (input)
   - weka_cluster_assignments.txt (output)
   - weka_evaluation_metrics.txt (output)
```

### Folder Naming
```
✅ Numbered for ordering: 01_, 02_, etc.
✅ Descriptive: affordability_cost_of_living, etc.
✅ Lowercase with underscores: snake_case
```

---

## 🔄 DATA FLOW DIAGRAM

```
RAW DATA SOURCES
    ↓
data_sources/ (Downloaded CSVs)
    ↓
data/raw/ (Backup copy)
    ↓
PHASE 1 Scripts: 01_data_collection.py
    ↓
data/processed/cities_cleaned.csv
    ↓
PHASE 2 Scripts: 02_data_preprocessing.py
    ↓
data/processed/cities_features.csv
    ↓
PHASE 3 Scripts: 03_feature_engineering.py
    ↓
data/processed/cities_features.csv (enhanced)
    ↓
PHASE 3 Scripts: 04_arff_conversion.py
    ↓
weka/cities.arff (SEND TO WEKA!)
    ↓
    └─→ WEKA GUI: SimpleKMeans Clustering
        ↓
    ┌───→ weka/weka_cluster_assignments.txt
    │
PHASE 3 Scripts: 05_weka_results_import.py
    ↓
data/processed/cities_clustered_weka.csv
    ↓
PHASE 4 Scripts: 06_visualizations.py
    ↓
output/citymetric_map_interactive.html
output/citymetric_charts_analysis.html
output/citymetric_cluster_analysis_report.pdf
    ↓
PHASE 5 Scripts: 07_streamlit_app.py
    ↓
Streamlit Cloud Dashboard (LIVE!)
```

---

## ✅ PHASE-BY-PHASE DELIVERABLES

### PHASE 1: Data Collection
```
├─ Download 6 datasets
├─ Place in data_sources/
├─ Verify file integrity
└─ Total: ~410 MB
```

### PHASE 2: Data Preprocessing
```
├─ data/processed/cities_cleaned.csv
├─ data/processed/cities_features.csv
└─ All dimensions populated (0-10 scores)
```

### PHASE 3: Clustering with WEKA ⭐
```
├─ INPUT: weka/cities.arff (from script 04)
├─ PROCESS: WEKA GUI SimpleKMeans
├─ OUTPUT: weka/weka_cluster_assignments.txt
├─ OUTPUT: weka/weka_cluster_centroids.txt
├─ OUTPUT: weka/weka_evaluation_metrics.txt
├─ Python: script 05 imports results
└─ RESULT: data/processed/cities_clustered_weka.csv
```

### PHASE 4: Visualization
```
├─ output/citymetric_map_interactive.html
├─ output/citymetric_charts_analysis.html
├─ output/citymetric_cluster_analysis_report.pdf
└─ output/visualizations/*.png
```

### PHASE 5: Dashboard
```
├─ streamlit_app.py (7 pages)
├─ Deploy to Streamlit Cloud
└─ Live URL: https://citymetric.streamlit.app
```

### PHASE 6: Documentation
```
├─ docs/README.md
├─ docs/METHODOLOGY.md
├─ docs/DATA_SOURCES.md
├─ docs/FINDINGS.md
├─ docs/CODE_STRUCTURE.md
├─ docs/DEPLOYMENT.md
├─ docs/Data_Dictionary.txt
└─ docs/CITYMETRIC_Analysis_Report.pdf
```

### FINAL OUTPUTS
```
├─ data/final/citymetric_index_final.csv
├─ data/final/cities_clusters.csv
├─ data/final/cluster_profiles.csv
├─ data/final/feature_analysis.csv
└─ GitHub repository (public, well-documented)
```

---

## 📊 KEY FILES TO REMEMBER

### Most Important Files:

```
🔥 FOR SUBMISSION / PORTFOLIO:
   ├─ README.md (root level - project overview)
   ├─ output/citymetric_map_interactive.html (show to people!)
   ├─ output/citymetric_cluster_analysis_report.pdf (read this!)
   ├─ Streamlit live URL (https://citymetric.streamlit.app)
   └─ GitHub repo (github.com/[username]/citymetric)

🔑 FOR WEKA CLUSTERING:
   ├─ weka/cities.arff (INPUT to WEKA)
   ├─ weka/weka_cluster_assignments.txt (OUTPUT from WEKA)
   └─ data/processed/cities_clustered_weka.csv (final clustered data)

📊 FOR ANALYSIS:
   ├─ data/final/citymetric_index_final.csv (master dataset)
   ├─ data/final/cluster_profiles.csv (cluster statistics)
   └─ output/citymetric_charts_analysis.html (interactive analysis)
```

---

## 🚀 NEXT STEPS

1. **Create folder structure** (use checklist above)
2. **Download datasets** (follow DATA_DOWNLOAD_GUIDE.md)
3. **Run Phase 1-2 scripts** (data processing)
4. **Convert to ARFF** (script 04)
5. **Run WEKA clustering** (WEKA GUI)
6. **Import WEKA results** (script 05)
7. **Create visualizations** (script 06)
8. **Deploy dashboard** (script 07)
9. **Complete documentation** (docs/)
10. **Push to GitHub** (git push)

---

## 💡 TIPS

```
✅ DO THIS:
   - Create folder structure first (before downloading)
   - Download Priority 1 datasets first
   - Test each script before moving to next phase
   - Commit to GitHub frequently
   - Check WEKA outputs carefully
   - Document findings as you go

❌ AVOID THIS:
   - Forgetting to backup original data (use data/raw/)
   - Skipping WEKA step (it's required!)
   - Not verifying data after download
   - Committing to GitHub without .gitignore
   - Large files in Git (use data/ folder which can be .gitignored)
```

---

**Ready to set up CityMetric? Let's go! 🚀📊**