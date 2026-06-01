# 📁 CITYMETRIC - DATA SOURCES FOLDER STRUCTURE

## Complete Folder Organization by Dimension

```
data_sources/
│
├── 1_affordability_livability/
│   ├── 01_cost_of_living_numbeo/
│   │   ├── metadata.txt
│   │   └── cost_of_living.csv ✅ AVAILABLE
│   │
│   ├── 02_salary_glassdoor/
│   │   ├── metadata.txt
│   │   └── glassdoor_salary.csv ❌ NOT AVAILABLE
│   │
│   ├── 03_salary_indeed/
│   │   ├── metadata.txt
│   │   └── indeed_salaries.csv ❌ NOT AVAILABLE
│   │
│   └── 04_economic_worldbank/
│       ├── metadata.txt
│       └── [Via API - No download]
│           ├── gdp_per_capita.csv
│           ├── gini_coefficient.csv
│           ├── healthcare_spending.csv
│           └── education_spending.csv
│
├── 2_digital_infrastructure/
│   ├── 01_internet_speed_speedtest/
│   │   ├── metadata.txt
│   │   └── internet_speed.csv ❌ NOT AVAILABLE
│   │
│   ├── 02_internet_users_worldstats/
│   │   ├── metadata.txt
│   │   └── internet_users.csv ❌ NOT AVAILABLE
│   │
│   ├── 03_tech_jobs_indeed/
│   │   ├── metadata.txt
│   │   └── tech_jobs_indeed.csv ❌ NOT AVAILABLE
│   │
│   ├── 04_tech_jobs_stackoverflow/
│   │   ├── metadata.txt
│   │   └── tech_jobs_stackoverflow.csv ❌ NOT AVAILABLE
│   │
│   └── 05_digital_worldbank/
│       ├── metadata.txt
│       └── [Via API - No download]
│           ├── internet_users_pct.csv
│           ├── broadband_subscriptions.csv
│           ├── mobile_subscriptions.csv
│           └── internet_servers.csv
│
├── 3_startup_ecosystem/
│   ├── 01_crunchbase_kaggle/
│   │   ├── metadata.txt
│   │   └── crunchbase_companies.csv ❌ NOT AVAILABLE
│   │
│   ├── 02_angellist_api/
│   │   ├── metadata.txt
│   │   └── [Via AngelList API - Optional]
│   │       └── angellist_startups.csv
│   │
│   ├── 03_github_api/
│   │   ├── metadata.txt
│   │   └── [Via GitHub API - Optional]
│   │       └── github_companies.csv
│   │
│   └── 04_cb_insights/
│       ├── metadata.txt
│       └── cb_insights_reports.csv ❌ NOT AVAILABLE
│
├── 4_urban_development/
│   ├── 01_world_cities_kaggle/
│   │   ├── metadata.txt
│   │   └── worldcities.csv ✅ AVAILABLE
│   │
│   ├── 02_city_temperature_kaggle/
│   │   ├── metadata.txt
│   │   └── city_temperature.csv ✅ AVAILABLE
│   │
│   ├── 03_openstreetmap_osmnx/
│   │   ├── metadata.txt
│   │   └── [Via osmnx Python library]
│   │       └── osm_urban_metrics.csv ❌ NOT AVAILABLE
│   │
│   ├── 04_worldpop_density/
│   │   ├── metadata.txt
│   │   └── [Via WorldPop - Download]
│   │       └── population_density.csv ❌ NOT AVAILABLE
│   │
│   └── 05_urban_worldbank/
│       ├── metadata.txt
│       └── [Via API - No download]
│           ├── urban_population_pct.csv
│           ├── population_growth_rate.csv
│           └── land_area.csv
│
├── 5_innovation_readiness/
│   ├── 01_patents_google_kaggle/
│   │   ├── metadata.txt
│   │   └── patents.csv ❌ NOT AVAILABLE
│   │
│   ├── 02_patents_wipo/
│   │   ├── metadata.txt
│   │   └── [Via WIPO - Manual download]
│   │       └── wipo_patents.csv ❌ NOT AVAILABLE
│   │
│   ├── 03_university_rankings_kaggle/
│   │   ├── metadata.txt
│   │   └── university_rankings.csv ✅ AVAILABLE
│   │
│   ├── 04_university_rankings_qs/
│   │   ├── metadata.txt
│   │   └── [Web scraping - Not recommended]
│   │       └── qs_rankings.csv ❌ NOT AVAILABLE
│   │
│   ├── 05_research_papers_arxiv/
│   │   ├── metadata.txt
│   │   └── [Via ArXiv Kaggle - Optional, Large]
│   │       └── arxiv_papers.csv ❌ NOT AVAILABLE (3GB)
│   │
│   ├── 06_scimago_research/
│   │   ├── metadata.txt
│   │   └── [Download CSV from website]
│   │       └── scimago_institutions.csv ❌ NOT AVAILABLE
│   │
│   └── 07_innovation_worldbank/
│       ├── metadata.txt
│       └── [Via API - No download]
│           ├── research_and_development_pct.csv
│           ├── scientific_publications.csv
│           └── high_tech_exports.csv
│
├── 6_talent_human_capital/
│   ├── 01_stackoverflow_survey_official/
│   │   ├── metadata.txt
│   │   └── survey_results_public.csv ✅ AVAILABLE
│   │
│   ├── 02_developer_salaries_kaggle/
│   │   ├── metadata.txt
│   │   └── developer_salaries.csv ❌ NOT AVAILABLE
│   │
│   ├── 03_linkedin_data/
│   │   ├── metadata.txt
│   │   └── [Via LinkedIn API - Limited]
│   │       └── linkedin_professionals.csv ❌ NOT AVAILABLE
│   │
│   ├── 04_immigration_government/
│   │   ├── metadata.txt
│   │   └── [Manual research - Government sites]
│   │       ├── h1b_visa_approvals.csv ❌ NOT AVAILABLE
│   │       ├── canada_immigration.csv ❌ NOT AVAILABLE
│   │       └── skilled_visa_grants.csv ❌ NOT AVAILABLE
│   │
│   └── 05_talent_worldbank/
│       ├── metadata.txt
│       └── [Via API - No download]
│           ├── tertiary_education_pct.csv
│           ├── literacy_rate.csv
│           ├── education_spending_pct.csv
│           └── school_enrollment.csv
│
└── 7_future_trajectory/
    └── [Use historical data from Dimensions 1-6]
        ├── historical_startup_data/
        │   └── (From 3_startup_ecosystem/01_crunchbase - historical filtering)
        │
        ├── historical_internet_speed/
        │   └── (From 2_digital_infrastructure/01_internet_speed - year-by-year)
        │
        ├── historical_economic_data/
        │   └── (From World Bank APIs - annual data 1990-2023)
        │
        └── historical_patent_data/
            └── (From 5_innovation_readiness/01_patents - filing dates)
```

