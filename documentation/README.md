# 📊 CityMetric
## Measure Your City, Measure Your Future

**A data-driven platform for global urban opportunity analysis**

---

## 🎯 PROJECT OVERVIEW

```
Project Name: CityMetric
Tagline: "Measure Your City, Measure Your Future"

Description: Comprehensive multi-dimensional analysis of 50-70 global cities
            across 7 key dimensions (affordability, digital infrastructure,
            startup ecosystem, urban development, innovation, talent, growth).
            
            Using data mining (WEKA K-means clustering), geospatial
            visualization (Folium), and interactive dashboard (Streamlit),
            CityMetric provides actionable insights for individuals and
            organizations looking to move, invest, or build in the right city.

Type: Full-stack data engineering + analytics + data mining project
Scope: 50-70 cities, 7 dimensions, 50+ features
Timeline: 4 weeks
Tech Stack: Python (Claude Code) + WEKA + Folium + Plotly + Streamlit
Deployment: Streamlit Cloud (FREE)
Portfolio Value: ⭐⭐⭐⭐⭐ (Highly impressive for competitions & employers)
```

---

## 🌟 WHY CITYMETRIC?

```
✅ FIND YOUR CITY
   Discover the perfect city that matches your goals,
   lifestyle, and career aspirations

✅ DATA-DRIVEN DECISIONS
   50+ metrics across 7 dimensions analyzed with
   scientific rigor

✅ GLOBAL PERSPECTIVE
   Compare 50-70 major cities worldwide across
   multiple factors

✅ ACTIONABLE INSIGHTS
   Get cluster-based city recommendations based
   on your priorities

✅ BEAUTIFUL VISUALIZATIONS
   Interactive maps, radar charts, and detailed
   analytics dashboards

✅ COMPETITIVE EDGE
   Win hackathons, competitions, and impress employers
   with your analytical portfolio
```

---

## 📊 THE 7 DIMENSIONS

| # | Dimension | Measures | Key Metrics |
|---|-----------|----------|------------|
| 1 | **Affordability & Livability** | Cost of living, housing, quality of life | Rent, food costs, utilities, salary, CoL ratio |
| 2 | **Digital Infrastructure** | Internet quality, connectivity, tech jobs | Speed, 5G, penetration, broadband |
| 3 | **Startup Ecosystem** | Innovation capacity, entrepreneurship | Startup count, funding, tech jobs, growth |
| 4 | **Urban Development** | City structure, sprawl, infrastructure | Density, roads, growth rate, development |
| 5 | **Innovation Readiness** | R&D, research, patents, universities | Patents, rankings, research, citations |
| 6 | **Talent & Human Capital** | Education, developer concentration | Developers, education quality, skills |
| 7 | **Future Trajectory** | Growth momentum, potential | Historical growth, trends, forecast |

---

## 🚀 KEY FEATURES

### 📈 Advanced Clustering Analysis
```
✅ WEKA SimpleKMeans clustering
✅ Optimal K determination (Elbow method)
✅ Silhouette coefficient evaluation
✅ Interpretable cluster profiles
✅ Feature importance analysis
```

### 🗺️ Interactive Geospatial Visualization
```
✅ Folium interactive map with clusters
✅ Circle markers colored by cluster
✅ Heatmap layers
✅ Detailed city popups with metrics
✅ Pan, zoom, filter capabilities
```

### 📊 Comprehensive Analytics Dashboard
```
✅ 7-page Streamlit dashboard
✅ Real-time filtering by cluster/region
✅ Radar charts for dimension comparison
✅ Scatter plots showing relationships
✅ City ranking tables
✅ Mobile-responsive design
```

### 📑 Professional Documentation
```
✅ Methodology documentation
✅ Data sources reference
✅ Key findings & insights
✅ Code structure guide
✅ Deployment instructions
✅ Data dictionary
```

---

## 📁 PROJECT STRUCTURE

```
citymetric/
│
├── data_sources/           ← Raw datasets (6 sources)
│   ├── 01_affordability_cost_of_living/
│   ├── 02_digital_worldbank_api/
│   ├── 03_urban_world_cities/
│   ├── 04_urban_city_temperature/
│   ├── 05_innovation_university_rankings/
│   └── 06_talent_stackoverflow_survey/
│
├── data/                   ← Processed data at each stage
│   ├── raw/               ← Raw CSVs from sources
│   ├── processed/         ← Cleaned & engineered features
│   └── final/             ← Final datasets with clusters
│
├── scripts/               ← Claude Code Python artifacts
│   ├── 01_data_collection.py
│   ├── 02_data_preprocessing.py
│   ├── 03_feature_engineering.py
│   ├── 04_arff_conversion.py          ← For WEKA
│   ├── 05_weka_results_import.py      ← Results from WEKA
│   ├── 06_visualizations.py
│   └── 07_streamlit_app.py
│
├── output/                ← Generated files
│   ├── citymetric_map_interactive.html
│   ├── citymetric_charts_analysis.html
│   ├── citymetric_cluster_analysis_report.pdf
│   └── visualizations/
│
├── docs/                  ← Documentation
│   ├── README.md
│   ├── METHODOLOGY.md
│   ├── DATA_SOURCES.md
│   ├── FINDINGS.md
│   ├── CODE_STRUCTURE.md
│   ├── DEPLOYMENT.md
│   └── Data_Dictionary.txt
│
└── streamlit_app.py       ← Main dashboard application
```

