# 🚀 CITYMETRIC - CLAUDE CODE HANDOFF PACKAGE

## COMPLETE SETUP & PROMPT FOR SEAMLESS TRANSITION

---

## 📋 WHAT TO PREPARE BEFORE CLAUDE CODE

### 1. Local Project Structure (Already Created)

```
citymetric/
├── data_sources/
│   ├── 1_affordability_livability/
│   │   ├── 01_cost_of_living_numbeo/
│   │   │   └── metadata.txt
│   │   └── 02_economic_worldbank/
│   │       └── metadata.txt
│   ├── 2_digital_infrastructure/
│   │   └── 01_digital_worldbank/
│   │       └── metadata.txt
│   ├── 3_startup_ecosystem/
│   ├── 4_urban_development/
│   │   ├── 01_world_cities_kaggle/
│   │   │   └── metadata.txt
│   │   ├── 02_city_temperature_kaggle/
│   │   │   └── metadata.txt
│   │   └── 03_urban_worldbank/
│   │       └── metadata.txt
│   ├── 5_innovation_readiness/
│   │   ├── 01_university_rankings_kaggle/
│   │   │   └── metadata.txt
│   │   └── 02_innovation_worldbank/
│   │       └── metadata.txt
│   ├── 6_talent_human_capital/
│   │   ├── 01_stackoverflow_survey_official/
│   │   │   └── metadata.txt
│   │   └── 02_talent_worldbank/
│   │       └── metadata.txt
│   └── 7_future_trajectory/
│
├── data/ (empty for now)
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── scripts/ (will create these in Claude Code)
├── output/ (will generate these)
├── docs/ (documentation files)
│
└── README.md
```

### 2. Downloaded Datasets (Must have before Claude Code)

Download these 5 files and place them:

```
✅ MUST DOWNLOAD:
1. cost_of_living.csv 
   → data_sources/1_affordability_livability/01_cost_of_living_numbeo/

2. worldcities.csv 
   → data_sources/4_urban_development/01_world_cities_kaggle/

3. city_temperature.csv 
   → data_sources/4_urban_development/02_city_temperature_kaggle/

4. university_rankings.csv 
   → data_sources/5_innovation_readiness/01_university_rankings_kaggle/

5. survey_results_public.csv 
   → data_sources/6_talent_human_capital/01_stackoverflow_survey_official/
```

### 3. Documentation Files to Create

Create these text files in `docs/` folder:

**docs/PROJECT_CONTEXT.txt:**
```
PROJECT: CityMetric
TAGLINE: Measure Your City, Measure Your Future

OVERVIEW:
Global urban opportunity analysis platform analyzing 50-70 cities
across 7 dimensions using data mining (WEKA clustering), geospatial
visualization (Folium), and interactive dashboard (Streamlit).

DIMENSIONS:
1. Affordability & Livability (housing, cost of living, quality of life)
2. Digital Infrastructure (internet, connectivity, tech jobs)
3. Startup Ecosystem (startups, funding, innovation activity)
4. Urban Development (city structure, density, growth)
5. Innovation Readiness (patents, universities, research)
6. Talent & Human Capital (developers, education, skills)
7. Future Trajectory (growth trends, predictions)

DATA SOURCES (AVAILABLE):
- Affordability: Cost of Living (Kaggle) + World Bank API
- Digital: World Bank API only
- Startup: NONE (SKIP or use alternative)
- Urban: World Cities (Kaggle) + City Temperature (Kaggle) + World Bank API
- Innovation: University Rankings (Kaggle) + World Bank API
- Talent: Stack Overflow Survey (Official) + World Bank API
- Growth: Use historical data from above

TIMELINE: 4 weeks (150-170 hours)
TECH: Python (Claude Code) + WEKA + Folium + Plotly + Streamlit
DEPLOYMENT: Streamlit Cloud (FREE)
```

**docs/DATA_SOURCES_SUMMARY.txt:**
```
AVAILABLE DATA SOURCES:

KAGGLE DATASETS (5):
1. Cost of Living - https://www.kaggle.com/datasets/mvieira101/global-cost-of-living
2. World Cities - https://www.kaggle.com/datasets/max-mind/world-cities-database
3. City Temperature - https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities
4. University Rankings - https://www.kaggle.com/datasets/mylesoneill/world-university-rankings
5. Stack Overflow Survey - https://insights.stackoverflow.com/survey

WORLD BANK API (5):
1. Economic Data (GDP per capita, Gini, Healthcare, Education)
2. Digital Data (Internet users %, broadband, mobile, servers)
3. Urban Data (Urban population %, growth, land area)
4. Innovation Data (R&D spending, publications, high-tech exports)
5. Talent Data (Education %, literacy, education spending, enrollment)

MISSING DATA:
- All Dimension 3 (Startup Ecosystem) data sources NOT AVAILABLE
```