---

## 📊 SUMMARY TABLE

### Data Sources by Dimension

| # | Dimension | Data Source | CSV Name | Status | Kaggle Link |
|---|-----------|-------------|----------|--------|-------------|
| **1** | **Affordability** | Cost of Living (Numbeo) | cost_of_living.csv | ✅ | https://www.kaggle.com/datasets/mvieira101/global-cost-of-living |
| | | Glassdoor Salary | glassdoor_salary.csv | ❌ | https://www.kaggle.com/datasets/zinovyev/glassdoor-salary |
| | | Indeed Jobs | indeed_jobs.csv | ❌ | (Not found) |
| | | World Bank Economic | gdp_per_capita.csv | ✅ API | https://data.worldbank.org/ |
| **2** | **Digital** | Speedtest Internet | internet_speed.csv | ❌ | https://www.kaggle.com/datasets/taruntiwarihp/internet-speed-by-country |
| | | Internet Users % | internet_users.csv | ❌ | https://www.kaggle.com/datasets/aliashraf/global-internet-users |
| | | Indeed Tech Jobs | tech_jobs_indeed.csv | ❌ | https://www.kaggle.com/datasets/PromptCloudHQ/tech-jobs-on-dice |
| | | Stack Overflow Jobs | tech_jobs_stackoverflow.csv | ❌ | (Not found) |
| | | World Bank Digital | internet_users_pct.csv | ✅ API | https://data.worldbank.org/ |
| **3** | **Startup** | Crunchbase | crunchbase_companies.csv | ❌ | https://www.kaggle.com/datasets/mgmarques/crunchbase-companies |
| | | AngelList | angellist_startups.csv | ❌ | (API limited) |
| | | GitHub | github_companies.csv | ❌ | (API only) |
| | | CB Insights | cb_insights_reports.csv | ❌ | (Reports only) |
| **4** | **Urban** | World Cities | worldcities.csv | ✅ | https://www.kaggle.com/datasets/max-mind/world-cities-database |
| | | City Temperature | city_temperature.csv | ✅ | https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities |
| | | OpenStreetMap | osm_urban_metrics.csv | ❌ | (osmnx library only) |
| | | WorldPop | population_density.csv | ❌ | (Download site) |
| | | World Bank Urban | urban_population_pct.csv | ✅ API | https://data.worldbank.org/ |
| **5** | **Innovation** | Google Patents | patents.csv | ❌ | https://www.kaggle.com/datasets/trainingdatasus/patent-data |
| | | WIPO Patents | wipo_patents.csv | ❌ | (WIPO site) |
| | | University Rankings | university_rankings.csv | ✅ | https://www.kaggle.com/datasets/mylesoneill/world-university-rankings |
| | | QS Rankings | qs_rankings.csv | ❌ | (Web scrape) |
| | | ArXiv Papers | arxiv_papers.csv | ❌ | https://www.kaggle.com/datasets/Cornell-University/arxiv (3GB!) |
| | | SCIMAGO | scimago_institutions.csv | ❌ | (Download from website) |
| | | World Bank Innovation | research_and_development_pct.csv | ✅ API | https://data.worldbank.org/ |
| **6** | **Talent** | Stack Overflow Survey | survey_results_public.csv | ✅ | https://insights.stackoverflow.com/survey |
| | | Dev Salaries | developer_salaries.csv | ❌ | https://www.kaggle.com/datasets/harshsingh2209/developer-salaries-in-2024 |
| | | LinkedIn | linkedin_professionals.csv | ❌ | (API limited) |
| | | Government Visas | h1b_visa_approvals.csv | ❌ | (Government sites) |
| | | World Bank Education | tertiary_education_pct.csv | ✅ API | https://data.worldbank.org/ |
| **7** | **Growth** | (Historical from above) | (Various) | ✅ | (Use time-series from 1-6) |

