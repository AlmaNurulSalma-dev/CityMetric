# 📁 CITYMETRIC - DATA SOURCES (AVAILABLE ONLY)

## Simplified Folder Structure - Only Available Datasets

```
data_sources/
│
├── 1_affordability_livability/
│   ├── 01_cost_of_living_numbeo/
│   │   ├── metadata.txt
│   │   └── cost_of_living.csv ✅
│   │
│   └── 02_economic_worldbank/
│       ├── metadata.txt
│       ├── gdp_per_capita.csv
│       ├── gini_coefficient.csv
│       ├── healthcare_spending.csv
│       └── education_spending.csv
│
├── 2_digital_infrastructure/
│   └── 01_digital_worldbank/
│       ├── metadata.txt
│       ├── internet_users_pct.csv
│       ├── broadband_subscriptions.csv
│       ├── mobile_subscriptions.csv
│       └── internet_servers.csv
│
├── 3_startup_ecosystem/
│   └── (Will use proxy data or skip for now)
│
├── 4_urban_development/
│   ├── 01_world_cities_kaggle/
│   │   ├── metadata.txt
│   │   └── worldcities.csv ✅
│   │
│   ├── 02_city_temperature_kaggle/
│   │   ├── metadata.txt
│   │   └── city_temperature.csv ✅
│   │
│   └── 03_urban_worldbank/
│       ├── metadata.txt
│       ├── urban_population_pct.csv
│       ├── population_growth_rate.csv
│       └── land_area.csv
│
├── 5_innovation_readiness/
│   ├── 01_university_rankings_kaggle/
│   │   ├── metadata.txt
│   │   └── university_rankings.csv ✅
│   │
│   └── 02_innovation_worldbank/
│       ├── metadata.txt
│       ├── research_and_development_pct.csv
│       ├── scientific_publications.csv
│       └── high_tech_exports.csv
│
├── 6_talent_human_capital/
│   ├── 01_stackoverflow_survey_official/
│   │   ├── metadata.txt
│   │   └── survey_results_public.csv ✅
│   │
│   └── 02_talent_worldbank/
│       ├── metadata.txt
│       ├── tertiary_education_pct.csv
│       ├── literacy_rate.csv
│       ├── education_spending_pct.csv
│       └── school_enrollment.csv
│
└── 7_future_trajectory/
    └── (Use historical data from dimensions 1-6)
```

---

## 📥 FILES TO DOWNLOAD

### Kaggle Datasets (5 files, ~310 MB):

```
1. Cost of Living
   Path: data_sources/1_affordability_livability/01_cost_of_living_numbeo/
   File: cost_of_living.csv (50 MB)
   Link: https://www.kaggle.com/datasets/mvieira101/global-cost-of-living

2. World Cities
   Path: data_sources/4_urban_development/01_world_cities_kaggle/
   File: worldcities.csv (50 MB)
   Link: https://www.kaggle.com/datasets/max-mind/world-cities-database

3. City Temperature
   Path: data_sources/4_urban_development/02_city_temperature_kaggle/
   File: city_temperature.csv (100 MB)
   Link: https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities

4. University Rankings
   Path: data_sources/5_innovation_readiness/01_university_rankings_kaggle/
   File: university_rankings.csv (10 MB)
   Link: https://www.kaggle.com/datasets/mylesoneill/world-university-rankings

5. Stack Overflow Survey
   Path: data_sources/6_talent_human_capital/01_stackoverflow_survey_official/
   File: survey_results_public.csv (100 MB)
   Link: https://insights.stackoverflow.com/survey
```

### World Bank API (via Python, No Download):

```
1. data_sources/1_affordability_livability/02_economic_worldbank/
2. data_sources/2_digital_infrastructure/01_digital_worldbank/
3. data_sources/4_urban_development/03_urban_worldbank/
4. data_sources/5_innovation_readiness/02_innovation_worldbank/
5. data_sources/6_talent_human_capital/02_talent_worldbank/
```

---

## 🚀 CREATE FOLDER STRUCTURE (BASH)

