# 📊 GCOI INDEX - DATA SOURCES (NO SCRAPING! DATASETS ONLY)

Ini adalah guide lengkap semua dataset yang sudah ready-made. **TIDAK PERLU WEB SCRAPING!**

---

## DIMENSION 1: AFFORDABILITY & LIVABILITY

### ✅ DATASET AVAILABLE: Cost of Living + Salary Data

#### Option 1: Kaggle - Cost of Living Dataset
**Link:** https://www.kaggle.com/datasets/mvieira101/global-cost-of-living

**What's included:**
- City names
- Country
- Rent prices (1-room apartment)
- Housing prices
- Food costs
- Transportation
- Utilities
- Average salary
- Cost of living index

**How to download:**
1. Go to link above
2. Click "Download" button (top right)
3. Unzip file
4. Use CSV: `cost_of_living.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 2: Kaggle - Glassdoor Salary Data
**Link:** https://www.kaggle.com/datasets/zinovyev/glassdoor-salary

**What's included:**
- Job title
- Salary
- City
- Country
- Company
- Industry
- Experience level

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `glassdoor_data.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 3: World Bank - Economic Indicators API (NO DOWNLOAD NEEDED)
**Link:** https://data.worldbank.org/

**Available via API (FREE):**
- GDP per capita
- Gini coefficient (inequality)
- Healthcare spending
- Education enrollment
- Urban population %

**How to use:**
```python
import wbdata
import pandas as pd

# Get GDP per capita
gdp_data = wbdata.get_dataframe({"NY.GDP.PCAP.CD": "gdp_per_capita"})

# Get multiple indicators at once
indicators = {
    'NY.GDP.PCAP.CD': 'gdp_per_capita',
    'SI.POV.GINI': 'gini_coefficient',
    'SP.DYN.LE00.IN': 'life_expectancy'
}
data = wbdata.get_dataframe(indicators)
```

**Status:** ✅ FREE, ✅ API (NO SCRAPING)

---

### 📥 HOW TO GET DIMENSION 1 DATA:

```
STEP 1: Download from Kaggle
├─ Cost of Living Dataset
├─ Glassdoor Salary Data
└─ Total size: ~50 MB

STEP 2: Get World Bank data via API
├─ GDP per capita
├─ Gini coefficient
├─ Healthcare/education metrics
└─ No download, direct API call

STEP 3: Combine in Python
├─ Load CSVs with pandas
├─ Merge by city/country
├─ Add World Bank data
└─ Output: affordability_dimension_data.csv
```

**Total collection time:** 1 hour
**Difficulty:** ⭐ (Just download + merge)

---

## DIMENSION 2: DIGITAL INFRASTRUCTURE

### ✅ DATASET AVAILABLE: Internet Speed + Connectivity

#### Option 1: Kaggle - Internet Speed by Country
**Link:** https://www.kaggle.com/datasets/taruntiwarihp/internet-speed-by-country

**What's included:**
- Country
- Download speed (Mbps)
- Upload speed (Mbps)
- Ping (latency)
- Year

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `internet_speed.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 2: Kaggle - Global Internet Users Dataset
**Link:** https://www.kaggle.com/datasets/aliashraf/global-internet-users

**What's included:**
- Country/Region
- Year
- Internet users count
- Internet penetration %
- Population

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `internet_users.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 3: Kaggle - Tech Jobs by Location
**Link:** https://www.kaggle.com/datasets/PromptCloudHQ/tech-jobs-on-dice

**What's included:**
- Job location (city, state)
- Job title
- Skills required
- Salary range
- Date posted

**How to download:**
1. Go to link above
2. Click "Download"
3. Filter by city → count tech jobs per city

**Status:** ✅ FREE, ✅ READY TO USE

---

### 📥 HOW TO GET DIMENSION 2 DATA:

```
STEP 1: Download from Kaggle (total ~100 MB)
├─ Internet Speed Dataset
├─ Internet Users Dataset
└─ Tech Jobs Dataset

STEP 2: Process in Python
├─ Load CSVs
├─ Group by city/country
├─ Calculate:
│  ├─ Avg internet speed
│  ├─ Internet penetration %
│  └─ Tech job count
└─ Output: digital_dimension_data.csv

STEP 3: No APIs needed!
└─ All data in Kaggle datasets
```

**Total collection time:** 2 hours
**Difficulty:** ⭐ (Download + filter + aggregate)

---

## DIMENSION 3: STARTUP ECOSYSTEM

### ✅ DATASET AVAILABLE: Crunchbase Startups

#### Option 1: Kaggle - Crunchbase Companies Dataset
**Link:** https://www.kaggle.com/datasets/mgmarques/crunchbase-companies