---

## ✅ AVAILABLE vs ❌ NOT AVAILABLE

### ✅ AVAILABLE (Download/Use These):

```
✅ 1_affordability_livability/
   └─ 01_cost_of_living_numbeo/cost_of_living.csv

✅ 2_digital_infrastructure/
   └─ 05_digital_worldbank/[API data]

✅ 4_urban_development/
   ├─ 01_world_cities_kaggle/worldcities.csv
   ├─ 02_city_temperature_kaggle/city_temperature.csv
   └─ 05_urban_worldbank/[API data]

✅ 5_innovation_readiness/
   ├─ 03_university_rankings_kaggle/university_rankings.csv
   └─ 07_innovation_worldbank/[API data]

✅ 6_talent_human_capital/
   ├─ 01_stackoverflow_survey_official/survey_results_public.csv
   └─ 05_talent_worldbank/[API data]
```

### ❌ NOT AVAILABLE (Skip These):

```
❌ 1_affordability_livability/
   ├─ 02_salary_glassdoor/ (Kaggle page down)
   └─ 03_salary_indeed/ (Not found)

❌ 2_digital_infrastructure/
   ├─ 01_internet_speed_speedtest/ (Kaggle page down)
   ├─ 02_internet_users_worldstats/ (Kaggle page down)
   ├─ 03_tech_jobs_indeed/ (Kaggle page down)
   └─ 04_tech_jobs_stackoverflow/ (Not found)

❌ 3_startup_ecosystem/
   ├─ 01_crunchbase_kaggle/ (Kaggle page down)
   ├─ 02_angellist_api/ (API limited)
   ├─ 03_github_api/ (API only)
   └─ 04_cb_insights/ (Reports only)

❌ 4_urban_development/
   ├─ 03_openstreetmap_osmnx/ (Library only, not CSV)
   └─ 04_worldpop_density/ (Download site limited)

❌ 5_innovation_readiness/
   ├─ 01_patents_google_kaggle/ (Kaggle page down)
   ├─ 02_patents_wipo/ (Not easily accessible)
   ├─ 04_university_rankings_qs/ (Web scrape needed)
   ├─ 05_research_papers_arxiv/ (3GB - Optional)
   └─ 06_scimago_research/ (Manual download)

❌ 6_talent_human_capital/
   ├─ 02_developer_salaries_kaggle/ (Kaggle page down)
   ├─ 03_linkedin_data/ (API limited)
   └─ 04_immigration_government/ (Manual research)
```