```bash
#!/bin/bash

echo "Creating CityMetric data_sources folder structure (AVAILABLE ONLY)..."

# Base
mkdir -p data_sources

# Dimension 1: Affordability & Livability
mkdir -p data_sources/1_affordability_livability/{01_cost_of_living_numbeo,02_economic_worldbank}

# Dimension 2: Digital Infrastructure
mkdir -p data_sources/2_digital_infrastructure/01_digital_worldbank

# Dimension 3: Startup Ecosystem
mkdir -p data_sources/3_startup_ecosystem

# Dimension 4: Urban Development
mkdir -p data_sources/4_urban_development/{01_world_cities_kaggle,02_city_temperature_kaggle,03_urban_worldbank}

# Dimension 5: Innovation Readiness
mkdir -p data_sources/5_innovation_readiness/{01_university_rankings_kaggle,02_innovation_worldbank}

# Dimension 6: Talent & Human Capital
mkdir -p data_sources/6_talent_human_capital/{01_stackoverflow_survey_official,02_talent_worldbank}

# Dimension 7: Future Trajectory
mkdir -p data_sources/7_future_trajectory

# Create metadata.txt in each folder
find data_sources -type d ! -empty -exec touch {}/metadata.txt \;

echo "✅ Folder structure created!"
```

---

## 🐍 CREATE FOLDER STRUCTURE (PYTHON)

```python
import os
from pathlib import Path

# Only available data sources
structure = {
    '1_affordability_livability': [
        '01_cost_of_living_numbeo',
        '02_economic_worldbank'
    ],
    '2_digital_infrastructure': [
        '01_digital_worldbank'
    ],
    '3_startup_ecosystem': [],  # Empty for now
    '4_urban_development': [
        '01_world_cities_kaggle',
        '02_city_temperature_kaggle',
        '03_urban_worldbank'
    ],
    '5_innovation_readiness': [
        '01_university_rankings_kaggle',
        '02_innovation_worldbank'
    ],
    '6_talent_human_capital': [
        '01_stackoverflow_survey_official',
        '02_talent_worldbank'
    ],
    '7_future_trajectory': []  # Will use historical data
}

base_path = Path('data_sources')
base_path.mkdir(exist_ok=True)

for dimension, sources in structure.items():
    dim_path = base_path / dimension
    dim_path.mkdir(exist_ok=True)
    
    for source in sources:
        source_path = dim_path / source
        source_path.mkdir(parents=True, exist_ok=True)
        
        # Create metadata.txt
        metadata_file = source_path / 'metadata.txt'
        if not metadata_file.exists():
            with open(metadata_file, 'w') as f:
                f.write(f"Data Source: {source}\n")
                f.write(f"Dimension: {dimension}\n\n")
                f.write(f"Files to place here:\n")
                f.write(f"- CSV file(s) from source\n")

print("✅ CityMetric data_sources folder structure created!")
print("\nReady to download datasets!")
```

---

## 📋 DOWNLOAD CHECKLIST

```
✅ PRIORITY 1 (Download Today):
   □ cost_of_living.csv → 1_affordability_livability/01_cost_of_living_numbeo/
   □ worldcities.csv → 4_urban_development/01_world_cities_kaggle/
   □ university_rankings.csv → 5_innovation_readiness/01_university_rankings_kaggle/

✅ PRIORITY 2 (Download Tomorrow):
   □ city_temperature.csv → 4_urban_development/02_city_temperature_kaggle/
   □ survey_results_public.csv → 6_talent_human_capital/01_stackoverflow_survey_official/

✅ SPECIAL (Extract via Python API):
   □ World Bank economic data → 1_affordability_livability/02_economic_worldbank/
   □ World Bank digital data → 2_digital_infrastructure/01_digital_worldbank/
   □ World Bank urban data → 4_urban_development/03_urban_worldbank/
   □ World Bank innovation data → 5_innovation_readiness/02_innovation_worldbank/
   □ World Bank talent data → 6_talent_human_capital/02_talent_worldbank/
```

---

## 📊 SUMMARY

```
TOTAL AVAILABLE DATASETS: 5 Kaggle + World Bank API

SIZE: ~310 MB (Kaggle) + API data
TIME: 2-3 hours to download

DIMENSIONS COVERED:
✅ 1. Affordability & Livability (2 sources)
✅ 2. Digital Infrastructure (1 source)
❌ 3. Startup Ecosystem (0 sources - will need alternative)
✅ 4. Urban Development (3 sources)
✅ 5. Innovation Readiness (2 sources)
✅ 6. Talent & Human Capital (2 sources)
⚠️  7. Future Trajectory (use historical data from 1-6)

STATUS: Ready to download and process!
```

---

## 🎯 NEXT STEPS

1. Create folder structure using bash/python script
2. Download 5 Kaggle CSVs
3. Extract World Bank data via Python
4. Move files to corresponding folders
5. Verify all files in place
6. Start Phase 1-2 data processing

Done! Clean, simple, practical! 🚀