**What's included:**
- Company name
- Founding year
- Headquarters location (city, country)
- Funding amount ($)
- Funding rounds count
- Industry/category
- Status (active, acquired, closed)

**How to download:**
1. Go to link above
2. Click "Download" (may need Kaggle account)
3. Use CSV: `companies.csv`

**Size:** ~500 MB (large but complete!)

**Status:** ✅ FREE, ✅ READY TO USE, ✅ MOST IMPORTANT!

---

#### Option 2: Alternative - Kaggle Startup Funding Dataset
**Link:** https://www.kaggle.com/datasets/PromptCloudHQ/us-startup-funding-data

**What's included:**
- Company name
- City
- Funding amount
- Funding rounds
- Founded year
- Industry

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `startup_data.csv`

**Status:** ✅ FREE, ✅ SMALLER ALTERNATIVE (if Crunchbase too large)

---

### 📥 HOW TO GET DIMENSION 3 DATA:

```
STEP 1: Download Crunchbase Dataset
├─ Go to Kaggle link
├─ Click Download
└─ File: companies.csv (~500 MB)

STEP 2: Process in Python
├─ Load CSV
├─ Filter by founding year (2014-2024) for growth analysis
├─ Group by city:
│  ├─ Count startups
│  ├─ Sum funding
│  ├─ Avg funding per startup
│  └─ Calculate growth rate
└─ Output: startup_dimension_data.csv

STEP 3: Done!
└─ No scraping, no APIs, just dataset!
```

**Total collection time:** 3-4 hours (dataset is big)
**Difficulty:** ⭐⭐ (Large dataset, need to filter/aggregate)

---

## DIMENSION 4: URBAN DEVELOPMENT

### ✅ DATASET AVAILABLE: Population + City Data

#### Option 1: Kaggle - World Cities Dataset
**Link:** https://www.kaggle.com/datasets/max-mind/world-cities-database

**What's included:**
- City name
- Country
- Latitude/longitude
- Population
- Area (km²)
- Elevation

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `world_cities.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 2: Kaggle - City Temperature & Climate Data
**Link:** https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities

**What's included:**
- City
- Country
- Date
- Avg temperature
- Min temperature
- Max temperature

**Can infer:** Urban heat, climate patterns

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 3: World Bank - Urban Data API (FREE)
**Link:** https://data.worldbank.org/

**Available via API:**
- Urban population %
- City growth rate
- Infrastructure investment
- Electricity access

**How to use:**
```python
import wbdata

indicators = {
    'SP.URB.TOTL.IN.ZS': 'urban_population_pct',
    'SP.POP.GROW': 'population_growth_rate',
    'EG.ELC.ACCS.ZS': 'electricity_access_pct'
}

urban_data = wbdata.get_dataframe(indicators)
```

**Status:** ✅ FREE, ✅ API

---

### 📥 HOW TO GET DIMENSION 4 DATA:

```
STEP 1: Download Kaggle Datasets
├─ World Cities Database
└─ City Temperature Data

STEP 2: Get World Bank API
├─ Urban population %
├─ Growth rate
└─ Infrastructure metrics

STEP 3: Process in Python
├─ Load world_cities.csv
├─ Calculate:
│  ├─ Population density (pop/area)
│  ├─ City size classification
│  ├─ Urbanization level
│  └─ Growth trajectory
└─ Output: urban_dimension_data.csv
```

**Total collection time:** 2-3 hours
**Difficulty:** ⭐⭐ (Download + calculate density metrics)

---

## DIMENSION 5: INNOVATION READINESS

### ✅ DATASET AVAILABLE: Patents + University Rankings

#### Option 1: Kaggle - Patent Dataset
**Link:** https://www.kaggle.com/datasets/trainingdatasus/patent-data

**What's included:**
- Patent ID
- Inventor location (city, country)
- Filing date
- Grant date
- Technology category
- Citation count

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `patent_data.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 2: Kaggle - University Rankings Dataset
**Link:** https://www.kaggle.com/datasets/mylesoneill/world-university-rankings

**What's included:**
- University name
- Country
- City (sometimes)
- Rank
- Research score
- International score
- Teaching score

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `university_rankings.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 3: Kaggle - Research Papers Dataset
**Link:** https://www.kaggle.com/datasets/Cornell-University/arxiv

**What's included:**
- Paper title
- Authors + affiliations (includes city/country)
- Publication date
- Citations
- Category

**Status:** ✅ FREE, ✅ LARGE (~3 GB)

---

### 📥 HOW TO GET DIMENSION 5 DATA:

```
STEP 1: Download Kaggle Datasets
├─ Patent Data
├─ University Rankings
└─ Research Papers (optional, large)