---

## 🛠️ TECH STACK

### Core Technologies
```
✅ Python 3.8+            (Data processing)
✅ Pandas & NumPy         (Data manipulation)
✅ WEKA SimpleKMeans      (Clustering - MANDATORY!)
✅ Folium                 (Interactive maps)
✅ Plotly                 (Interactive charts)
✅ Streamlit              (Dashboard)
```

### Data Sources
```
✅ Kaggle Datasets        (5 datasets, pre-processed)
✅ World Bank API         (Free API, no download)
✅ Stack Overflow Survey  (Official developer data)
```

### Deployment
```
✅ GitHub                 (Code repository)
✅ Streamlit Cloud        (Free dashboard hosting)
✅ Google Colab/Claude Code (Development)
```

---

## 📊 PHASES & TIMELINE

```
PHASE 1: DATA COLLECTION (Week 1)
├─ 6 datasets from Kaggle + APIs
├─ ~410 MB total size
└─ 1-2 hours to download

PHASE 2: DATA PREPROCESSING (Week 2)
├─ Cleaning & validation
├─ Feature engineering
├─ Creating 7 composite scores (0-10)
└─ Preparing features for clustering

PHASE 3: CLUSTERING & ANALYSIS (Week 3)
├─ ✅ Step 3.0: Convert CSV → ARFF (Python)
├─ ✅ Step 3.1: Export to ARFF format (Python)
├─ ✅ Step 3.2: WEKA SimpleKMeans clustering (WEKA GUI)
├─ ✅ Step 3.3: Export WEKA results (WEKA GUI)
├─ ✅ Step 3.4: Import results back (Python)
└─ ✅ Step 3.5: Feature importance analysis (Python)

PHASE 4: VISUALIZATION (Week 3, Days 4-5)
├─ Folium interactive map
├─ Plotly analytics charts
└─ Analysis report generation

PHASE 5: DASHBOARD (Week 4, Days 1-3)
├─ Build Streamlit app (7 pages)
├─ Deploy to Streamlit Cloud
└─ Live URL ready to share

PHASE 6: DOCUMENTATION (Week 4, Days 4-7)
├─ Complete documentation
├─ Code review & optimization
└─ Final exports & deliverables

TOTAL TIME: ~150-170 hours over 4 weeks
```

---

## 🎯 QUICK START

### 1. Download Datasets
```bash
# Follow data_sources/ download guide
# Download 6 datasets (~410 MB)
# Takes ~3-4 hours
```

### 2. Run Data Processing
```bash
cd citymetric/
python scripts/01_data_collection.py
python scripts/02_data_preprocessing.py
python scripts/03_feature_engineering.py
```

### 3. Prepare for WEKA
```bash
python scripts/04_arff_conversion.py
# Creates: cities.arff file
# Use WEKA GUI to cluster this file
```

### 4. Import WEKA Results
```bash
# After running WEKA clustering
python scripts/05_weka_results_import.py
```

### 5. Create Visualizations
```bash
python scripts/06_visualizations.py
# Creates: maps, charts, reports
```

### 6. Deploy Dashboard
```bash
streamlit run streamlit_app.py
# Local: http://localhost:8501

# Deploy to Streamlit Cloud:
# git push to GitHub
# Connect repo to Streamlit Cloud
# Live URL: https://citymetric.streamlit.app
```

---

## 📊 EXPECTED OUTPUTS

### Datasets
```
✅ citymetric_index_final.csv (master dataset)
✅ cities_clustered.csv (with WEKA clusters)
✅ cluster_profiles.csv (statistical summaries)
✅ feature_analysis.csv (importance metrics)
```

### Visualizations
```
✅ Interactive Folium map (citymetric_map_interactive.html)
✅ Plotly analytics charts (citymetric_charts_analysis.html)
✅ Cluster profile radar charts
✅ Correlation heatmap
✅ Silhouette analysis plots
```

### Reports
```
✅ citymetric_cluster_analysis_report.pdf
✅ Comprehensive analysis findings
✅ City insights & recommendations
✅ Cluster interpretations
```

### Dashboard
```
✅ 7-page Streamlit app
✅ Live URL on Streamlit Cloud
✅ Interactive & mobile-responsive
✅ Shareable with public
```

