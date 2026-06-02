# 🌍 CityMetric — Global City Opportunity & Innovation Index

> **Measure Your City, Measure Your Future**

A data-driven platform analyzing **55 global cities** across **6 key dimensions** using data mining, geospatial visualization, and an interactive dashboard.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://citymetric.streamlit.app)

---

## 🎯 What is CityMetric?

CityMetric answers: **"Where should you build, invest, or move?"**

It collects data from 8+ global sources, engineers composite scores for each city across 6 dimensions, clusters cities into 5 archetypes using K-Means (WEKA + scikit-learn), and presents everything through an interactive Streamlit dashboard.

---

## 📊 The 6 Dimensions

| # | Dimension | What it measures | Key data source |
|---|-----------|-----------------|-----------------|
| 1 | 💰 **Affordability** | Rent, salary, cost-of-living ratio | Numbeo |
| 2 | 📡 **Digital** | Internet %, broadband, mobile penetration | World Bank API |
| 3 | 🏙️ **Urban** | Population, climate comfort, city growth | MaxMind + NOAA |
| 4 | 💡 **Innovation** | R&D spending, research output, university quality | World Bank + CWUR/Times/Shanghai |
| 5 | 👩‍💻 **Talent** | Education enrollment, developer density, seniority | World Bank + Stack Overflow |
| 6 | 📈 **Growth** | GDP, population trend, high-tech exports | World Bank API |

---

## 🏆 Top 10 Cities (Opportunity Index)

| Rank | City | Score | Cluster |
|------|------|-------|---------|
| 1 | Los Angeles | 6.20 | Established Hubs |
| 2 | New York | 6.01 | Established Hubs |
| 3 | San Francisco | 5.93 | Established Hubs |
| 4 | Chicago | 5.86 | Established Hubs |
| 5 | Hong Kong | 5.82 | Digital Leaders |
| 6 | Melbourne | 5.74 | Digital Leaders |
| 7 | Singapore | 5.59 | Digital Leaders |
| 8 | Sydney | 5.55 | Digital Leaders |
| 9 | Tel Aviv | 5.50 | Established Hubs |
| 10 | Istanbul | 5.49 | Established Hubs |

---

## 🗂️ Project Structure

```
citymetric/
├── streamlit_app.py          # Main dashboard (7 pages)
├── requirements.txt
├── data_sources/             # Raw downloaded datasets
│   ├── 1_affordability_livability/
│   ├── 2_digital_infrastructure/
│   ├── 3_startup_ecosystem/
│   ├── 4_urban_development/
│   ├── 5_innovation_readiness/
│   ├── 6_talent_human_capital/
│   └── 7_future_trajectory/
├── data/
│   ├── raw/                  # Cleaned per-source CSVs
│   ├── processed/            # Feature-engineered + clustered
│   └── final/                # Export-ready datasets
├── scripts/
│   ├── 01_data_collection.py
│   ├── 02_data_preprocessing.py
│   ├── 03_clustering.py      # ARFF conversion + K-Means
│   └── 04_visualization.py
├── weka/
│   ├── cities.arff           # WEKA input file
│   ├── weka_cluster_assignments.txt
│   ├── weka_cluster_centroids.txt
│   └── weka_evaluation_metrics.txt
├── output/                   # Charts, maps, PNGs
└── docs/                     # Documentation
```

---

## 🚀 Quick Start

### Run locally

```bash
git clone https://github.com/AlmaNurulSalma-dev/citymetric
cd citymetric
pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Open `http://localhost:8501` in your browser.

### Reproduce the full pipeline

```bash
python scripts/01_data_collection.py    # fetch & organise data
python scripts/02_data_preprocessing.py # clean + feature engineering
python scripts/03_clustering.py         # ARFF + K-Means clustering
python scripts/04_visualization.py      # generate all charts
python -m streamlit run streamlit_app.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| pandas / numpy | Data manipulation |
| scikit-learn | K-Means clustering |
| **WEKA** | Official data mining (SimpleKMeans) |
| Folium | Interactive geospatial map |
| Plotly | Interactive charts |
| Streamlit | Web dashboard |
| World Bank API (wbdata) | Economic & social indicators |

---

## 📁 Key Output Files

| File | Description |
|------|-------------|
| `data/processed/cities_features.csv` | 55 cities × 7 scores |
| `data/processed/cities_clustered.csv` | + cluster assignments |
| `weka/cities.arff` | WEKA-ready input |
| `output/citymetric_map_interactive.html` | Folium world map |
| `output/citymetric_summary_poster.png` | One-page visual summary |

---

## 👤 Author

**Alma Nurul Salma**
Informatics — Universitas Islam Indonesia & Nanjing Xiaozhuang University
📧 almanurulsalma@gmail.com · 🔗 [github.com/AlmaNurulSalma-dev](https://github.com/AlmaNurulSalma-dev)