**docs/PHASE_BREAKDOWN.txt:**
```
PHASE 1: Data Collection (Week 1)
- Load CSVs from data_sources/
- Extract World Bank API data via wbdata library
- Validate data quality
- Output: data/raw/

PHASE 2: Data Preprocessing (Week 2)
- Clean & standardize all data
- Handle missing values
- Merge datasets by city
- Feature engineering: Create 7 composite scores (0-10)
- Output: data/processed/cities_features.csv

PHASE 3: WEKA Clustering (Week 3)
- Convert cities_features.csv → cities.arff (ARFF format)
- Open WEKA GUI
- Load cities.arff
- Run SimpleKMeans clustering (K=5)
- Export cluster assignments
- Import results back to Python
- Output: data/processed/cities_clustered_weka.csv

PHASE 4: Visualization (Week 3)
- Create Folium interactive map (colored by cluster)
- Create Plotly charts (radar, scatter, heatmap, etc)
- Generate analysis report (PDF)
- Output: output/

PHASE 5: Dashboard (Week 4)
- Build Streamlit app (7 pages)
- Deploy to Streamlit Cloud
- Output: Live URL

PHASE 6: Documentation (Week 4)
- Complete all docs
- Export final datasets
- Code review
- Output: docs/ + final CSVs
```

---

## 🎯 CLAUDE CODE MASTER PROMPT

Use this prompt in Claude Code to start:

```
You are helping me build CityMetric - a data-driven platform analyzing 
global cities across 7 dimensions (affordability, digital, startup, urban, 
innovation, talent, growth).

PROJECT CONTEXT:
- Project Name: CityMetric
- Tagline: "Measure Your City, Measure Your Future"
- Scope: 50-70 cities, 7 dimensions, data mining with WEKA clustering
- Tech: Python (Claude Code) + WEKA + Folium + Plotly + Streamlit
- Timeline: 4 weeks total, currently starting PHASE 1

PHASE 1: Data Collection (THIS PHASE)
Goal: Load all available datasets and extract World Bank API data
Datasets Available:
  Kaggle CSVs (5):
  1. cost_of_living.csv - data_sources/1_affordability_livability/01_cost_of_living_numbeo/
  2. worldcities.csv - data_sources/4_urban_development/01_world_cities_kaggle/
  3. city_temperature.csv - data_sources/4_urban_development/02_city_temperature_kaggle/
  4. university_rankings.csv - data_sources/5_innovation_readiness/01_university_rankings_kaggle/
  5. survey_results_public.csv - data_sources/6_talent_human_capital/01_stackoverflow_survey_official/
  
  World Bank API (5):
  - Economic data (GDP, Gini, healthcare, education)
  - Digital data (internet users %, broadband, mobile)
  - Urban data (urban population %, growth, land area)
  - Innovation data (R&D, publications, high-tech exports)
  - Talent data (tertiary education %, literacy, school enrollment)

NEXT STEPS:
1. Load all 5 Kaggle CSVs using pandas
2. Extract World Bank API data using wbdata library
3. Validate data quality and coverage
4. Organize into data/raw/ folder
5. Create summary statistics

IMPORTANT NOTES:
- Dimension 3 (Startup Ecosystem): NO DATA AVAILABLE - will skip
- All data should be saved to data/raw/ folder
- Document any data quality issues
- Keep file sizes reasonable for processing

Please start PHASE 1 by loading the Kaggle CSVs first.
```

---

## 📝 BEFORE YOU START CLAUDE CODE - CHECKLIST

### Pre-Claude Code Setup Checklist:

```
✅ FOLDER STRUCTURE:
  □ Created citymetric/ main folder
  □ Created data_sources/ with all 7 dimension subfolders
  □ Created data/{raw,processed,final}/ folders
  □ Created scripts/, output/, docs/ folders

✅ DOWNLOADED FILES:
  □ cost_of_living.csv → data_sources/1_affordability_livability/01_cost_of_living_numbeo/
  □ worldcities.csv → data_sources/4_urban_development/01_world_cities_kaggle/
  □ city_temperature.csv → data_sources/4_urban_development/02_city_temperature_kaggle/
  □ university_rankings.csv → data_sources/5_innovation_readiness/01_university_rankings_kaggle/
  □ survey_results_public.csv → data_sources/6_talent_human_capital/01_stackoverflow_survey_official/

✅ DOCUMENTATION:
  □ Created docs/PROJECT_CONTEXT.txt
  □ Created docs/DATA_SOURCES_SUMMARY.txt
  □ Created docs/PHASE_BREAKDOWN.txt

✅ GIT SETUP (OPTIONAL):
  □ git init
  □ git add .
  □ git commit -m "Initial CityMetric structure"
  □ git remote add origin https://github.com/[username]/citymetric

✅ READY FOR CLAUDE CODE:
  □ All files in correct locations
  □ All documentation prepared
  □ Project structure complete
```

