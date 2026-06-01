# 🌍 GLOBAL CITY OPPORTUNITY & INNOVATION ECOSYSTEM INDEX
## Complete Project Specification (Claude Code Edition)

---

## TABLE OF CONTENTS

1. [Project Overview](#project-overview)
2. [The 7 Key Dimensions](#the-7-key-dimensions)
3. [Complete Architecture](#complete-architecture)
4. [Phase 1: Data Collection](#phase-1-data-collection-week-1)
5. [Phase 2: Data Preprocessing](#phase-2-data-preprocessing-week-2)
6. [Phase 3: Clustering & Analysis](#phase-3-clustering--analysis-week-3)
7. [Phase 4: Visualization & Analysis](#phase-4-visualization--analysis-week-3-days-4-5)
8. [Phase 5: Interactive Dashboard](#phase-5-interactive-dashboard-week-4-days-1-3)
9. [Phase 6: Documentation](#phase-6-documentation--finalization-week-4-days-4-7)
10. [Deliverables Checklist](#-complete-deliverables-checklist)
11. [Tools & Platforms](#-tools--platforms-required)
12. [Data Structure](#-data-structure-final-csv)
13. [Timeline & Workload](#-realistic-timeline--workload)
14. [Success Criteria](#-success-criteria)

---

## PROJECT OVERVIEW

```
Project Name: GCOI Index 2024-2030
            (Global City Opportunity & Innovation Index)

Subtitle: "Where should you build, invest, or move? 
          Data-driven city intelligence platform."

Description: Comprehensive multi-dimensional analysis of 50-70 global cities
            across 7 key dimensions (affordability, digital access, startup
            ecosystem, urban development, innovation, talent, growth potential).
            
            Combines data mining (Scikit-learn clustering), geospatial
            visualization (Folium), and interactive dashboard (Streamlit).

Type: Full-stack data engineering + analytics project
Scope: 50-70 cities, 7 dimensions, 50+ features
Timeline: 4 weeks
Tech Stack: Python (100% in Claude Code)
Deployment: Streamlit Cloud (FREE)
```

---

## THE 7 KEY DIMENSIONS

| # | Dimension | Key Metrics | Data Sources |
|---|-----------|------------|--------------|
| 1 | **Affordability & Livability** | Housing costs, CoL, salary, QoL | Numbeo, Glassdoor, World Bank |
| 2 | **Digital Infrastructure** | Internet speed, 5G, tech talent | Speedtest, Internet Stats, Indeed |
| 3 | **Startup Ecosystem** | Startups, funding, tech jobs, growth | Crunchbase, AngelList, GitHub |
| 4 | **Urban Development** | Sprawl, density, infrastructure | OpenStreetMap, WorldPop, UN-Habitat |
| 5 | **Innovation Readiness** | Patents, research, R&D investment | Google Patents, University Rankings |
| 6 | **Talent & Human Capital** | Education, talent attraction, diversity | Stack Overflow, World Bank, LinkedIn |
| 7 | **Future Trajectory** | Historical growth, prediction, potential | Time-series analysis from above |

---

## COMPLETE ARCHITECTURE

```
PROJECT STRUCTURE:
═══════════════════════════════════════════════════════════

gcoi-index-2024/
│
├── 📁 data/
│   ├── raw/
│   │   ├── numbeo_raw.csv
│   │   ├── crunchbase_raw.csv
│   │   ├── speedtest_raw.csv
│   │   ├── worldbank_raw.csv
│   │   ├── openstreetmap_raw.csv
│   │   ├── patents_raw.csv
│   │   └── stackoverflow_raw.csv
│   │
│   ├── processed/
│   │   ├── cities_cleaned.csv
│   │   ├── cities_features.csv
│   │   └── cities_clustered.csv
│   │
│   └── final/
│       ├── gcoi_index_final.csv
│       └── cluster_analysis.csv
│
├── 📁 scripts/ (Claude Code artifacts)
│   ├── 01_data_collection.py
│   ├── 02_data_preprocessing.py
│   ├── 03_feature_engineering.py
│   ├── 04_clustering_analysis.py
│   ├── 05_visualizations.py
│   └── 06_streamlit_app.py
│
├── 📁 output/
│   ├── map_interactive.html (Folium)
│   ├── charts_analysis.html (Plotly)
│   └── cluster_analysis_report.pdf
│
├── 📁 docs/
│   ├── README.md (project overview)
│   ├── METHODOLOGY.md (detailed approach)
│   ├── DATA_SOURCES.md (all sources + access methods)
│   ├── FINDINGS.md (key insights)
│   └── DEPLOYMENT.md (how to run)
│
└── streamlit_app.py (main dashboard)
```

---

## PHASE 1: DATA COLLECTION (WEEK 1)

### STEP 1.1: Set Up Environment

**Platform:** Claude Code  
**Timeline:** Days 1-2  
**Task:** Create data collection infrastructure

**Artifact: setup_environment.py**

```
Tasks:
├─ Install required libraries
├─ Create folder structure
├─ Set up API credentials/keys
└─ Test connections

Libraries needed:
├─ pandas (data manipulation)
├─ requests (HTTP requests)
├─ beautifulsoup4 (web scraping)
├─ selenium OR playwright (dynamic content)
├─ geopy (geocoding)
├─ numpy (numerical)
└─ csv (file handling)

Installation command:
pip install pandas requests beautifulsoup4 selenium geopy numpy
```

---

### STEP 1.2: Collect Dimension 1 - AFFORDABILITY

**Platform:** Claude Code  
**Timeline:** Days 1-2

**Artifact: collect_affordability.py**

```
Tasks:
├─ Scrape Numbeo cost of living data
│  ├─ Target: 50-70 cities
│  ├─ Metrics: rent, food, transport, utilities
│  └─ Output: affordability_raw.csv
│
├─ Fetch World Bank economic data (API)
│  ├─ GDP per capita
│  ├─ Gini coefficient
│  └─ Other economic indicators
│
└─ Scrape Glassdoor salary data
   ├─ Average salaries per city
   ├─ Tech job salaries
   └─ Salary ranges

Output files:
├─ numbeo_affordability.csv
├─ worldbank_economic.csv
└─ glassdoor_salary.csv

Error handling:
├─ Rate limiting (add delays between requests)
├─ Missing data (log and note)
└─ Data validation (check for outliers)
```

---

### STEP 1.3: Collect Dimension 2 - DIGITAL INFRASTRUCTURE

**Platform:** Claude Code  
**Timeline:** Days 2-3

**Artifact: collect_digital.py**

```
Tasks:
├─ Download/scrape Speedtest data
│  ├─ Download speed (Mbps)
│  ├─ Upload speed (Mbps)
│  ├─ Latency
│  └─ 5G coverage %
│
├─ Scrape Internet World Stats
│  ├─ Internet penetration %
│  ├─ Active users
│  ├─ Smartphone penetration
│  └─ Digital literacy
│
└─ Scrape Indeed for tech jobs (as talent proxy)
   ├─ Tech job count per city
   ├─ Average tech salary
   └─ In-demand skills

Output files:
├─ speedtest_digital.csv
├─ internet_penetration.csv
└─ tech_jobs_indeed.csv

Data quality checks:
├─ Validate speed values (logical ranges)
├─ Check for duplicates
└─ Ensure all cities have data
```

---

### STEP 1.4: Collect Dimension 3 - STARTUP ECOSYSTEM

**Platform:** Claude Code  
**Timeline:** Days 3-4

**Artifact: collect_startups.py**

```
Tasks:
├─ Download Crunchbase data from Kaggle
│  ├─ Use: kagglehub library OR manual download
│  ├─ Extract: startups per city, funding, dates
│  └─ Metrics: startup count, total funding, avg funding
│
├─ Fetch AngelList API data
│  ├─ Startups per location
│  ├─ Funding received
│  ├─ Investor concentration
│  └─ Auth: requires free API key
│
├─ Use GitHub API for tech activity
│  ├─ Query companies by location
│  ├─ Count repositories, stars
│  ├─ Measure development activity
│  └─ Auth: requires free GitHub token
│
└─ Extract job data from Indeed
   ├─ Already scraped in Dimension 2
   ├─ Use for startup opportunity metric

Output files:
├─ crunchbase_startups.csv
├─ angellist_funding.csv
├─ github_companies.csv
└─ startup_opportunity.csv

Calculations:
├─ Startup density (startups per 100k population)
├─ Total funding per city
├─ Avg funding per startup
└─ Startup growth rate (YoY if historical data available)
```

---

### STEP 1.5: Collect Dimension 4 - URBAN DEVELOPMENT

**Platform:** Claude Code  
**Timeline:** Days 4-5

**Artifact: collect_urban.py**

```
Tasks:
├─ Use OpenStreetMap API (via osmnx library)
│  ├─ Query road networks per city
│  ├─ Calculate road density (sprawl indicator)
│  ├─ Count buildings, parks, infrastructure
│  └─ Analyze walkability patterns
│
├─ Download WorldPop density data
│  ├─ Get population density rasters
│  ├─ Calculate density per city
│  └─ Measure urban concentration
│
├─ Fetch World Bank urban data
│  ├─ Urban population %
│  ├─ City growth rate
│  ├─ Infrastructure investment
│  └─ Already have API access
│
└─ Manual research (UN-Habitat)
   ├─ Sprawl index
   ├─ Development trajectory
   └─ Urban quality indicators

Libraries needed:
├─ osmnx (OpenStreetMap)
├─ rasterio (for density rasters)
└─ shapely (geometric operations)

Output files:
├─ osm_urban_metrics.csv
├─ worldpop_density.csv
└─ urban_development_score.csv

Metrics calculated:
├─ Road density
├─ Population density
├─ Urban sprawl index
└─ Infrastructure quality score
```

---

### STEP 1.6: Collect Dimension 5 - INNOVATION

**Platform:** Claude Code  
**Timeline:** Days 5-6

**Artifact: collect_innovation.py**

```
Tasks:
├─ Download patent data from Kaggle
│  ├─ Pre-processed patent datasets available
│  ├─ Extract: patents per city, by year
│  ├─ Calculate: patent density, innovation rate
│  └─ Identify: technology focus per city
│
├─ Scrape university rankings
│  ├─ QS World Rankings
│  ├─ Times Higher Education
│  ├─ SCIMAGO Research Rankings
│  └─ Extract: top universities per city
│
├─ Collect research publication data
│  ├─ From SCIMAGO or similar
│  ├─ Count publications per city
│  ├─ Calculate citation impact
│  └─ Measure research output
│
└─ Compile R&D investment data
   ├─ World Bank R&D spending %
   ├─ Government statistics
   └─ Corporate R&D by city (if available)

Output files:
├─ patents_innovation.csv
├─ university_rankings.csv
├─ research_publications.csv
└─ innovation_readiness.csv

Calculations:
├─ Patent density (patents per 100k population)
├─ University quality score
├─ Research output index
└─ Innovation readiness overall score
```

---

### STEP 1.7: Collect Dimension 6 - TALENT & HUMAN CAPITAL

**Platform:** Claude Code  
**Timeline:** Days 6-7

**Artifact: collect_talent.py**

```
Tasks:
├─ Use Stack Overflow Developer Survey data
│  ├─ Download: https://insights.stackoverflow.com/survey
│  ├─ Extract: developer distribution by location
│  ├─ Get: skill distribution per region
│  └─ Analyze: developer concentration
│
├─ Fetch World Bank education data (API)
│  ├─ Tertiary education enrollment %
│  ├─ Education quality index
│  ├─ Skilled workforce metrics
│  └─ Already have API access
│
├─ Scrape government immigration data
│  ├─ Visa statistics (if public)
│  ├─ Tech worker visa approvals
│  ├─ Skilled worker immigration
│  └─ May need manual research
│
└─ Analyze brain drain
   ├─ Outward migration statistics
   ├─ Remittance flows (World Bank)
   ├─ Talent retention rate
   └─ Visa approval trends

Output files:
├─ stackoverflow_developers.csv
├─ education_quality.csv
├─ immigration_data.csv
└─ talent_index.csv

Calculations:
├─ Tech talent concentration
├─ Education quality score
├─ Talent attraction/retention rate
└─ Human capital index
```

---

### STEP 1.8: Compile Historical Data - FUTURE TRAJECTORY

**Platform:** Claude Code  
**Timeline:** Days 7-8

**Artifact: collect_historical.py**

```
Tasks:
├─ Compile historical startup data
│  ├─ Crunchbase with founding dates
│  ├─ Track startups over time (2014-2024)
│  ├─ Calculate growth rates per year
│  └─ Identify "rising star" patterns
│
├─ Collect historical speed data
│  ├─ Speedtest historical reports
│  ├─ Track internet improvement over time
│  └─ Measure digital growth trajectory
│
├─ Gather economic growth data
│  ├─ World Bank historical GDP
│  ├─ Population growth rates
│  └─ Development trajectory
│
└─ Compile job market trends
   ├─ Historical job posting counts
   ├─ Tech job market growth
   └─ Opportunity growth rate

Output files:
├─ historical_startups.csv
├─ historical_speed.csv
├─ historical_economy.csv
└─ growth_trajectory.csv

Calculations:
├─ 5-year growth rates
├─ Growth trajectory classification
├─ Future potential prediction
└─ Risk factors identification
```

**OUTPUT OF PHASE 1:** 15+ raw CSV files in data/raw/ folder

---

## PHASE 2: DATA PREPROCESSING (WEEK 2)

### STEP 2.1: Data Cleaning & Validation

**Platform:** Claude Code  
**Timeline:** Days 8-10

**Artifact: preprocess_data.py**

```
Tasks:
├─ Load all raw CSV files
├─ Data quality assessment
│  ├─ Check missing values
│  ├─ Identify outliers
│  ├─ Validate data types
│  └─ Detect duplicates
│
├─ Handle missing data
│  ├─ For quantitative: interpolate or use mean
│  ├─ For categorical: use mode or drop
│  ├─ Document decisions
│  └─ Log imputation records
│
├─ Standardize city names
│  ├─ Ensure consistent spelling
│  ├─ Match across all datasets
│  ├─ Create city lookup table
│  └─ Handle country names
│
├─ Standardize units
│  ├─ Currency conversion (to USD)
│  ├─ Speed units (to Mbps)
│  ├─ Population (to actual numbers)
│  └─ Create conversion factors
│
└─ Validate value ranges
   ├─ Remove obvious errors
   ├─ Flag suspicious values
   ├─ Keep detailed audit log
   └─ Manual review for edge cases

Pandas operations:
├─ df.isnull().sum() - check missing
├─ df.describe() - check ranges
├─ df.drop_duplicates() - remove dupes
├─ df.fillna() - handle missing
├─ String operations for standardization

Output file:
└─ cities_cleaned.csv (with all dimensions, cleaned)

Quality metrics:
├─ % missing data per column
├─ Outlier count per column
├─ Data completeness score
└─ Validation report
```

---

### STEP 2.2: Merge All Data Sources

**Platform:** Claude Code  
**Timeline:** Days 10-11

**Artifact: merge_datasets.py**

```
Tasks:
├─ Create master city list
│  ├─ 50-70 target cities
│  ├─ Add coordinates (lat/lon)
│  ├─ Add country, region, continent
│  └─ Create city_id for linking
│
├─ Merge dimension data by city
│  ├─ Left join on city name
│  ├─ Preserve all cities
│  ├─ Handle unmatched entries
│  └─ Create merge quality report
│
├─ Create dimension-specific tables
│  ├─ Table for affordability metrics
│  ├─ Table for digital metrics
│  ├─ Table for startup metrics
│  ├─ Table for urban metrics
│  ├─ Table for innovation metrics
│  ├─ Table for talent metrics
│  └─ Table for growth metrics
│
└─ Final master dataset
   ├─ One row per city
   ├─ ~50-70 columns (metrics)
   ├─ All 7 dimensions represented
   └─ Ready for feature engineering

Merge operations:
├─ pd.merge(left, right, on='city', how='left')
├─ Verify merge completeness
├─ Document join losses
└─ Quality assurance

Output file:
└─ cities_merged_raw.csv
```

---

### STEP 2.3: Create Composite Scores

**Platform:** Claude Code  
**Timeline:** Days 12-14

**Artifact: feature_engineering.py**

```
DIMENSION 1: AFFORDABILITY SCORE (0-10)
├─ Input metrics:
│  ├─ Rent ($/month)
│  ├─ Cost of living index
│  ├─ Salary levels (avg)
│  └─ Salary-to-CoL ratio
├─ Calculation:
│  ├─ Normalize each metric
│  ├─ Weight: (salary/CoL) heavily weighted
│  ├─ Invert rent (higher = less affordable)
│  └─ Final score: weighted average
└─ Output: affordability_score (0-10)

DIMENSION 2: DIGITAL ACCESS SCORE (0-10)
├─ Input metrics:
│  ├─ Internet speed (Mbps)
│  ├─ Internet penetration %
│  ├─ 5G coverage %
│  └─ Smartphone penetration %
├─ Calculation:
│  ├─ Normalize all metrics (0-10)
│  ├─ Equal weights
│  └─ Average
└─ Output: digital_score (0-10)

DIMENSION 3: STARTUP OPPORTUNITY SCORE (0-10)
├─ Input metrics:
│  ├─ Startup density (per capita)
│  ├─ Total funding ($)
│  ├─ Avg funding per startup
│  ├─ Startup growth rate (YoY)
│  └─ Tech job count
├─ Calculation:
│  ├─ Normalize each
│  ├─ Weight growth heavily
│  ├─ Weight funding moderately
│  └─ Weighted average
└─ Output: startup_score (0-10)

DIMENSION 4: URBAN DEVELOPMENT SCORE (0-10)
├─ Input metrics:
│  ├─ Road density
│  ├─ Population density
│  ├─ Urban sprawl index
│  └─ Infrastructure quality
├─ Calculation:
│  ├─ Normalize metrics
│  ├─ Prefer compact development (penalize sprawl)
│  ├─ Weight infrastructure highly
│  └─ Weighted average
└─ Output: urban_score (0-10)

DIMENSION 5: INNOVATION READINESS SCORE (0-10)
├─ Input metrics:
│  ├─ Patent density
│  ├─ University quality
│  ├─ Research publications
│  └─ R&D investment %
├─ Calculation:
│  ├─ Normalize all
│  ├─ Weight patents highly
│  ├─ Weight research moderately
│  └─ Weighted average
└─ Output: innovation_score (0-10)

DIMENSION 6: TALENT & HUMAN CAPITAL SCORE (0-10)
├─ Input metrics:
│  ├─ Education quality
│  ├─ Tech talent concentration
│  ├─ Immigration-friendly index
│  └─ Brain drain rate (inverted)
├─ Calculation:
│  ├─ Normalize metrics
│  ├─ Invert brain drain
│  ├─ Weight education highly
│  └─ Weighted average
└─ Output: talent_score (0-10)

DIMENSION 7: GROWTH POTENTIAL SCORE (0-10)
├─ Input metrics:
│  ├─ Historical growth rate (5-yr)
│  ├─ Current growth trajectory
│  ├─ Risk factors (economic, political)
│  └─ Opportunity indicators
├─ Calculation:
│  ├─ Normalize growth rates
│  ├─ Apply risk adjustments
│  ├─ Project future trajectory
│  └─ Weighted average with time decay
└─ Output: growth_score (0-10)

OVERALL OPPORTUNITY INDEX
├─ Calculation:
│  ├─ Equal weight all 6 dimensions
│  ├─ Special weight growth if high
│  └─ Final formula: weighted_avg([afford, digital, startup, urban, innovation, talent])
└─ Output: opportunity_index (0-10)

Normalization strategy:
├─ Min-Max scaling (0-10 scale)
├─ Formula: ((x - min) / (max - min)) * 10
├─ Handle outliers (cap at 0-10)
└─ Document all weights & formulas

Output file:
└─ cities_features.csv (with all calculated scores)
```

---

### STEP 2.4: Add Metadata & Geographic Data

**Platform:** Claude Code  
**Timeline:** Days 14-15

**Artifact: add_metadata.py**

```
Tasks:
├─ Add city coordinates (if not present)
│  ├─ Use geopy library
│  ├─ Geocode city names to lat/lon
│  ├─ Cache results to avoid re-geocoding
│  └─ Output: latitude, longitude columns
│
├─ Add region classification
│  ├─ Map cities to regions: Asia-Pacific, Europe, Americas, etc
│  ├─ Create region_id for clustering analysis
│  └─ Output: region column
│
├─ Add country classification
│  ├─ Extract from city data
│  ├─ Add country_code (ISO)
│  └─ Output: country, country_code columns
│
├─ Add city size classification
│  ├─ Based on population
│  ├─ Classify: small, medium, large, megacity
│  └─ Output: city_size column
│
└─ Create summary statistics
   ├─ Data completeness per city
   ├─ Data quality score per row
   └─ Flags for manual review

Output file:
└─ cities_with_metadata.csv
```

**OUTPUT OF PHASE 2:** cities_features.csv (ready for clustering)

---

## PHASE 3: CLUSTERING & ANALYSIS WITH WEKA (WEEK 3)

### STEP 3.0: Data Preparation & Feature Selection

**Platform:** Claude Code  
**Timeline:** Days 15-16

**Artifact: prepare_for_weka.py**

```
Tasks:
├─ Select features for clustering
│  ├─ Use the 7 main scores (0-10 scale)
│  ├─ Decision: use 7 scores (cleaner, interpretable)
│  └─ Features: [afford, digital, startup, urban, innovation, talent, growth]
│
├─ Remove rows with excessive missing data
│  ├─ Threshold: drop if >2 missing values
│  ├─ Document exclusions
│  └─ Final dataset: 45-65 cities
│
├─ Add city identifiers (for WEKA output tracking)
│  ├─ city_id, city_name, country
│  └─ These will help match results back
│
└─ Create final feature CSV
   ├─ Clean, no missing values
   ├─ Ready for ARFF conversion
   └─ Save as cities_features_clean.csv

Output file:
└─ cities_features_clean.csv (ready for WEKA)
```

---

### STEP 3.1: Convert CSV to ARFF Format (untuk WEKA)

**Platform:** Claude Code  
**Timeline:** Days 16-17

**Artifact: convert_to_arff.py**

```
Tasks:
├─ Load clean feature CSV
├─ Define ARFF attribute structure
│  ├─ numeric for each dimension score
│  ├─ string for city names
│  └─ Follow WEKA ARFF format specification
│
├─ Generate ARFF file header
│  ├─ @relation city_opportunity
│  ├─ @attribute definitions (7 numeric + metadata)
│  └─ @data section marker
│
├─ Write data rows in ARFF format
│  ├─ Values separated by commas
│  ├─ String values in single quotes
│  ├─ No missing values allowed
│  └─ Validate format
│
└─ Save ARFF file
   └─ Output: cities.arff (WEKA-ready)

Python code example:
import pandas as pd

data = pd.read_csv('cities_features_clean.csv')

arff_content = """@relation city_opportunity

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
"""

for idx, row in data.iterrows():
    line = f"'{row['city']}','{row['country']}',"
    line += f"{row['affordability_score']},"
    line += f"{row['digital_score']},"
    line += f"{row['startup_score']},"
    line += f"{row['urban_score']},"
    line += f"{row['innovation_score']},"
    line += f"{row['talent_score']},"
    line += f"{row['growth_score']}"
    arff_content += line + "\n"

with open('cities.arff', 'w') as f:
    f.write(arff_content)

Output file:
└─ cities.arff (WEKA format)
```

---

### STEP 3.2: WEKA Clustering (GUI)

**Platform:** WEKA Desktop Application  
**Timeline:** Days 17-18

**WEKA Clustering Process:**

```
Installation:
├─ Download WEKA: https://www.cs.waikato.ac.nz/ml/weka/
├─ Install Java (WEKA requires Java)
├─ Run WEKA GUI Chooser

Steps:
1. Open WEKA Explorer
   ├─ Applications → Weka → Weka GUI Chooser
   └─ Click "Explorer"

2. Load data
   ├─ Click "Open file..."
   ├─ Navigate to cities.arff
   ├─ Select it
   └─ Dataset loaded in Preprocess tab

3. Go to Cluster tab
   ├─ Click "Cluster" tab at top
   ├─ Click "Choose" button
   ├─ Select Clusterers → SimpleKMeans
   └─ SimpleKMeans selected

4. Configure K-Means
   ├─ numClusters: 5 (or test 2-10)
   ├─ seed: 42 (for reproducibility)
   ├─ distance function: Euclidean
   ├─ maxIterations: 100
   └─ Save other defaults

5. Run clustering
   ├─ Click "Start"
   ├─ Wait for completion
   ├─ See cluster summary in Results

6. Analyze results
   ├─ View "Cluster centroids" (mean values)
   ├─ View cluster sizes
   ├─ View silhouette coefficient
   ├─ Check "Classes to clusters" evaluation

7. Visualize
   ├─ Right-click on result → Visualize
   ├─ 3D scatter plot of clusters
   ├─ Save visualization (screenshot)

8. Try different K values (optional)
   ├─ Change numClusters to 2, 3, 4, 6, 7...
   ├─ Rerun
   ├─ Compare silhouette scores
   ├─ Choose best K (likely 5)

Output from WEKA:
├─ Cluster assignments (in Cluster mode)
├─ Silhouette values per instance
├─ Centroids (attribute values per cluster)
├─ Cluster sizes
└─ Visualization (3D plot)
```

---

### STEP 3.3: Export WEKA Results

**Platform:** WEKA GUI  
**Timeline:** Days 18

**Export Steps:**

```
Option 1: Copy from WEKA GUI
├─ In Results tab, select all text
├─ Copy to clipboard
├─ Paste to text file
└─ Save as weka_cluster_output.txt

Option 2: Save WEKA model
├─ File → Save model
├─ Save as model_kmeans_k5.model
├─ Can reload/use later

Option 3: Export predictions
├─ Right-click result → Visualize
├─ Manually note cluster assignments
└─ Or use WEKA CLI for batch processing

What to extract:
├─ Which city belongs to which cluster
├─ Cluster centroids (mean values per cluster)
├─ Cluster sizes
├─ Silhouette coefficient (quality metric)
└─ Any cluster statistics

Save outputs:
├─ weka_cluster_assignments.txt (city → cluster mapping)
├─ weka_cluster_centroids.txt (center values)
├─ weka_evaluation_metrics.txt (silhouette, etc)
└─ weka_visualization.png (screenshot of 3D plot)
```

---

### STEP 3.4: Import WEKA Results Back to Python

**Platform:** Claude Code  
**Timeline:** Days 18-19

**Artifact: import_weka_results.py**

```
Tasks:
├─ Parse WEKA output text
│  ├─ Extract cluster assignments per city
│  ├─ Extract centroids values
│  ├─ Extract silhouette scores
│  └─ Extract cluster statistics
│
├─ Create mapping: city → cluster_id
│  ├─ From WEKA output text
│  ├─ Manual parsing or regex
│  └─ Validate completeness
│
├─ Merge with original data
│  ├─ Load original cities_features_clean.csv
│  ├─ Add cluster_id column (from WEKA)
│  ├─ Add cluster_name (descriptive)
│  └─ Maintain city metadata (country, region, etc)
│
├─ Create cluster profiles
│  ├─ Calculate mean values per cluster
│  ├─ Std deviation per cluster
│  ├─ Min/max per cluster
│  └─ Cluster size
│
└─ Save merged dataset
   ├─ cities_clustered_weka.csv
   ├─ All original data + cluster assignments
   ├─ Ready for visualization
   └─ Ready for dashboard

Python code example:
import pandas as pd
import re

# Load original data
data = pd.read_csv('cities_features_clean.csv')

# Parse WEKA output (manual or regex depending on format)
# Example: WEKA lists "Instance 0 -> Cluster 2"
weka_output = open('weka_cluster_assignments.txt').read()

clusters = {}
for line in weka_output.split('\n'):
    if ' -> Cluster ' in line:
        # Extract instance number and cluster
        match = re.search(r'Instance (\d+) -> Cluster (\d+)', line)
        if match:
            idx = int(match.group(1))
            cluster = int(match.group(2))
            clusters[idx] = cluster

# Add clusters to data
data['cluster'] = data.index.map(clusters)

# Create cluster names
cluster_names = {
    0: 'Established Hubs',
    1: 'Rising Stars',
    2: 'Affordable Emerging',
    3: 'Balanced Development',
    4: 'Unique Profile'
}
data['cluster_name'] = data['cluster'].map(cluster_names)

# Cluster profiles
cluster_profiles = data.groupby('cluster')[[
    'affordability_score', 'digital_score', 'startup_score',
    'urban_score', 'innovation_score', 'talent_score', 'growth_score'
]].agg(['mean', 'std', 'min', 'max'])

print(cluster_profiles)

# Save
data.to_csv('cities_clustered_weka.csv', index=False)
cluster_profiles.to_csv('cluster_profiles_weka.csv')

Output files:
├─ cities_clustered_weka.csv (cities + clusters)
├─ cluster_profiles_weka.csv (statistics per cluster)
└─ weka_analysis_summary.txt (documentation)
```

---

### STEP 3.5: Feature Importance & Cluster Analysis (Python)

**Platform:** Claude Code  
**Timeline:** Days 19-20

**Artifact: feature_importance.py**

```
Tasks:
├─ Analyze cluster centers from WEKA
│  ├─ Which dimensions vary most across clusters?
│  ├─ Calculate variance per dimension
│  ├─ Rank by importance
│  └─ Document findings
│
├─ Correlation analysis
│  ├─ Correlation between dimensions
│  ├─ Create correlation heatmap
│  └─ Identify relationships
│
├─ Cluster separation quality
│  ├─ Review WEKA silhouette coefficient
│  ├─ Evaluate cluster validity
│  └─ Document quality metrics
│
└─ Interpret clusters
   ├─ Describe each cluster's characteristics
   ├─ Identify best/worst clusters
   ├─ Document insights
   └─ Prepare for visualization

Output files:
├─ feature_importance.csv
├─ correlation_heatmap.png
├─ cluster_interpretation.txt
└─ weka_quality_metrics.txt
```

**OUTPUT OF PHASE 3:** cities_clustered_weka.csv with WEKA cluster assignments

---

## PHASE 4: VISUALIZATION & ANALYSIS (WEEK 3, DAYS 4-5)

### STEP 4.1: Create Interactive Folium Map

**Platform:** Claude Code  
**Timeline:** Days 20-21

**Artifact: visualize_map.py**

```
Tasks:
├─ Create base map (centered on world)
│  ├─ Center: (20, 0) - world center
│  ├─ Zoom: 2 (world view)
│  ├─ Tile style: OpenStreetMap
│  └─ Control: zoom, pan, fullscreen
│
├─ Add city markers
│  ├─ Color by cluster (5 distinct colors)
│  ├─ Size by population (optional)
│  ├─ Marker type: CircleMarker
│  └─ Coordinates: latitude, longitude
│
├─ Add heatmap layer (optional)
│  ├─ Opportunity score heatmap
│  ├─ Shows geographic distribution
│  ├─ Can toggle on/off
│  └─ Uses gradient colors
│
├─ Add popups per city
│  ├─ Click marker → see popup
│  ├─ Info: City name, country, cluster
│  ├─ Display: all 7 scores
│  ├─ Display: overall opportunity index
│  └─ Display: key metrics
│
├─ Add layer control
│  ├─ Toggle: cluster markers
│  ├─ Toggle: heatmap
│  ├─ Toggle: map tile styles
│  └─ Easy exploration
│
└─ Styling
   ├─ Cluster 1: #FFB6D9 (pastel pink)
   ├─ Cluster 2: #C8A2E8 (pastel purple)
   ├─ Cluster 3: #B4D7FF (pastel blue)
   ├─ Cluster 4: #FFE8B6 (pastel peach)
   ├─ Cluster 5: #B4FFD7 (pastel mint)
   └─ Match your Y2K aesthetic!

Python code (example):
import folium
from folium.plugins import HeatMap

map = folium.Map(location=[20, 0], zoom_start=2)

for idx, row in data.iterrows():
    colors = {0: '#FFB6D9', 1: '#C8A2E8', 2: '#B4D7FF', 
              3: '#FFE8B6', 4: '#B4FFD7'}
    color = colors[row['cluster']]
    
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=8,
        color=color,
        fill=True,
        fillColor=color,
        fillOpacity=0.7,
        popup=f"{row['city']}, {row['country']}<br>"
              f"Cluster: {row['cluster']}<br>"
              f"Opportunity: {row['opportunity_index']:.1f}/10"
    ).add_to(map)

map.save('gcoi_map.html')

Output file:
└─ gcoi_map_interactive.html (shareable!)
```

---

### STEP 4.2: Create Plotly Visualizations

**Platform:** Claude Code  
**Timeline:** Days 21-22

**Artifact: visualize_charts.py**

```
1️⃣ CLUSTER PROFILES (Radar Charts)
├─ For each cluster: 1 radar chart
├─ Axes: 7 dimensions
├─ Value: average score per dimension
├─ 5 subplots (one per cluster)
├─ Shows cluster characteristics
└─ Output: cluster_profiles_radar.html

2️⃣ SCATTER PLOTS (2D Visualizations)
├─ Affordability vs Opportunity
│  ├─ X: affordability_score
│  ├─ Y: opportunity_index
│  ├─ Color: cluster
│  ├─ Size: population
│  └─ Shows: value for money
│
├─ Innovation vs Talent
│  ├─ X: innovation_score
│  ├─ Y: talent_score
│  ├─ Color: cluster
│  └─ Shows: innovation ecosystem maturity
│
└─ Startup Growth vs Digital
   ├─ X: digital_score
   ├─ Y: startup_score
   ├─ Color: growth_score
   └─ Shows: tech ecosystem readiness

3️⃣ BOX PLOTS (Distribution per Cluster)
├─ For each dimension: 1 box plot
├─ 5 boxes (one per cluster)
├─ Shows: range and distribution
├─ Identifies outliers
└─ 7 subplots total

4️⃣ BAR CHARTS (Rankings)
├─ Top 10 cities by opportunity_index
├─ Top 10 by affordability
├─ Top 10 by startup opportunity
├─ Top 10 by innovation
├─ Color by cluster
└─ Easy to read rankings

5️⃣ HEATMAP (Correlation Matrix)
├─ Correlation between all dimensions
├─ Color intensity: strength
├─ Shows: which factors related?
└─ Identify multicollinearity

6️⃣ TIME SERIES (Growth Trajectory)
├─ If historical data available
├─ X: year (2014-2024)
├─ Y: opportunity index (or dimension)
├─ Separate lines per cluster
├─ Shows: how clusters evolving
└─ Trend lines

Output files:
├─ cluster_profiles_radar.html
├─ afford_vs_opportunity.html
├─ innovation_vs_talent.html
├─ startup_vs_digital.html
├─ dimension_distributions.html
├─ top_cities_rankings.html
├─ correlation_heatmap.html
└─ growth_trajectories.html (if historical)
```

---

### STEP 4.3: Generate Analysis Report

**Platform:** Claude Code  
**Timeline:** Days 22-23

**Artifact: generate_report.py**

```
Tasks:
├─ Create executive summary
│  ├─ Key findings (3-5 main insights)
│  ├─ Methodology overview
│  ├─ 7 dimensions explanation
│  └─ Cluster interpretation
│
├─ Cluster analysis detailed
│  ├─ For each cluster:
│  │  ├─ Cluster name (e.g., "Established Hubs")
│  │  ├─ Characteristics
│  │  ├─ Cities in cluster
│  │  ├─ Strengths
│  │  ├─ Weaknesses
│  │  ├─ Best for (who should move here?)
│  │  └─ Opportunities
│  └─ Cross-cluster comparisons
│
├─ City-specific insights
│  ├─ Top 10 cities by opportunity
│  ├─ Best value cities (high opportunity, low cost)
│  ├─ Rising stars (high growth potential)
│  ├─ Challenges & opportunities per city
│  └─ Recommendations per city
│
├─ Dimension deep-dives
│  ├─ For each of 7 dimensions:
│  │  ├─ Which cities score highest?
│  │  ├─ Which need improvement?
│  │  ├─ Regional variations
│  │  ├─ Trends & predictions
│  │  └─ Recommendations for improvement
│  └─ Interdependencies (which factors co-occur?)
│
├─ Regional analysis
│  ├─ Asia-Pacific: strongest/weakest
│  ├─ Europe: trends & patterns
│  ├─ Americas: emerging opportunities
│  └─ Regional comparisons
│
├─ Future outlook
│  ├─ Which clusters will grow?
│  ├─ Emerging opportunities
│  ├─ Risk factors & challenges
│  ├─ 2030 predictions
│  └─ Investment implications
│
└─ Methodology & caveats
   ├─ Data sources (list all)
   ├─ Data quality (completeness %)
   ├─ Feature definitions
   ├─ Weighting rationale
   ├─ Clustering approach
   ├─ Limitations
   └─ Future improvements

Output formats:
├─ Markdown report (for GitHub)
├─ PDF report (for sharing)
└─ HTML report (interactive, with embedded charts)
```

**OUTPUT OF PHASE 4:** All visualizations + reports

---

## PHASE 5: INTERACTIVE DASHBOARD (WEEK 4, DAYS 1-3)

### STEP 5.1: Build Streamlit App Structure

**Platform:** Claude Code + Streamlit Cloud  
**Timeline:** Days 24-26

**Artifact: streamlit_app.py (MAIN DELIVERABLE)**

```python
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="GCOI Index 2024-2030",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# SIDEBAR - FILTERS & CONTROLS
# ============================================
st.sidebar.title("🎛️ Controls")
st.sidebar.markdown("---")

# Filter 1: Cluster selection
selected_clusters = st.sidebar.multiselect(
    "Filter by Cluster",
    [0, 1, 2, 3, 4],
    default=[0, 1, 2, 3, 4]
)

# Filter 2: Region selection
selected_regions = st.sidebar.multiselect(
    "Filter by Region",
    data['region'].unique(),
    default=data['region'].unique()
)

# Filter 3: Opportunity score range
afford_range = st.sidebar.slider(
    "Affordability Score Range",
    0.0, 10.0, (0.0, 10.0)
)

# Filter 4: Dimension to highlight
highlight_dim = st.sidebar.selectbox(
    "Highlight Dimension",
    ["Opportunity Index", "Affordability", "Digital", "Startup", 
     "Urban", "Innovation", "Talent", "Growth"]
)

# Apply filters
filtered_data = data[
    (data['cluster'].isin(selected_clusters)) &
    (data['region'].isin(selected_regions)) &
    (data['affordability_score'] >= afford_range[0]) &
    (data['affordability_score'] <= afford_range[1])
]

# ============================================
# MAIN CONTENT PAGES
# ============================================

pages = {
    "🏠 Overview": "overview",
    "📍 City Map": "map",
    "📊 Clusters": "clusters",
    "🔍 Dimensions": "dimensions",
    "🔄 Compare": "compare",
    "🚀 Insights": "insights",
    "📖 About": "about"
}

page = st.sidebar.radio("Select Page", pages.keys())

if page == "🏠 Overview":
    st.title("🌍 Global City Opportunity & Innovation Index 2024-2030")
    st.markdown("""
        Data-driven analysis of 50+ global cities across 7 key dimensions.
        Find where to build, invest, or move.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Cities", len(data))
    col2.metric("Clusters Found", data['cluster'].nunique())
    col3.metric("Avg Opportunity", f"{data['opportunity_index'].mean():.1f}/10")
    col4.metric("Data Sources", 15)
    
    st.markdown("---")
    st.subheader("Cluster Summary")
    cluster_summary = data.groupby('cluster').agg({
        'opportunity_index': 'mean',
        'affordability_score': 'mean',
        'startup_score': 'mean',
        'innovation_score': 'mean'
    }).round(1)
    st.dataframe(cluster_summary)

elif page == "📍 City Map":
    st.subheader("📍 City Intelligence Map")
    
    map = folium.Map(location=[20, 0], zoom_start=2)
    
    for idx, row in filtered_data.iterrows():
        colors = {0: '#FFB6D9', 1: '#C8A2E8', 2: '#B4D7FF', 
                  3: '#FFE8B6', 4: '#B4FFD7'}
        color = colors[row['cluster']]
        
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=8,
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.7,
            popup=f"{row['city']}, {row['country']}<br>"
                  f"Cluster: {row['cluster']}<br>"
                  f"Opportunity: {row['opportunity_index']:.1f}/10"
        ).add_to(map)
    
    st_folium(map, width=1400, height=600)
    
    st.markdown("""
    **Cluster Colors:**
    - 🎀 Pink: Established Hubs
    - 💜 Purple: Rising Stars
    - 💙 Blue: Affordable Emerging
    - 🧡 Peach: Balanced Development
    - 💚 Mint: Unique Profile
    """)

elif page == "📊 Clusters":
    st.subheader("📊 Cluster Analysis")
    
    selected_cluster = st.selectbox(
        "Select Cluster",
        range(5),
        format_func=lambda x: f"Cluster {x}"
    )
    
    cluster_data = data[data['cluster'] == selected_cluster]
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"### Cluster {selected_cluster} Profile")
        st.metric("Cities in Cluster", len(cluster_data))
        st.metric("Avg Opportunity", f"{cluster_data['opportunity_index'].mean():.1f}")
    
    st.write("### Cities in This Cluster")
    st.dataframe(cluster_data[['city', 'country', 'opportunity_index', 
                                'affordability_score', 'startup_score']])

elif page == "🔍 Dimensions":
    st.subheader("🔍 Dimension Analysis")
    
    selected_dim = st.selectbox(
        "Select Dimension",
        ["Affordability", "Digital", "Startup", 
         "Urban", "Innovation", "Talent", "Growth"]
    )
    
    dim_col = f'{selected_dim.lower()}_score'
    top_cities = data.nlargest(10, dim_col)
    
    fig = px.bar(top_cities, x=dim_col, y='city', 
                 color='cluster', 
                 title=f"Top 10 Cities - {selected_dim}")
    st.plotly_chart(fig)
    
    st.write("### Regional Comparison")
    regional_data = data.groupby('region')[dim_col].mean()
    st.bar_chart(regional_data)

elif page == "🔄 Compare":
    st.subheader("🔄 City Comparison Tool")
    
    cities_to_compare = st.multiselect(
        "Select 2-5 cities to compare",
        data['city'].unique(),
        default=['Bangkok', 'Lisbon', 'Jakarta']
    )
    
    comparison_data = data[data['city'].isin(cities_to_compare)]
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.scatter(comparison_data, 
                          x='affordability_score', 
                          y='opportunity_index',
                          text='city',
                          title="Affordability vs Opportunity")
        st.plotly_chart(fig1)
    
    with col2:
        fig2 = px.scatter(comparison_data,
                          x='digital_score',
                          y='startup_score',
                          text='city',
                          title="Digital vs Startup")
        st.plotly_chart(fig2)
    
    st.dataframe(comparison_data[['city', 'cluster', 'opportunity_index',
                                  'affordability_score', 'digital_score']])

elif page == "🚀 Insights":
    st.subheader("🚀 Key Insights & Predictions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("💰 Best Value")
        best_value = data.nlargest(3, 'opportunity_index').nsmallest(3, 'affordability_score')
        for idx, row in best_value.iterrows():
            st.write(f"**{row['city']}**")
            st.write(f"Score: {row['opportunity_index']:.1f}/10")
    
    with col2:
        st.subheader("📈 Rising Stars")
        rising = data.nlargest(3, 'growth_score')
        for idx, row in rising.iterrows():
            st.write(f"**{row['city']}**")
            st.write(f"Growth: {row['growth_score']:.1f}/10")
    
    with col3:
        st.subheader("🚀 Most Innovative")
        innovative = data.nlargest(3, 'innovation_score')
        for idx, row in innovative.iterrows():
            st.write(f"**{row['city']}**")
            st.write(f"Score: {row['innovation_score']:.1f}/10")
    
    st.write("### Key Findings")
    findings = [
        "✅ Best Value Cities: Lisbon, Bangkok, Jakarta",
        "✅ Innovation Hubs: San Francisco, Shenzhen, London",
        "✅ Rising Opportunities: Emerging Asian cities",
        "✅ Growth Leaders: High growth potential identified",
        "✅ Digital Future: Infrastructure gaps closing"
    ]
    for finding in findings:
        st.write(finding)

elif page == "📖 About":
    st.subheader("📖 About This Project")
    
    st.write("""
    ### Overview
    Analysis of 7 dimensions across 50+ global cities:
    1. Affordability & Livability
    2. Digital Infrastructure
    3. Startup Ecosystem
    4. Urban Development
    5. Innovation Readiness
    6. Talent & Human Capital
    7. Future Trajectory
    
    ### Data Sources
    15+ global data sources integrated
    
    ### Methodology
    - Data collection & cleaning
    - Feature engineering with weighted scoring
    - K-means clustering (K=5)
    - Statistical analysis
    - Interactive visualization
    
    ### Author
    Alma - Informatics Student @ UII, Nanjing Xiaozhuang University
    """)
    
    st.markdown("---")
    st.write("📊 Last Updated: January 2025")
    st.write("🔗 GitHub: [project-repo-link]")
```

**Output:**
- streamlit_app.py (fully functional dashboard)

---

### STEP 5.2: Deploy to Streamlit Cloud

**Platform:** Streamlit Cloud  
**Timeline:** Days 26-27

```
Tasks:
├─ Create requirements.txt
│  ├─ streamlit==1.28.0
│  ├─ pandas==2.0.0
│  ├─ folium==0.14.0
│  ├─ plotly==5.17.0
│  ├─ scikit-learn==1.3.0
│  ├─ geopy==2.3.0
│  ├─ numpy==1.24.0
│  └─ requests==2.31.0
│
├─ Create .gitignore
│  ├─ __pycache__/
│  ├─ *.pyc
│  ├─ .env
│  ├─ /data/raw
│  └─ /.streamlit/secrets.toml
│
├─ Initialize Git repository
│  ├─ git init
│  ├─ git add .
│  ├─ git commit -m "Initial: GCOI Index"
│  └─ git push to GitHub
│
├─ Deploy to Streamlit Cloud
│  ├─ Go to: https://share.streamlit.io/
│  ├─ Connect GitHub repo
│  ├─ Select branch + file
│  ├─ Deploy
│  └─ Live URL: https://your-username-gcoi.streamlit.app
│
└─ Test deployment
   ├─ Open live URL
   ├─ Test all pages
   ├─ Check filters
   └─ Performance testing
```

**OUTPUT OF PHASE 5:** Live Streamlit dashboard

---

## PHASE 6: DOCUMENTATION & FINALIZATION (WEEK 4, DAYS 4-7)

### STEP 6.1: Create Documentation

**Platform:** Claude Code + Markdown/PDF  
**Timeline:** Days 28-30

```
Files to create:

1️⃣ README.md
├─ Project overview
├─ Quick start guide
├─ Features overview
├─ Installation
├─ Usage examples
├─ Dashboard link
├─ Contributing
└─ License

2️⃣ METHODOLOGY.md
├─ Data sources
├─ Feature definitions
├─ Normalization approach
├─ Weighting rationale
├─ Clustering methodology
├─ Limitations
└─ Future improvements

3️⃣ DATA_SOURCES.md
├─ All 15+ sources
├─ Access methods
├─ API documentation
├─ Data collection scripts
├─ Quality notes
└─ Update frequency

4️⃣ FINDINGS.md
├─ Executive summary
├─ Cluster descriptions
├─ Top cities analysis
├─ Regional insights
├─ Trends & predictions
└─ Recommendations

5️⃣ CODE_STRUCTURE.md
├─ Project structure
├─ How to run scripts
├─ Data pipeline flow
├─ How to extend
└─ Testing procedures

6️⃣ DEPLOYMENT.md
├─ Streamlit Cloud setup
├─ GitHub setup
├─ Environment variables
├─ Troubleshooting
└─ Maintenance

Output files (in /docs):
├─ README.md
├─ METHODOLOGY.md
├─ DATA_SOURCES.md
├─ FINDINGS.md
├─ CODE_STRUCTURE.md
├─ DEPLOYMENT.md
└─ ANALYSIS_REPORT.pdf
```

---

### STEP 6.2: Create Final Datasets & Exports

**Platform:** Claude Code  
**Timeline:** Days 30-31

**Artifact: prepare_final_outputs.py**

```
Tasks:
├─ Export main dataset
│  ├─ cities_gcoi_index_final.csv
│  ├─ All 7 scores + metadata
│  ├─ Clean columns
│  └─ Ready for external use
│
├─ Export cluster assignments
│  ├─ cities_clusters.csv
│  ├─ Cluster ID, name, characteristics
│  └─ Cities grouped by cluster
│
├─ Export cluster profiles
│  ├─ cluster_profiles.csv
│  ├─ Mean values per cluster
│  ├─ Statistical summaries
│  └─ Cluster descriptions
│
├─ Export feature correlations
│  ├─ feature_correlations.csv
│  ├─ Correlation matrix
│  └─ Statistical significance
│
├─ Generate PDF report
│  ├─ Executive summary
│  ├─ Methodology
│  ├─ Key findings
│  ├─ Visualizations
│  └─ Cluster analysis
│
└─ Create data dictionary
   ├─ Column definitions
   ├─ Unit explanations
   ├─ Data sources
   ├─ Quality notes
   └─ Usage guidelines

Output files in /data/final:
├─ cities_gcoi_index_final.csv
├─ cities_clusters.csv
├─ cluster_profiles.csv
├─ feature_analysis.csv
├─ GCOI_Analysis_Report.pdf
└─ Data_Dictionary.txt
```

---

### STEP 6.3: Code Review & Optimization

**Platform:** Claude Code  
**Timeline:** Days 31-32

```
Tasks:
├─ Code quality check
│  ├─ Consistent naming
│  ├─ Proper docstrings
│  ├─ Type hints
│  ├─ Remove dead code
│  └─ Refactor complex sections
│
├─ Performance optimization
│  ├─ Vectorize operations
│  ├─ Cache expensive computations
│  ├─ Streamlit caching (@st.cache_data)
│  └─ Database indexing
│
├─ Error handling
│  ├─ Try-except blocks
│  ├─ Graceful failures
│  ├─ User-friendly messages
│  └─ Logging for debugging
│
├─ Testing
│  ├─ Manual testing all scripts
│  ├─ Edge case testing
│  ├─ Data validation
│  ├─ Dashboard testing
│  └─ Performance benchmarking
│
└─ Final cleanup
   ├─ Remove debug prints
   ├─ Clean commented code
   ├─ Update documentation
   ├─ Final version of files
   └─ Commit to GitHub
```

---

## ✅ COMPLETE DELIVERABLES CHECKLIST

```
PHASE 1: DATA COLLECTION ✅
└─ 15+ raw CSV files in /data/raw/

PHASE 2: PREPROCESSING ✅
└─ cities_features.csv (normalized, engineered)

PHASE 3: CLUSTERING ✅
├─ cities_clustered.csv (with cluster assignments)
├─ elbow_curve.png (optimal K visualization)
├─ cluster_metrics.txt (quality metrics)
└─ cluster_profiles.csv (mean values per cluster)

PHASE 4: VISUALIZATION ✅
├─ gcoi_map_interactive.html (Folium map)
├─ cluster_profiles_radar.html (radar charts)
├─ afford_vs_opportunity.html (scatter)
├─ innovation_vs_talent.html (scatter)
├─ top_cities_rankings.html (bar charts)
├─ correlation_heatmap.html (heatmap)
├─ dimension_distributions.html (box plots)
└─ growth_trajectories.html (time series)

PHASE 5: DASHBOARD ✅
├─ streamlit_app.py (fully functional)
├─ requirements.txt (dependencies)
├─ .gitignore (repo management)
├─ GitHub repo (public, documented)
└─ Live Streamlit URL (https://...)

PHASE 6: DOCUMENTATION ✅
├─ README.md (overview & quick start)
├─ METHODOLOGY.md (technical details)
├─ DATA_SOURCES.md (all source documentation)
├─ FINDINGS.md (key insights & analysis)
├─ CODE_STRUCTURE.md (developer guide)
├─ DEPLOYMENT.md (how to run & deploy)
├─ Data_Dictionary.txt (column definitions)
└─ GCOI_Analysis_Report.pdf (comprehensive)

FINAL DATASETS ✅
├─ cities_gcoi_index_final.csv (main dataset)
├─ cities_clusters.csv (cluster assignments)
├─ cluster_profiles.csv (statistical summaries)
└─ feature_analysis.csv (importance & correlation)
```

---

## 🛠️ TOOLS & PLATFORMS REQUIRED

```
CLAUDE CODE (Python Scripts):
├─ Script 01: Data Collection
├─ Script 02: Data Preprocessing
├─ Script 03: Feature Engineering
├─ Script 04: ARFF Conversion (for WEKA)
├─ Script 05: Import WEKA results
├─ Script 06: Visualizations (Folium + Plotly)
└─ Script 07: Streamlit Dashboard

⭐ WEKA DESKTOP APPLICATION (MANDATORY FOR DATA MINING):
├─ Download: https://www.cs.waikato.ac.nz/ml/weka/
├─ Load: cities.arff file
├─ Run: SimpleKMeans clustering
├─ Export: Cluster assignments & results
└─ Requirements: Java installed

EXTERNAL PLATFORMS (For Deployment):
├─ GitHub (host repository)
├─ Streamlit Cloud (deploy dashboard)
├─ Kaggle (download Crunchbase data)
└─ APIs (Crunchbase, AngelList, World Bank, etc.)

PYTHON LIBRARIES:
├─ pandas, numpy (data)
├─ matplotlib, seaborn (plotting)
├─ plotly (interactive charts)
├─ folium (maps)
├─ streamlit (dashboard)
├─ requests, beautifulsoup4 (web scraping)
├─ geopy (geocoding)
└─ wbdata (World Bank API)

CRITICAL REQUIREMENTS:
✅ WEKA MUST BE INSTALLED - this is graded
✅ Phase 3 clustering MUST use WEKA SimpleKMeans
✅ ARFF file format required for WEKA
✅ Results must be exported from WEKA
✅ Documentation must show WEKA usage & outputs
```

---

## 📊 DATA STRUCTURE (Final CSV)

### Columns in cities_gcoi_index_final.csv:

```
IDENTIFIERS:
├─ city (string)
├─ country (string)
├─ region (string)
├─ latitude (float)
└─ longitude (float)

DIMENSION 1: AFFORDABILITY (0-10)
├─ housing_cost_usd (numeric)
├─ cost_of_living_index (numeric)
├─ avg_salary_usd (numeric)
├─ salary_to_col_ratio (numeric)
└─ affordability_score (0-10)

DIMENSION 2: DIGITAL (0-10)
├─ internet_speed_mbps (numeric)
├─ internet_penetration_pct (numeric)
├─ 5g_coverage_pct (numeric)
├─ smartphone_penetration_pct (numeric)
└─ digital_score (0-10)

DIMENSION 3: STARTUP (0-10)
├─ startup_count (numeric)
├─ total_funding_usd (numeric)
├─ avg_funding_per_startup (numeric)
├─ startup_growth_rate_pct (numeric)
├─ tech_jobs_count (numeric)
└─ startup_score (0-10)

DIMENSION 4: URBAN (0-10)
├─ road_density (numeric)
├─ population_density (numeric)
├─ sprawl_index (numeric)
├─ infrastructure_quality (0-10)
└─ urban_score (0-10)

DIMENSION 5: INNOVATION (0-10)
├─ patents_count (numeric)
├─ patent_density (numeric)
├─ university_quality_score (numeric)
├─ research_publications (numeric)
└─ innovation_score (0-10)

DIMENSION 6: TALENT (0-10)
├─ education_quality_index (numeric)
├─ tech_talent_concentration (numeric)
├─ immigration_friendliness (numeric)
├─ brain_drain_index (numeric, inverted)
└─ talent_score (0-10)

DIMENSION 7: GROWTH (0-10)
├─ historical_growth_rate_5yr (numeric)
├─ current_growth_trajectory (numeric)
├─ growth_potential (numeric)
└─ growth_score (0-10)

COMPOSITE:
├─ opportunity_index (0-10)
└─ data_quality_score (0-100)

CLUSTERING:
├─ cluster (0-4)
└─ cluster_name (string)
```

---

## ⏱️ REALISTIC TIMELINE & WORKLOAD

```
WEEK 1: DATA COLLECTION
├─ Day 1: Setup + Affordability data
├─ Day 2: Digital infrastructure
├─ Day 3: Startup ecosystem
├─ Day 4: Urban development
├─ Day 5: Innovation & research
├─ Day 6: Talent & education
├─ Day 7: Historical trends
└─ Effort: 5-6 hours/day, moderate intensity

WEEK 2: PREPROCESSING & FEATURES
├─ Day 8: Data cleaning & validation
├─ Day 9: Data merging
├─ Day 10-11: Feature engineering (7 scores)
├─ Day 12-13: Historical analysis & metadata
├─ Day 14: Quality assurance
└─ Effort: 4-5 hours/day, moderate-high intensity

WEEK 3: CLUSTERING & VISUALIZATION
├─ Day 15: Normalization + optimal K finding
├─ Day 16: K-means clustering + metrics
├─ Day 17: Feature importance analysis
├─ Day 18-19: Create Folium map
├─ Day 20-21: Create Plotly visualizations
└─ Effort: 5-6 hours/day, high intensity

WEEK 4: DASHBOARD & FINALIZATION
├─ Day 22-24: Build Streamlit dashboard (7 pages)
├─ Day 25-26: Deploy to Streamlit Cloud + testing
├─ Day 27-30: Documentation & final exports
├─ Day 31-32: Code review & optimization
└─ Effort: 6-7 hours/day, high intensity

TOTAL TIME: ~150-170 hours over 4 weeks
PACE: ~40 hours/week (manageable alongside studies)
```

---

## ✨ SUCCESS CRITERIA

```
PROJECT COMPLETE WHEN YOU HAVE:

✅ PHASE 1: Complete dataset from 15+ sources
   └─ All 7 dimensions populated
   └─ 50-70 cities analyzed
   └─ Data quality >85%

✅ PHASE 2: Clean, engineered features
   └─ All metrics normalized (0-10)
   └─ No missing values
   └─ Feature correlations analyzed

✅ PHASE 3: Optimal clustering model
   └─ K=5 (or justified alternative)
   └─ Silhouette score >0.4
   └─ Interpretable clusters

✅ PHASE 4: Professional visualizations
   └─ Interactive Folium map
   └─ 8+ Plotly charts
   └─ Comprehensive analysis report

✅ PHASE 5: Live deployed dashboard
   └─ 7 functional pages
   └─ All filters working
   └─ Mobile-responsive
   └─ Publicly shareable URL

✅ PHASE 6: Complete documentation
   └─ 6+ documentation files
   └─ Code is well-commented
   └─ Methodology clearly explained
   └─ Data dictionary provided

✅ PORTFOLIO READY:
   └─ GitHub repo with clean code
   └─ Live dashboard to share
   └─ Comprehensive analysis report
   └─ Shareable with employers/competitions
```

---

## 🚀 AFTER PROJECT COMPLETION (Optional Extensions)

```
1️⃣ EXTENSION: Interactive Tool
   └─ User inputs preferences → get city recommendations
   └─ "Where should I move?" quiz
   └─ Personalized scoring

2️⃣ EXTENSION: Time-Series Predictions
   └─ Forecast future scores for each city
   └─ Predict cluster movements
   └─ "Which cities will be #1 by 2030?"

3️⃣ EXTENSION: API Development
   └─ REST API for GCOI Index data
   └─ Public API for external use
   └─ Allow community contributions

4️⃣ EXTENSION: Academic Paper
   └─ Write & publish methodology paper
   └─ Submit to conference
   └─ Career advancement

5️⃣ EXTENSION: Commercial Version
   └─ Subscription-based detailed reports
   └─ Corporate/investor dashboard
   └─ Monetize insights
```

---

## 📞 SUPPORT & RESOURCES

```
REFERENCE MATERIALS:
├─ Scikit-learn: https://scikit-learn.org/
├─ Streamlit: https://docs.streamlit.io/
├─ Pandas: https://pandas.pydata.org/
├─ Folium: https://folium.readthedocs.io/
├─ Plotly: https://plotly.com/python/
└─ World Bank API: https://datahelpdesk.worldbank.org/

TROUBLESHOOTING:
├─ API rate limiting → add delays, cache results
├─ Missing data → log source, consider imputation
├─ Slow Streamlit → use @st.cache_data decorator
├─ Deployment issues → check requirements.txt

BEST PRACTICES:
├─ Commit frequently to GitHub
├─ Document as you go
├─ Test each script before moving on
├─ Keep backup of data files
└─ Regular quality assurance checks
```

---

## 📋 SUMMARY

```
PROJECT: Global City Opportunity & Innovation Index 2024-2030
SCOPE: 50-70 cities, 7 dimensions, 15+ data sources
TYPE: Full-stack data engineering + interactive analytics + DATA MINING
TIMELINE: 4 weeks
DELIVERABLE: Live Streamlit dashboard + analysis report + WEKA clustering
TECH: Python (Claude Code) + WEKA (Data Mining) + Folium + Plotly + Streamlit
DEPLOYMENT: Streamlit Cloud (FREE)
PORTFOLIO VALUE: ⭐⭐⭐⭐⭐ (Highly impressive)

⭐ WEKA MANDATORY - Phase 3 Clustering with WEKA SimpleKMeans
✅ Data collection & preprocessing in Claude Code
✅ Data exported to WEKA ARFF format
✅ Clustering performed in WEKA Desktop App
✅ Results imported back to Python
✅ Visualizations & dashboard in Streamlit
✅ Beautiful interactive dashboard - shareable URL
✅ Comprehensive documentation - professional quality
✅ Competition-ready - suitable for GEMASTIK, tech challenges
```

---

**READY TO START?**

Begin with **PHASE 1, STEP 1.1** (Set Up Environment) or whichever step you prefer!

Let me know when you're ready and we'll build it! 🚀