STEP 2: Process in Python
├─ Load patent_data.csv
├─ Group by city:
│  ├─ Count patents
│  ├─ Calculate density (per capita)
│  └─ Technology focus
│
├─ Load university_rankings.csv
├─ Group by city:
│  ├─ Count universities
│  ├─ Average rank
│  └─ Research score

STEP 3: Combine
├─ Merge patent + university data by city
└─ Output: innovation_dimension_data.csv
```

**Total collection time:** 3-4 hours (patents dataset is large)
**Difficulty:** ⭐⭐ (Large dataset, need aggregation)

---

## DIMENSION 6: TALENT & HUMAN CAPITAL

### ✅ DATASET AVAILABLE: Developer Survey + Education Data

#### Option 1: Stack Overflow Developer Survey (OFFICIAL, FREE)
**Link:** https://insights.stackoverflow.com/survey

**What's included:**
- Developer location (country + some cities)
- Programming languages
- Salary
- Experience level
- Education background
- Remote work preference

**How to download:**
1. Go to link above
2. Look for "Download Survey Data" button
3. Select latest year
4. Download CSV: `survey_results_public.csv`

**Size:** ~100 MB
**Year coverage:** 2021-2024 (latest available)

**Status:** ✅ FREE, ✅ OFFICIAL, ✅ HIGHLY RECOMMENDED

---

#### Option 2: Kaggle - Developer Salary Dataset
**Link:** https://www.kaggle.com/datasets/harshsingh2209/developer-salaries-in-2024

**What's included:**
- Developer location (city, country)
- Experience level
- Salary
- Technology stack
- Company type

**How to download:**
1. Go to link above
2. Click "Download"
3. Use CSV: `developer_salaries.csv`

**Status:** ✅ FREE, ✅ READY TO USE

---

#### Option 3: World Bank - Education API (FREE)
**Link:** https://data.worldbank.org/

**Available via API:**
- Tertiary education enrollment %
- School enrollment rates
- Education quality index
- Literacy rate

**How to use:**
```python
import wbdata

indicators = {
    'SE.ADT.TERT.ZS': 'tertiary_education_pct',
    'SE.HES.ENRL': 'higher_ed_enrollment',
    'SE.ADT.LITR.ZS': 'literacy_rate'
}

education_data = wbdata.get_dataframe(indicators)
```

**Status:** ✅ FREE, ✅ API

---

### 📥 HOW TO GET DIMENSION 6 DATA:

```
STEP 1: Download Stack Overflow Survey (PRIORITY!)
├─ Go to: https://insights.stackoverflow.com/survey
├─ Download latest year
└─ File: survey_results_public.csv

STEP 2: Download Kaggle Developer Salary
├─ Go to Kaggle link
├─ Click Download
└─ File: developer_salaries.csv

STEP 3: Get World Bank Education API
├─ Call API for education metrics
└─ By country

STEP 4: Process in Python
├─ Load survey_results_public.csv
├─ Group by location:
│  ├─ Count developers
│  ├─ Average salary
│  ├─ Skill distribution
│  └─ Experience levels
│
├─ Load developer_salaries.csv
├─ Verify salary data by city
│
├─ Add World Bank education data
└─ Output: talent_dimension_data.csv
```

**Total collection time:** 2-3 hours
**Difficulty:** ⭐ (Download + filter by location)

---

## DIMENSION 7: FUTURE TRAJECTORY & GROWTH

### ✅ USE HISTORICAL DATA FROM ABOVE DATASETS

**No separate dataset needed!** Use the datasets dari Dimensions 1-6 dengan **historical years**.

```
STEP 1: Use Crunchbase Data (Dimension 3)
├─ Filter by founding_year (2014-2024)
├─ Group by city + year
├─ Calculate YoY startup growth rate
└─ Example: Bangkok startups: 2014=10, 2024=150 → 150% growth

STEP 2: Use Internet Speed Data (Dimension 2)
├─ Compare historical speeds (2015 vs 2024)
├─ Calculate improvement rate
└─ Example: Bangkok: 2015=5 Mbps, 2024=50 Mbps → 10x improvement

STEP 3: Use World Bank Historical Data (All Dimensions)
├─ GDP growth year-by-year
├─ Population growth rates
├─ Urban development trajectory
└─ Economic indicators over time