---

## 🔧 HOW TO USE CLAUDE CODE EFFECTIVELY

### When Starting in Claude Code:

1. **First Message - Share Context:**
```
I'm starting PHASE 1 of CityMetric project. Here's my setup:

PROJECT: CityMetric - City Opportunity & Innovation Analysis
PHASE: 1 (Data Collection)
DATA LOCATION: project_folder/data_sources/
OUTPUT LOCATION: project_folder/data/raw/

AVAILABLE DATASETS:
- 5 Kaggle CSVs (already downloaded in data_sources/)
- 5 World Bank API endpoints (need extraction via Python)

TASK: Create 01_data_collection.py script that:
1. Loads all 5 Kaggle CSVs
2. Extracts World Bank data via wbdata library
3. Validates data quality
4. Saves all to data/raw/ folder
5. Creates summary statistics

Let me share the project structure and file locations...
```

2. **File Path Convention:**
```
Always reference files with paths:
- "data_sources/1_affordability_livability/01_cost_of_living_numbeo/cost_of_living.csv"
- "data/raw/" for outputs
- "scripts/" for code files
- Keep paths clear and consistent
```

3. **Data Dictionary Reference:**
```
When working with CSVs, ask Claude Code to:
- Print first few rows of each CSV
- Show column names
- Check data types
- Identify missing values
- Show basic statistics

Example:
"Print the shape, columns, and first 5 rows of each CSV"
```

4. **Phase-by-Phase Handoff:**
```
After each phase completes, save the prompt for next phase:

PHASE 2 PROMPT:
"I've completed PHASE 1 and have data/raw/ with all CSVs.
Now starting PHASE 2 (Data Preprocessing).
Please create 02_data_preprocessing.py that:
1. Loads all raw CSVs
2. Cleans & standardizes
3. Merges by city
4. Outputs: data/processed/cities_cleaned.csv"
```

---

## 📦 PHASE-BY-PHASE CLAUDE CODE PROMPTS

### PHASE 1 PROMPT (Ready to use):

```
PROJECT: CityMetric Data Collection

AVAILABLE DATASETS:
1. cost_of_living.csv (50 MB) - Numbeo data, housing/food/transport costs
2. worldcities.csv (50 MB) - City locations, population, area
3. city_temperature.csv (100 MB) - Daily temp for 100+ cities, 1743-2013
4. university_rankings.csv (10 MB) - QS/Times rankings, research scores
5. survey_results_public.csv (100 MB) - Stack Overflow developer survey

TASK: Create 01_data_collection.py that:

1. LOAD KAGGLE CSVs
   - Read all 5 CSVs from data_sources/ subfolders
   - Print shape, columns, dtypes for each
   - Check for missing values
   - Display first row of each

2. EXTRACT WORLD BANK API
   - Use wbdata library
   - Extract 5 datasets:
     a) Economic: NY.GDP.PCAP.CD (GDP per capita), SI.POV.GINI (Gini)
     b) Digital: IT.NET.USER.ZS (internet %), IT.NET.BBND.P2 (broadband)
     c) Urban: SP.URB.TOTL.IN.ZS (urban %), SP.POP.GROW (growth)
     d) Innovation: GB.XPD.RSDV.GD.ZS (R&D %), IP.JRN.ARTC.SC (publications)
     e) Talent: SE.ADT.TERT.ZS (tertiary ed %), SE.ADT.LITR.ZS (literacy)
   - Save each to CSV

3. VALIDATION
   - Check data coverage (countries/cities)
   - Identify missing values
   - Print summary stats

4. OUTPUT
   - Save all CSVs to data/raw/ folder
   - Create data_collection_summary.txt with statistics
   - List all files created

5. ERROR HANDLING
   - Try-except for file loading
   - Handle API connection issues
   - Document any failures

DELIVERABLES:
- scripts/01_data_collection.py (complete, runnable script)
- data/raw/ folder with all CSVs
- Data collection summary report
```

### PHASE 2 PROMPT (For after Phase 1):