---

## 📥 HOW TO CREATE FOLDER STRUCTURE

### Option 1: Using Terminal/Command Line

```bash
# Main data_sources folder
mkdir -p data_sources

# Dimension 1: Affordability & Livability
mkdir -p data_sources/1_affordability_livability/{01_cost_of_living_numbeo,02_salary_glassdoor,03_salary_indeed,04_economic_worldbank}

# Dimension 2: Digital Infrastructure
mkdir -p data_sources/2_digital_infrastructure/{01_internet_speed_speedtest,02_internet_users_worldstats,03_tech_jobs_indeed,04_tech_jobs_stackoverflow,05_digital_worldbank}

# Dimension 3: Startup Ecosystem
mkdir -p data_sources/3_startup_ecosystem/{01_crunchbase_kaggle,02_angellist_api,03_github_api,04_cb_insights}

# Dimension 4: Urban Development
mkdir -p data_sources/4_urban_development/{01_world_cities_kaggle,02_city_temperature_kaggle,03_openstreetmap_osmnx,04_worldpop_density,05_urban_worldbank}

# Dimension 5: Innovation Readiness
mkdir -p data_sources/5_innovation_readiness/{01_patents_google_kaggle,02_patents_wipo,03_university_rankings_kaggle,04_university_rankings_qs,05_research_papers_arxiv,06_scimago_research,07_innovation_worldbank}

# Dimension 6: Talent & Human Capital
mkdir -p data_sources/6_talent_human_capital/{01_stackoverflow_survey_official,02_developer_salaries_kaggle,03_linkedin_data,04_immigration_government,05_talent_worldbank}

# Dimension 7: Future Trajectory
mkdir -p data_sources/7_future_trajectory/{historical_startup_data,historical_internet_speed,historical_economic_data,historical_patent_data}

# Create metadata.txt in each folder
find data_sources -type d -name "*_*" -exec touch {}/metadata.txt \;
```

### Option 2: Using Python Script