STEP 4: Combine for Growth Score
├─ Startup growth + Internet growth + Economic growth + Urban growth
├─ Weighted average
└─ Output: growth_trajectory_data.csv
```

**Total collection time:** 1 hour (just combine existing data)
**Difficulty:** ⭐ (Just aggregate historical data)

---

## 📋 COMPLETE SHOPPING LIST (All Datasets)

### REQUIRED DATASETS:

| # | Dimension | Kaggle Link | Size | Priority |
|---|-----------|------------|------|----------|
| 1 | Affordability | https://www.kaggle.com/datasets/mvieira101/global-cost-of-living | 50 MB | ⭐⭐⭐ |
| 1 | Salaries | https://www.kaggle.com/datasets/zinovyev/glassdoor-salary | 50 MB | ⭐⭐⭐ |
| 2 | Internet Speed | https://www.kaggle.com/datasets/taruntiwarihp/internet-speed-by-country | 5 MB | ⭐⭐⭐ |
| 2 | Internet Users | https://www.kaggle.com/datasets/aliashraf/global-internet-users | 10 MB | ⭐⭐⭐ |
| 2 | Tech Jobs | https://www.kaggle.com/datasets/PromptCloudHQ/tech-jobs-on-dice | 30 MB | ⭐⭐ |
| 3 | Startups | https://www.kaggle.com/datasets/mgmarques/crunchbase-companies | 500 MB | ⭐⭐⭐ |
| 4 | World Cities | https://www.kaggle.com/datasets/max-mind/world-cities-database | 50 MB | ⭐⭐⭐ |
| 4 | City Temp | https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities | 100 MB | ⭐ |
| 5 | Patents | https://www.kaggle.com/datasets/trainingdatasus/patent-data | 200 MB | ⭐⭐⭐ |
| 5 | University Rankings | https://www.kaggle.com/datasets/mylesoneill/world-university-rankings | 10 MB | ⭐⭐⭐ |
| 6 | Developer Survey | https://insights.stackoverflow.com/survey | 100 MB | ⭐⭐⭐ |
| 6 | Dev Salaries | https://www.kaggle.com/datasets/harshsingh2209/developer-salaries-in-2024 | 30 MB | ⭐⭐ |

**TOTAL SIZE:** ~1.1 GB (manageable!)

### REQUIRED APIs (NO DOWNLOAD):

| Source | Link | Data |
|--------|------|------|
| World Bank | https://data.worldbank.org/ | GDP, education, urban, population data |
| Stack Overflow Survey | https://insights.stackoverflow.com/survey | Developer distribution (optional, already in Kaggle alternatives) |

---

## 🚀 QUICKSTART: DOWNLOAD ALL IN 1 HOUR

### Step 1: Create Kaggle Account (5 min)
```
1. Go to: https://www.kaggle.com/
2. Sign up (free)
3. Go to Account Settings → API
4. Download kaggle.json
5. Save to: ~/.kaggle/kaggle.json
```

### Step 2: Download All Datasets Using Python Script
```python
# Install kaggle CLI
pip install kaggle

# Download all datasets at once
import os
os.system('kaggle datasets download -d mvieira101/global-cost-of-living')
os.system('kaggle datasets download -d zinovyev/glassdoor-salary')
os.system('kaggle datasets download -d taruntiwarihp/internet-speed-by-country')
os.system('kaggle datasets download -d aliashraf/global-internet-users')
os.system('kaggle datasets download -d PromptCloudHQ/tech-jobs-on-dice')
os.system('kaggle datasets download -d mgmarques/crunchbase-companies')
os.system('kaggle datasets download -d max-mind/world-cities-database')
os.system('kaggle datasets download -d trainingdatasus/patent-data')
os.system('kaggle datasets download -d mylesoneill/world-university-rankings')
os.system('kaggle datasets download -d harshsingh2209/developer-salaries-in-2024')

# Unzip all
os.system('for file in *.zip; do unzip -q "$file"; done')
```

**Result:** All datasets downloaded + unzipped in 1 hour!

---

## ⚠️ IMPORTANT NOTES

### Dataset Coverage:
```
✅ COVERS: 100+ countries
✅ COVERS: 500+ major cities
✅ TIME RANGE: 2014-2024
⚠️ NOTE: Some cities have more complete data than others
⚠️ NOTE: Not all dimensions have perfect coverage for all cities
```

### Data Quality:
```
✅ Good quality datasets
✅ Pre-cleaned (mostly)
⚠️ May need minor cleaning/validation
⚠️ Some missing values (expected)
```

### For cities with limited data:
```
If a city doesn't have data in all dimensions:
├─ Use regional averages
├─ Use country averages
├─ Mark as "data incomplete"
└─ Document in report
```

---

## 📥 NEXT STEPS

1. **Create Kaggle account** (free)
2. **Download all datasets** (using script above)
3. **Extract all CSVs** (unzip)
4. **Start Claude Code artifact** for data merging/processing

**Ready?** Lemme create Claude Code artifact untuk download + merge semua data! 🚀