---

## 💡 USE CASES

### 🏠 For Individuals
```
"Where should I move for my career?"
"Which city is most affordable for my lifestyle?"
"Where can I find the best tech job opportunities?"
```

### 💼 For Organizations
```
"Where should we open our next office?"
"Which cities have the most startup activity?"
"Where can we find top tech talent?"
```

### 🎓 For Researchers
```
"How do urban factors correlate with opportunity?"
"What defines a high-opportunity city?"
"How are cities clustering based on multiple metrics?"
```

---

## 🏆 COMPETITION & PORTFOLIO VALUE

```
🥇 PERFECT FOR:
   ✅ GEMASTIK (Data Science / Data Engineering track)
   ✅ Google Solution Challenge
   ✅ Hackathons & Competitions
   ✅ Portfolio projects for job applications
   ✅ Internship/scholarship applications
   ✅ Open-source contributions

⭐ WHY IT STANDS OUT:
   ✅ Complete end-to-end data engineering pipeline
   ✅ Uses WEKA for data mining (required tool)
   ✅ Professional geospatial visualizations
   ✅ Deployed live dashboard
   ✅ Global scope & relevant topic
   ✅ Well-documented & reproducible
   ✅ Impressive analytics insights
```

---

## 📥 DATA SOURCES SUMMARY

| # | Dataset | Source | Size | Status |
|---|---------|--------|------|--------|
| 1 | Cost of Living | Kaggle | 50 MB | ✅ Available |
| 2 | World Cities | Kaggle | 50 MB | ✅ Available |
| 3 | City Temperature | Kaggle | 100 MB | ✅ Available |
| 4 | University Rankings | Kaggle | 10 MB | ✅ Available |
| 5 | Stack Overflow Survey | Stack Overflow | 100 MB | ✅ Available |
| 6 | Digital Indicators | World Bank API | - | ✅ Free API |
| **TOTAL** | | | **~410 MB** | **✅ READY** |

---

## 🎨 BRANDING & AESTHETICS

```
Project Name: CityMetric
Tagline: "Measure Your City, Measure Your Future"

Color Scheme (Y2K/Modern):
├─ Primary: #FF69B4 (Hot Pink)
├─ Secondary: #9D4EDD (Purple)
├─ Accent: #3A86FF (Blue)
└─ Neutral: #E0E0E0 (Light Gray)

Cluster Colors (Folium Map):
├─ Cluster 0: #FFB6D9 (Pink)
├─ Cluster 1: #C8A2E8 (Purple)
├─ Cluster 2: #B4D7FF (Light Blue)
├─ Cluster 3: #FFE8B6 (Peach)
└─ Cluster 4: #B4FFD7 (Mint)

Typography: Modern, clean, professional
Logo Style: Minimalist, data-driven
```

---

## 📚 DOCUMENTATION

See individual files:
- **README.md** (this file - project overview)
- **METHODOLOGY.md** (technical approach & formulas)
- **DATA_SOURCES.md** (detailed source documentation)
- **FINDINGS.md** (key insights & analysis)
- **CODE_STRUCTURE.md** (developer guide)
- **DEPLOYMENT.md** (how to deploy)
- **Data_Dictionary.txt** (column definitions)

---

## 👨‍💻 DEVELOPER INFO

```
Developer: [Your Name]
Institution: Universitas Islam Indonesia
Dual Degree Program: Nanjing Xiaozhuang University
Created: 2026
Last Updated: 2026-06-01
```

---

## 📞 SUPPORT & RESOURCES

```
DOCUMENTATION:
├─ Data sources guide: /docs/DATA_SOURCES.md
├─ Methodology: /docs/METHODOLOGY.md
└─ Deployment: /docs/DEPLOYMENT.md

EXTERNAL RESOURCES:
├─ Kaggle: https://www.kaggle.com/
├─ World Bank API: https://data.worldbank.org/
├─ WEKA: https://www.cs.waikato.ac.nz/ml/weka/
├─ Streamlit: https://streamlit.io/
├─ Folium: https://folium.readthedocs.io/
└─ Plotly: https://plotly.com/python/
```

---

## 🚀 READY TO START?

1. **Download data_sources folder structure**
2. **Follow data download guide**
3. **Run Phase 1 scripts**
4. **Proceed through Phase 2-6**
5. **Deploy live dashboard**
6. **Share with world!**

---

**Let's build CityMetric! 🌍📊**

```
┌─────────────────────────────────────┐
│  CityMetric - Data-Driven City      │
│  Intelligence Platform              │
│                                     │
│  Measure Your City,                 │
│  Measure Your Future                │
│                                     │
│  github.com/[username]/citymetric   │
│  https://citymetric.streamlit.app   │
└─────────────────────────────────────┘
```