```python
import os
from pathlib import Path

# Define complete structure
structure = {
    '1_affordability_livability': [
        '01_cost_of_living_numbeo',
        '02_salary_glassdoor',
        '03_salary_indeed',
        '04_economic_worldbank'
    ],
    '2_digital_infrastructure': [
        '01_internet_speed_speedtest',
        '02_internet_users_worldstats',
        '03_tech_jobs_indeed',
        '04_tech_jobs_stackoverflow',
        '05_digital_worldbank'
    ],
    '3_startup_ecosystem': [
        '01_crunchbase_kaggle',
        '02_angellist_api',
        '03_github_api',
        '04_cb_insights'
    ],
    '4_urban_development': [
        '01_world_cities_kaggle',
        '02_city_temperature_kaggle',
        '03_openstreetmap_osmnx',
        '04_worldpop_density',
        '05_urban_worldbank'
    ],
    '5_innovation_readiness': [
        '01_patents_google_kaggle',
        '02_patents_wipo',
        '03_university_rankings_kaggle',
        '04_university_rankings_qs',
        '05_research_papers_arxiv',
        '06_scimago_research',
        '07_innovation_worldbank'
    ],
    '6_talent_human_capital': [
        '01_stackoverflow_survey_official',
        '02_developer_salaries_kaggle',
        '03_linkedin_data',
        '04_immigration_government',
        '05_talent_worldbank'
    ],
    '7_future_trajectory': [
        'historical_startup_data',
        'historical_internet_speed',
        'historical_economic_data',
        'historical_patent_data'
    ]
}

# Create folders
base_path = Path('data_sources')
base_path.mkdir(exist_ok=True)

for dimension, sources in structure.items():
    for source in sources:
        folder_path = base_path / dimension / source
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Create metadata.txt
        metadata_file = folder_path / 'metadata.txt'
        if not metadata_file.exists():
            with open(metadata_file, 'w') as f:
                f.write(f"Dimension: {dimension}\n")
                f.write(f"Data Source: {source}\n")
                f.write(f"Created: {datetime.now()}\n")
                f.write(f"\nFiles in this folder:\n")
                f.write(f"- metadata.txt (this file)\n")
                f.write(f"- [CSV files to be added here]\n")

print("✅ Complete data_sources folder structure created!")
```

---

## 📋 FOLDER STRUCTURE CHECKLIST

Use this to verify your folder structure is correct:

```
DIMENSION 1: Affordability & Livability
├─ 01_cost_of_living_numbeo/
│  ├─ metadata.txt ✅
│  └─ cost_of_living.csv (TO DOWNLOAD)
├─ 02_salary_glassdoor/
│  ├─ metadata.txt ✅
│  └─ glassdoor_salary.csv (NOT AVAILABLE)
├─ 03_salary_indeed/
│  ├─ metadata.txt ✅
│  └─ indeed_jobs.csv (NOT AVAILABLE)
└─ 04_economic_worldbank/
   ├─ metadata.txt ✅
   └─ (API data - no CSV)

DIMENSION 2: Digital Infrastructure
├─ 01_internet_speed_speedtest/
├─ 02_internet_users_worldstats/
├─ 03_tech_jobs_indeed/
├─ 04_tech_jobs_stackoverflow/
└─ 05_digital_worldbank/ ✅
   └─ (API data)

DIMENSION 3: Startup Ecosystem
├─ 01_crunchbase_kaggle/ (NOT AVAILABLE)
├─ 02_angellist_api/ (NOT AVAILABLE)
├─ 03_github_api/ (NOT AVAILABLE)
└─ 04_cb_insights/ (NOT AVAILABLE)

DIMENSION 4: Urban Development
├─ 01_world_cities_kaggle/ ✅
│  └─ worldcities.csv (TO DOWNLOAD)
├─ 02_city_temperature_kaggle/ ✅
│  └─ city_temperature.csv (TO DOWNLOAD)
├─ 03_openstreetmap_osmnx/ (NOT AVAILABLE)
├─ 04_worldpop_density/ (NOT AVAILABLE)
└─ 05_urban_worldbank/ ✅
   └─ (API data)

DIMENSION 5: Innovation Readiness
├─ 01_patents_google_kaggle/ (NOT AVAILABLE)
├─ 02_patents_wipo/ (NOT AVAILABLE)
├─ 03_university_rankings_kaggle/ ✅
│  └─ university_rankings.csv (TO DOWNLOAD)
├─ 04_university_rankings_qs/ (NOT AVAILABLE)
├─ 05_research_papers_arxiv/ (NOT AVAILABLE)
├─ 06_scimago_research/ (NOT AVAILABLE)
└─ 07_innovation_worldbank/ ✅
   └─ (API data)

DIMENSION 6: Talent & Human Capital
├─ 01_stackoverflow_survey_official/ ✅
│  └─ survey_results_public.csv (TO DOWNLOAD)
├─ 02_developer_salaries_kaggle/ (NOT AVAILABLE)
├─ 03_linkedin_data/ (NOT AVAILABLE)
├─ 04_immigration_government/ (NOT AVAILABLE)
└─ 05_talent_worldbank/ ✅
   └─ (API data)

DIMENSION 7: Future Trajectory
├─ historical_startup_data/
├─ historical_internet_speed/
├─ historical_economic_data/
└─ historical_patent_data/
```