```
PROJECT: CityMetric Data Preprocessing

INPUT: data/raw/ folder with all CSVs from Phase 1

TASK: Create 02_data_preprocessing.py that:

1. LOAD ALL DATA
   - Load 5 Kaggle CSVs from data/raw/
   - Load 5 World Bank CSVs from data/raw/

2. DATA CLEANING
   - Remove duplicate rows
   - Standardize column names (lowercase, underscores)
   - Handle missing values strategy:
     * Drop if >30% missing
     * Fill with mean/median if <30%
   - Remove outliers (check for unrealistic values)

3. CITY MATCHING
   - Identify common cities across all datasets
   - Create master city list (50-70 cities minimum)
   - Match cities across datasets (handle spelling variations)
   - Document any unmatched cities

4. STANDARDIZATION
   - Convert all currencies to USD
   - Standardize units (e.g., per capita, percentages)
   - Normalize numeric columns where needed

5. OUTPUT
   - data/processed/cities_cleaned.csv
   - Contains: city, country, all raw metrics
   - Document cleaning process

DELIVERABLES:
- scripts/02_data_preprocessing.py
- data/processed/cities_cleaned.csv
- Cleaning summary report
```

### PHASE 3 PROMPT (For WEKA - after Phase 2):

```
PROJECT: CityMetric Feature Engineering & WEKA Preparation

INPUT: data/processed/cities_cleaned.csv

TASK: Create 03_feature_engineering.py that:

1. FEATURE ENGINEERING
   Create 7 composite scores (0-10 scale):
   
   1_AFFORDABILITY:
     - Inputs: rent, food costs, salary, CoL
     - Formula: Min-Max normalize to 0-10
   
   2_DIGITAL:
     - Inputs: internet %, broadband, mobile
     - Formula: Min-Max normalize to 0-10
   
   3_STARTUP:
     - Input: SKIP (no data available)
     - Use: 0 or placeholder
   
   4_URBAN:
     - Inputs: population density, city size, growth
     - Formula: Min-Max normalize to 0-10
   
   5_INNOVATION:
     - Inputs: university ranks, R&D spending
     - Formula: Min-Max normalize to 0-10
   
   6_TALENT:
     - Inputs: developer count, education %, salary
     - Formula: Min-Max normalize to 0-10
   
   7_GROWTH:
     - Inputs: historical growth data
     - Formula: Min-Max normalize to 0-10
   
   OVERALL_INDEX:
     - Average of all 7 scores
     - Scale 0-10

2. WEKA PREPARATION
   - Select features: all 7 scores
   - Create ARFF file format:
     @relation city_opportunity
     @attribute city string
     @attribute country string
     @attribute affordability numeric
     @attribute digital numeric
     @attribute startup numeric
     @attribute urban numeric
     @attribute innovation numeric
     @attribute talent numeric
     @attribute growth numeric
     @data
   - Save as data/processed/cities.arff

3. OUTPUT
   - data/processed/cities_features.csv (with all scores)
   - data/processed/cities.arff (for WEKA)
   - Feature engineering summary

DELIVERABLES:
- scripts/03_feature_engineering.py
- data/processed/cities_features.csv
- data/processed/cities.arff (READY FOR WEKA!)
- Feature summary report

NEXT STEP: 
- Open WEKA GUI
- Load cities.arff
- Run SimpleKMeans clustering
- Export results to weka/ folder
```

### PHASE 4 PROMPT (After WEKA clustering):

```
PROJECT: CityMetric WEKA Results Import

INPUT: 
- data/processed/cities_features.csv
- WEKA output files (weka/weka_cluster_assignments.txt, etc.)

TASK: Create 04_weka_results_import.py that:

1. IMPORT WEKA RESULTS
   - Read weka/weka_cluster_assignments.txt
   - Extract cluster assignments for each city
   - Validate all cities have assignments

2. MERGE WITH FEATURES
   - Load cities_features.csv
   - Add cluster_id column from WEKA
   - Add cluster_name (descriptive labels)
   - Create cluster_profiles (mean/std per cluster)

3. OUTPUT
   - data/processed/cities_clustered_weka.csv
   - data/processed/cluster_profiles.csv
   - Clustering summary & insights

DELIVERABLES:
- scripts/04_weka_results_import.py
- data/processed/cities_clustered_weka.csv
- data/processed/cluster_profiles.csv
```

---

## 📋 QUICK REFERENCE - WHAT TO HAVE READY

**BEFORE Starting Claude Code Session:**

```
READY:
✅ Folder structure created
✅ 5 Kaggle CSVs downloaded & in correct locations
✅ Project context document prepared
✅ Data sources summary ready
✅ Phase breakdown documented
✅ This Claude Code handoff guide

IN CLAUDE CODE, YOU'LL CREATE:
📝 01_data_collection.py
📝 02_data_preprocessing.py
📝 03_feature_engineering.py
📝 04_arff_conversion.py
📝 05_weka_results_import.py
📝 06_visualizations.py
📝 07_streamlit_app.py

DATA FLOW:
data_sources/ → data/raw/ → data/processed/ → data/final/ → output/ → Streamlit Cloud
```

---

**You're 100% ready for Claude Code now!** 🚀

Just paste the relevant PHASE PROMPT when you start each phase, and Claude Code will take it from there! 

Good luck! 💪📊