# CityMetric — Deployment Guide

## Local Development

### Requirements
- Python 3.10+
- pip

### Setup

```bash
git clone https://github.com/AlmaNurulSalma-dev/citymetric
cd citymetric
pip install -r requirements.txt
```

### Run dashboard

```bash
python -m streamlit run streamlit_app.py
```

Open `http://localhost:8501`.

### Reproduce full pipeline

Run scripts in order:

```bash
python scripts/01_data_collection.py     # ~2 min (World Bank API)
python scripts/02_data_preprocessing.py  # ~5 sec
python scripts/03_clustering.py          # ~10 sec
python scripts/04_visualization.py       # ~15 sec
python -m streamlit run streamlit_app.py
```

---

## Streamlit Cloud Deployment

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "CityMetric ready for deployment"
   git push origin main
   ```

2. **Go to** [share.streamlit.io](https://share.streamlit.io)

3. **New app** → Connect your GitHub repo → Select:
   - Repository: `AlmaNurulSalma-dev/citymetric`
   - Branch: `main`
   - Main file: `streamlit_app.py`

4. **Deploy** → Live at `https://citymetric.streamlit.app`

### Important for Streamlit Cloud
- `data/processed/cities_clustered.csv` **must be committed** to the repo
  (the dashboard reads from this file)
- Large raw data files (`data_sources/`) should be in `.gitignore`
- `requirements.txt` must be present

---

## .gitignore recommendation

```gitignore
# Large raw data (re-run pipeline to regenerate)
data_sources/4_urban_development/01_world_cities_kaggle/data.csv
data_sources/4_urban_development/02_city_temperature_kaggle/
data_sources/6_talent_human_capital/01_stackoverflow_survey_official/

# Python
__pycache__/
*.pyc
.env

# Helper scripts
scripts/_screenshot.py
```

Commit everything else including:
- `data/processed/` — processed CSVs that the dashboard reads
- `data/raw/` — smaller raw files
- `output/` — generated charts
- `weka/` — ARFF and WEKA results

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| Map not showing on Streamlit Cloud | Ensure `streamlit-folium` in requirements.txt |
| World Bank API slow | Uses targeted ISO2 list — should be <30 sec |
| `cities_clustered.csv` not found | Run `scripts/02` and `scripts/03` first |
| Streamlit port already in use | `streamlit run streamlit_app.py --server.port 8502` |