---

## 🎯 QUICK REFERENCE: WHAT TO DOWNLOAD

### ✅ DOWNLOAD THESE (5 Kaggle datasets + 1 Official source):

```
1. Affordability & Livability
   └─ data_sources/1_affordability_livability/01_cost_of_living_numbeo/
      → cost_of_living.csv (50 MB)
      → https://www.kaggle.com/datasets/mvieira101/global-cost-of-living

2. Urban Development
   ├─ data_sources/4_urban_development/01_world_cities_kaggle/
   │  → worldcities.csv (50 MB)
   │  → https://www.kaggle.com/datasets/max-mind/world-cities-database
   │
   └─ data_sources/4_urban_development/02_city_temperature_kaggle/
      → city_temperature.csv (100 MB)
      → https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities

3. Innovation Readiness
   └─ data_sources/5_innovation_readiness/03_university_rankings_kaggle/
      → university_rankings.csv (10 MB)
      → https://www.kaggle.com/datasets/mylesoneill/world-university-rankings

4. Talent & Human Capital
   └─ data_sources/6_talent_human_capital/01_stackoverflow_survey_official/
      → survey_results_public.csv (100 MB)
      → https://insights.stackoverflow.com/survey

TOTAL: ~310 MB (5 datasets)
TIME: ~2-3 hours
```

### ✅ EXTRACT FROM WORLD BANK API (No download):

```
Via Python + wbdata library:

1. data_sources/1_affordability_livability/04_economic_worldbank/
   → gdp_per_capita.csv
   → gini_coefficient.csv
   → healthcare_spending.csv
   → education_spending.csv

2. data_sources/2_digital_infrastructure/05_digital_worldbank/
   → internet_users_pct.csv
   → broadband_subscriptions.csv
   → mobile_subscriptions.csv
   → internet_servers.csv

3. data_sources/4_urban_development/05_urban_worldbank/
   → urban_population_pct.csv
   → population_growth_rate.csv
   → land_area.csv

4. data_sources/5_innovation_readiness/07_innovation_worldbank/
   → research_and_development_pct.csv
   → scientific_publications.csv
   → high_tech_exports.csv

5. data_sources/6_talent_human_capital/05_talent_worldbank/
   → tertiary_education_pct.csv
   → literacy_rate.csv
   → education_spending_pct.csv
   → school_enrollment.csv
```

---

## 📖 HOW TO USE THIS STRUCTURE

### When you download a file:

```
Example 1: Cost of Living CSV
1. Download from Kaggle: https://www.kaggle.com/datasets/mvieira101/global-cost-of-living
2. Extract ZIP file
3. Find file: cost_of_living.csv
4. Place in: data_sources/1_affordability_livability/01_cost_of_living_numbeo/
5. Result: data_sources/1_affordability_livability/01_cost_of_living_numbeo/cost_of_living.csv

Example 2: World Cities CSV
1. Download from Kaggle: https://www.kaggle.com/datasets/max-mind/world-cities-database
2. Extract ZIP file
3. Find file: worldcities.csv
4. Place in: data_sources/4_urban_development/01_world_cities_kaggle/
5. Result: data_sources/4_urban_development/01_world_cities_kaggle/worldcities.csv
```

---

**This structure is organized by DIMENSION (what it measures) rather than by source type, making it logical for analysis and WEKA processing!** ✅

Ready to create this folder structure locally? 🚀