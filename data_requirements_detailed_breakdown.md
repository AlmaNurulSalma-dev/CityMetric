# 📊 GCOI INDEX - DETAILED DATA REQUIREMENTS PER DIMENSION

Ini breakdown LENGKAP untuk setiap dimension: apa data yg dibutuhkan, darimana, dan field apa.

---

## DIMENSION 1: AFFORDABILITY & LIVABILITY

### Data Fields Needed (untuk scoring 0-10):

```
1. housing_rent_1bed_city_center (USD/month)
2. housing_rent_1bed_outside_center (USD/month)
3. housing_price_per_sqm (USD)
4. meal_cost_inexpensive_restaurant (USD)
5. meal_cost_3course_midrange (USD)
6. groceries_milk (USD/liter)
7. groceries_bread (USD/loaf)
8. groceries_chicken (USD/kg)
9. transportation_monthly_pass (USD)
10. transportation_taxi_1km (USD)
11. utilities_electricity_water_gas (USD/month)
12. utilities_internet (USD/month)
13. average_salary_gross (USD/month)
14. tech_job_salary (USD/month)
15. healthcare_quality_index (0-100)
16. education_quality_index (0-100)
17. quality_of_life_index (0-100)
```

### Source 1: Kaggle - Global Cost of Living Dataset

**Link:** https://www.kaggle.com/datasets/mvieira101/global-cost-of-living

**CSV File:** `cost_of_living.csv`

**Available Columns:**
```
├─ city (string)
├─ country (string)
├─ x1_rent_1_bed_city_centre (numeric) → housing_rent_1bed_city_center
├─ x1_rent_1_bed_outside_center (numeric) → housing_rent_1bed_outside_center
├─ x2_price_per_square_meter (numeric) → housing_price_per_sqm
├─ x3_inexpensive_meal (numeric) → meal_cost_inexpensive_restaurant
├─ x3_3_course_meal_midrange (numeric) → meal_cost_3course_midrange
├─ x4_domestic_beer (numeric)
├─ x4_imported_beer (numeric)
├─ x5_milk_1_liter (numeric) → groceries_milk
├─ x6_bread_1_kg (numeric) → groceries_bread
├─ x7_chicken_fillets_1_kg (numeric) → groceries_chicken
├─ x8_monthly_pass (numeric) → transportation_monthly_pass
├─ x8_taxi_1_km (numeric) → transportation_taxi_1km
├─ x9_utilities (numeric) → utilities_electricity_water_gas
├─ x10_internet (numeric) → utilities_internet
└─ data_quality (numeric) → data quality flag
```

**Coverage:** 
- ✅ 100+ countries
- ✅ 500+ cities
- ✅ Updated 2023-2024

**Check:** https://www.kaggle.com/datasets/mvieira101/global-cost-of-living

---

### Source 2: Kaggle - Glassdoor Salary Data

**Link:** https://www.kaggle.com/datasets/zinovyev/glassdoor-salary

**CSV File:** `glassdoor_data.csv` or `salaries.csv`

**Available Columns:**
```
├─ job_title (string)
├─ salary_in_usd (numeric) → average_salary_gross
├─ job_category (string)
├─ employee_residence (string) → city/country
├─ work_year (numeric)
├─ experience_level (string)
├─ employment_type (string)
└─ company_location (string)
```

**Coverage:**
- ✅ Focus: USA + some international
- ✅ Updated 2024
- ✅ Tech-focused salaries

**Check:** https://www.kaggle.com/datasets/zinovyev/glassdoor-salary

---

### Source 3: World Bank API

**Link:** https://data.worldbank.org/

**Available Indicators (via API - NO DOWNLOAD):**
```
GDP per capita:
├─ Indicator: NY.GDP.PCAP.CD
├─ Returns: GDP per capita (current USD)
└─ Use for: Economic context

Healthcare Spending:
├─ Indicator: SH.XPD.CHEX.GD.ZS
├─ Returns: Health expenditure (% GDP)
└─ Use for: Healthcare quality proxy

Education Spending:
├─ Indicator: SE.XPD.TOTL.GD.ZS
├─ Returns: Education spending (% GDP)
└─ Use for: Education quality proxy

Urban Population:
├─ Indicator: SP.URB.TOTL.IN.ZS
├─ Returns: Urban population (%)
└─ Use for: Urbanization level
```

**How to use:**
```python
import wbdata
import pandas as pd

# Get GDP per capita for all countries
gdp_data = wbdata.get_dataframe({"NY.GDP.PCAP.CD": "gdp_per_capita"})

# Get healthcare spending
health_data = wbdata.get_dataframe({"SH.XPD.CHEX.GD.ZS": "health_spending_pct_gdp"})

# Get education spending
edu_data = wbdata.get_dataframe({"SE.XPD.TOTL.GD.ZS": "education_spending_pct_gdp"})

# Combine
data = gdp_data.join(health_data).join(edu_data)
```

**Coverage:**
- ✅ All countries
- ✅ Updated annually
- ✅ Historical data available (1960-2023)

**Check:** https://data.worldbank.org/

---

### Data Processing for Dimension 1:

```python
import pandas as pd

# Load datasets
cost_of_living = pd.read_csv('cost_of_living.csv')
glassdoor = pd.read_csv('glassdoor_data.csv')

# Process cost of living
# Group by city, get mean values
affordability_data = cost_of_living.groupby('city').agg({
    'x1_rent_1_bed_city_centre': 'mean',
    'x2_price_per_square_meter': 'mean',
    'x3_inexpensive_meal': 'mean',
    'x9_utilities': 'mean',
    'x10_internet': 'mean'
}).reset_index()

# Process salary
salary_data = glassdoor.groupby('employee_residence')['salary_in_usd'].mean()

# Merge with World Bank data
# Calculate affordability score (0-10)
# Result: affordability_dimension.csv
```

---

## DIMENSION 2: DIGITAL INFRASTRUCTURE

### Data Fields Needed:

```
1. internet_download_speed_mbps
2. internet_upload_speed_mbps
3. internet_latency_ms
4. 5g_coverage_percent
5. 4g_coverage_percent
6. internet_penetration_percent
7. broadband_availability_percent
8. smartphone_penetration_percent
9. digital_literacy_percent
10. tech_job_openings_count
11. mobile_phone_subscriptions_per_100
```

### Source 1: Kaggle - Internet Speed by Country

**Link:** https://www.kaggle.com/datasets/taruntiwarihp/internet-speed-by-country

**CSV File:** `internet_speed.csv`

**Available Columns:**
```
├─ country (string)
├─ continent (string)
├─ type (string) → Mobile/Fixed/etc
├─ speed_mbps (numeric) → internet_download_speed_mbps
├─ year (numeric)
├─ rank (numeric)
└─ date (string)
```

**Coverage:**
- ✅ 170+ countries
- ✅ 2015-2023 (historical!)
- ⚠️ Country level, not city level

**Check:** https://www.kaggle.com/datasets/taruntiwarihp/internet-speed-by-country

---

### Source 2: Kaggle - Global Internet Users

**Link:** https://www.kaggle.com/datasets/aliashraf/global-internet-users

**CSV File:** `internet_users.csv`

**Available Columns:**
```
├─ year (numeric)
├─ country (string)
├─ population (numeric)
├─ internet_users_number (numeric)
├─ internet_users_percentage (numeric) → internet_penetration_percent
├─ mobile_subscriptions (numeric) → mobile_phone_subscriptions_per_100
├─ cellular_subscriptions_per_100 (numeric)
├─ broadband_subscriptions (numeric) → broadband_availability_percent
└─ gdp (numeric)
```

**Coverage:**
- ✅ 170+ countries
- ✅ 1990-2023 (very historical!)
- ⚠️ Country level only

**Check:** https://www.kaggle.com/datasets/aliashraf/global-internet-users

---

### Source 3: Kaggle - Tech Jobs Dataset

**Link:** https://www.kaggle.com/datasets/PromptCloudHQ/tech-jobs-on-dice

**CSV File:** `jobs.csv` or `tech_jobs.csv`

**Available Columns:**
```
├─ job_title (string)
├─ company (string)
├─ location (string) → city/country
├─ experience_level (numeric)
├─ salary_low (numeric)
├─ salary_high (numeric)
├─ salary_currency (string)
├─ description (string)
├─ job_type (string)
└─ posted_date (string)
```

**Coverage:**
- ✅ USA + some international
- ✅ Tech jobs only
- ✅ Updated 2024
- ⚠️ Limited to specific job board

**Check:** https://www.kaggle.com/datasets/PromptCloudHQ/tech-jobs-on-dice

---

### Source 4: World Bank API

**Available Indicators:**
```
Mobile subscriptions per 100 people:
├─ Indicator: IT.CEL.SETS.P2
├─ Returns: Cellular subscriptions per 100 people
└─ Use for: Mobile penetration

Internet users per 100:
├─ Indicator: IT.NET.USER.ZS
├─ Returns: Internet users (% population)
└─ Use for: Internet penetration

Broadband subscriptions:
├─ Indicator: IT.NET.BBND.P2
├─ Returns: Fixed broadband subscriptions per 100
└─ Use for: Broadband availability
```

**Check:** https://data.worldbank.org/

---

### Data Processing for Dimension 2:

```python
import pandas as pd

# Load datasets
internet_speed = pd.read_csv('internet_speed.csv')
internet_users = pd.read_csv('internet_users.csv')
tech_jobs = pd.read_csv('jobs.csv')

# Get latest internet speed by country
latest_speed = internet_speed[internet_speed['year'] == internet_speed['year'].max()]
speed_by_country = latest_speed.groupby('country')['speed_mbps'].mean()

# Get latest internet users
latest_users = internet_users[internet_users['year'] == internet_users['year'].max()]
users_by_country = latest_users[['country', 'internet_users_percentage', 'mobile_subscriptions']]

# Count tech jobs by location
jobs_by_location = tech_jobs.groupby('location').size().reset_index(name='tech_jobs_count')

# Get World Bank data
# Merge all sources
# Calculate digital score (0-10)
# Result: digital_dimension.csv
```

---

## DIMENSION 3: STARTUP ECOSYSTEM

### Data Fields Needed:

```
1. startup_count_per_city
2. total_funding_usd
3. average_funding_per_startup_usd
4. startup_growth_rate_yoy_percent
5. funding_rounds_count
6. startup_status_distribution (active/acquired/closed)
7. top_industries
8. recent_funding_activity (last 2 years)
```

### Source: Kaggle - Crunchbase Companies Dataset (MOST IMPORTANT!)

**Link:** https://www.kaggle.com/datasets/mgmarques/crunchbase-companies

**CSV Files:** 
- `companies.csv` (main file - LARGEST!)
- `funding_rounds.csv` (optional, for detailed funding analysis)
- `acquisitions.csv` (optional, for M&A analysis)

**Available Columns in companies.csv:**
```
├─ name (string) → company_name
├─ permalink (string) → unique_id
├─ homepage_url (string)
├─ category_code (string) → industry
├─ status (string) → active/acquired/closed/operating
├─ founded_at (string/date) → founding_year
├─ total_money_raised (numeric) → total_funding_usd
├─ funding_rounds (numeric)
├─ first_funding_at (date)
├─ last_funding_at (date)
├─ city (string) → CITY LOCATION
├─ region (string) → region
├─ country_code (string)
└─ state_code (string)
```

**Coverage:**
- ✅ 500,000+ companies
- ✅ Global coverage
- ✅ 2000-2023
- ✅ Complete funding history
- ⚠️ Large file (~500 MB)

**Check:** https://www.kaggle.com/datasets/mgmarques/crunchbase-companies

**IMPORTANT NOTES:**
- This is THE dataset for startups
- Has exact founding dates (can calculate YoY growth)
- Has city-level location data (perfect!)
- Has funding amounts (can calculate total + average)
- Has company status (can see survival rate)

---

### Data Processing for Dimension 3:

```python
import pandas as pd

# Load Crunchbase
companies = pd.read_csv('companies.csv')

# Filter startups (founded 2014 onwards, funding > 0)
startups = companies[
    (companies['founded_at'] >= '2014-01-01') & 
    (companies['total_money_raised'] > 0)
]

# Group by city
startup_metrics = startups.groupby('city').agg({
    'name': 'count',  # startup_count
    'total_money_raised': 'sum',  # total_funding
    'funding_rounds': 'mean',  # avg funding rounds
    'status': lambda x: (x == 'active').sum()  # active count
}).reset_index()

startup_metrics.columns = ['city', 'startup_count', 'total_funding_usd', 
                           'avg_funding_rounds', 'active_startups']

# Calculate avg funding per startup
startup_metrics['avg_funding_per_startup'] = (
    startup_metrics['total_funding_usd'] / startup_metrics['startup_count']
)

# Calculate YoY growth (2020 vs 2024)
startups_2020 = startups[startups['founded_at'] <= '2020-12-31']
startups_2024 = startups[startups['founded_at'] <= '2024-12-31']
growth = startups.groupby('city').apply(
    lambda x: len(x[x['founded_at'] <= '2024']) / len(x[x['founded_at'] <= '2020']) 
    if len(x[x['founded_at'] <= '2020']) > 0 else 0
)
startup_metrics['growth_rate_pct'] = growth

# Result: startup_dimension.csv
```

---

## DIMENSION 4: URBAN DEVELOPMENT

### Data Fields Needed:

```
1. city_population
2. city_area_sqkm
3. population_density_per_sqkm
4. urban_sprawl_index (0-10)
5. road_density_km_per_sqkm (from OpenStreetMap)
6. green_space_percentage
7. public_transport_coverage
8. infrastructure_quality_index (0-100)
9. city_growth_rate_percent_annually
10. urbanization_level_percent
11. climate_category
```

### Source 1: Kaggle - World Cities Database

**Link:** https://www.kaggle.com/datasets/max-mind/world-cities-database

**CSV File:** `worldcities.csv`

**Available Columns:**
```
├─ city (string) → city_name
├─ city_ascii (string)
├─ lat (numeric) → latitude
├─ lng (numeric) → longitude
├─ country (string)
├─ iso2 (string) → country_code_2
├─ iso3 (string) → country_code_3
├─ admin_name (string) → region/state
├─ capital (string) → is_capital (Y/N)
├─ population (numeric) → city_population
├─ area (numeric) → city_area_sqkm (sometimes)
└─ density (numeric) → population_density
```

**Coverage:**
- ✅ 43,000+ cities worldwide
- ✅ Population data (mostly 2020)
- ⚠️ May have missing area data
- ✅ Exact coordinates (useful!)

**Check:** https://www.kaggle.com/datasets/max-mind/world-cities-database

---

### Source 2: Kaggle - City Temperature Dataset

**Link:** https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities

**CSV File:** `city_temperature.csv`

**Available Columns:**
```
├─ Region (string) → continent
├─ Country (string)
├─ City (string)
├─ Month (numeric)
├─ Day (numeric)
├─ Year (numeric)
├─ AvgTemperature (numeric)
├─ AvgTemperatureUncertainty (numeric)
└─ Latitude/Longitude (sometimes)
```

**Coverage:**
- ✅ 100+ major cities
- ✅ 1743-2013 (historical!)
- ✅ Can infer climate category

**Check:** https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities

---

### Source 3: World Bank API

**Available Indicators:**
```
Urban population percentage:
├─ Indicator: SP.URB.TOTL.IN.ZS
├─ Returns: Urban population (% total)
└─ Use for: urbanization_level_percent

Population growth rate:
├─ Indicator: SP.POP.GROW
├─ Returns: Annual population growth (%)
└─ Use for: city_growth_rate_percent_annually

Land area:
├─ Indicator: AG.LND.TOTL.K2
├─ Returns: Land area (km²)
└─ Use for: country/regional context
```

**Check:** https://data.worldbank.org/

---

### Data Processing for Dimension 4:

```python
import pandas as pd

# Load datasets
cities = pd.read_csv('worldcities.csv')
temps = pd.read_csv('city_temperature.csv')

# Calculate urban metrics
urban_data = cities[['city', 'country', 'population', 'area', 'lat', 'lng']].copy()
urban_data['population_density'] = urban_data['population'] / urban_data['area']

# Get climate by city (from temperature data)
climate_by_city = temps.groupby('City')['AvgTemperature'].mean()

# Add climate classification
def classify_climate(avg_temp):
    if avg_temp < 0: return 'Cold'
    elif avg_temp < 10: return 'Cool'
    elif avg_temp < 20: return 'Temperate'
    elif avg_temp < 25: return 'Warm'
    else: return 'Hot'

urban_data = urban_data.merge(
    climate_by_city.apply(classify_climate),
    left_on='city', right_index=True, how='left'
)

# Get World Bank data
# Merge all sources
# Calculate urban score (0-10)
# Result: urban_dimension.csv
```

---

## DIMENSION 5: INNOVATION READINESS

### Data Fields Needed:

```
1. patent_count_total
2. patent_density_per_capita
3. patent_growth_rate_yoy
4. top_universities_count
5. university_quality_ranking_average
6. research_publications_count
7. citation_impact_index
8. r_and_d_investment_percent_gdp
9. research_institutions_count
10. technology_category_distribution
11. patent_filing_trend
```

### Source 1: Kaggle - Patent Dataset

**Link:** https://www.kaggle.com/datasets/trainingdatasus/patent-data

**CSV Files:**
- `patents.csv` (main)
- `inventors.csv` (optional, for inventor location)

**Available Columns in patents.csv:**
```
├─ patent_id (string) → unique_patent_id
├─ patent_date (date) → filing_date
├─ patent_title (string)
├─ category (string) → technology_category
├─ claims (numeric) → patent_complexity
├─ citations (numeric) → citation_count
├─ inventors (string)
├─ assignee (string) → company/institution
├─ inventor_location (string) → city/country (if available)
└─ abstract (string)
```

**Coverage:**
- ✅ USA patents mainly
- ✅ 1976-2023+
- ✅ Historical data available
- ⚠️ US-centric (World patents harder to get)

**Check:** https://www.kaggle.com/datasets/trainingdatasus/patent-data

---

### Source 2: Kaggle - University Rankings

**Link:** https://www.kaggle.com/datasets/mylesoneill/world-university-rankings

**CSV File:** `university_rankings.csv` or similar

**Available Columns:**
```
├─ university_name (string)
├─ country (string)
├─ year (numeric)
├─ world_rank (numeric) → ranking
├─ national_rank (numeric)
├─ research_score (numeric)
├─ teaching_score (numeric)
├─ international_score (numeric)
├─ industry_income (numeric)
└─ citations_per_faculty (numeric) → research_quality
```

**Coverage:**
- ✅ Top 1000 universities worldwide
- ✅ 2011-2023
- ✅ Multiple ranking systems
- ✅ City-level information (usually)

**Check:** https://www.kaggle.com/datasets/mylesoneill/world-university-rankings

---

### Source 3: Kaggle - Research Papers Dataset (Optional, Large)

**Link:** https://www.kaggle.com/datasets/Cornell-University/arxiv

**Size:** ~3 GB (Large! Optional)

**If you want to include:**
```
├─ paper_id
├─ submitter (string)
├─ authors (string)
├─ title (string)
├─ comments (string)
├─ journal_ref (string)
├─ doi (string)
├─ report_number (string)
├─ categories (string) → research_field
├─ license (string)
├─ abstract (string)
├─ versions (array)
├─ update_date (date)
├─ authors_parsed (array) → can extract affiliation
└─ submitter_email (string) → can infer location
```

**Check:** https://www.kaggle.com/datasets/Cornell-University/arxiv

---

### Source 4: World Bank API

**Available Indicators:**
```
R&D spending:
├─ Indicator: GB.XPD.RSDV.GD.ZS
├─ Returns: R&D expenditure (% GDP)
└─ Use for: r_and_d_investment_percent_gdp

Scientific publications:
├─ Indicator: IP.JRN.ARTC.SC
├─ Returns: Scientific articles published
└─ Use for: research_publications_count
```

**Check:** https://data.worldbank.org/

---

### Data Processing for Dimension 5:

```python
import pandas as pd

# Load datasets
patents = pd.read_csv('patents.csv')
universities = pd.read_csv('university_rankings.csv')

# Patent analysis
# Group by inventor location (if available)
patent_by_location = patents.groupby('inventor_location').agg({
    'patent_id': 'count',  # patent_count
    'citations': 'mean',  # citation_impact
    'patent_date': lambda x: x.max() - x.min()  # time span
}).reset_index()

patent_by_location.columns = ['location', 'patent_count', 'avg_citations', 'years_active']

# Calculate patent density (need population data)
# patent_density = patent_count / population

# University analysis
# Get latest rankings
latest_rankings = universities[universities['year'] == universities['year'].max()]

# Group by country/city
uni_by_location = latest_rankings.groupby('country').agg({
    'university_name': 'count',  # university_count
    'world_rank': 'mean',  # avg_ranking
    'research_score': 'mean'  # research_quality
}).reset_index()

# Get World Bank R&D data
# Merge all sources
# Calculate innovation score (0-10)
# Result: innovation_dimension.csv
```

---

## DIMENSION 6: TALENT & HUMAN CAPITAL

### Data Fields Needed:

```
1. developer_count_per_city
2. tech_worker_concentration
3. average_developer_salary
4. programming_language_distribution
5. experience_level_distribution
6. education_level_distribution
7. tertiary_education_rate_percent
8. skilled_worker_immigration_rate
9. tech_talent_attraction_index
10. brain_drain_rate
11. remote_work_readiness_percent
```

### Source 1: Stack Overflow Developer Survey (OFFICIAL - BEST SOURCE!)

**Link:** https://insights.stackoverflow.com/survey

**File:** `survey_results_public.csv` (latest year)

**Available Columns:**
```
├─ ResponseId (numeric)
├─ Respondent (numeric) → unique ID
├─ MainBranch (string) → developer type
├─ Employment (string) → employment_type
├─ Country (string) → responder_country
├─ RemoteWork (string) → remote_work_yes/no/hybrid
├─ EdLevel (string) → education_level
├─ YearsCode (numeric) → years_experience
├─ YearsCodePro (numeric) → professional_experience
├─ DevType (string) → developer_type_category
├─ Language (string) → primary_programming_language
├─ Salary (numeric) → salary_usd
├─ SalaryType (string)
├─ CompFreq (string)
├─ Currency (string)
├─ DatabaseHaveWorkedWith (string)
├─ PlatformHaveWorkedWith (string)
└─ FrameworkHaveWorkedWith (string)
```

**Coverage:**
- ✅ 50,000+ responses
- ✅ 180+ countries
- ✅ Annual survey (2014-2024)
- ✅ Can filter by country/region
- ⚠️ Self-reported (some bias)

**Check:** https://insights.stackoverflow.com/survey

---

### Source 2: Kaggle - Developer Salaries 2024

**Link:** https://www.kaggle.com/datasets/harshsingh2209/developer-salaries-in-2024

**CSV File:** `developer_salaries.csv` or `ds.csv`

**Available Columns:**
```
├─ Name (string)
├─ Location (string) → city/country
├─ Experience_Level (string)
├─ Salary (numeric) → salary_in_local_currency
├─ Salary_Currency (string)
├─ Salary_in_USD (numeric)
├─ Employment_Type (string)
├─ Job_Title (string)
├─ Company_Size (string)
├─ Tech_Stack (string)
└─ Remote_Friendly (boolean)
```

**Coverage:**
- ✅ Updated 2024
- ✅ Multiple countries
- ✅ Tech salary focused
- ⚠️ Limited to specific job boards

**Check:** https://www.kaggle.com/datasets/harshsingh2209/developer-salaries-in-2024

---

### Source 3: World Bank API

**Available Indicators:**
```
Tertiary education enrollment:
├─ Indicator: SE.ADT.TERT.ZS
├─ Returns: Adult tertiary education (%)
└─ Use for: tertiary_education_rate_percent

School enrollment:
├─ Indicator: SE.ADT.LITR.ZS
├─ Returns: Literacy rate (%)
└─ Use for: education_level_proxy

Government spending on education:
├─ Indicator: SE.XPD.TOTL.GD.ZS
├─ Returns: Education expenditure (% GDP)
└─ Use for: education_investment
```

**Check:** https://data.worldbank.org/

---

### Data Processing for Dimension 6:

```python
import pandas as pd

# Load datasets
survey = pd.read_csv('survey_results_public.csv')
dev_salaries = pd.read_csv('developer_salaries.csv')

# Survey analysis - group by country
survey_by_country = survey.groupby('Country').agg({
    'ResponseId': 'count',  # developer_count
    'Salary': 'mean',  # avg_salary
    'RemoteWork': lambda x: (x == 'Hybrid').sum() / len(x),  # remote_pct
    'YearsCodePro': 'mean'  # avg_experience
}).reset_index()

survey_by_country.columns = ['country', 'developer_count', 'avg_salary', 
                             'remote_work_pct', 'avg_experience']

# Salary verification - from dev_salaries dataset
salary_by_location = dev_salaries.groupby('Location').agg({
    'Salary_in_USD': 'mean',
    'Experience_Level': lambda x: x.mode()[0]
}).reset_index()

# Get World Bank education data
# Merge all sources
# Calculate talent score (0-10)
# Result: talent_dimension.csv
```

---

## DIMENSION 7: FUTURE TRAJECTORY & GROWTH

### Data Fields Needed:

```
1. historical_startup_founding_count_by_year
2. startup_funding_growth_rate_5yr
3. internet_speed_improvement_rate_5yr
4. gdp_growth_rate_5yr_average
5. population_growth_rate_5yr
6. urban_development_growth_rate
7. patent_filing_growth_rate
8. tech_job_growth_rate
9. forecast_2030_opportunity_index
10. risk_factors_score
11. economic_resilience_index
```

### HOW TO GET: Use historical data from above dimensions!

**NO NEW DATASET NEEDED!**

Use existing datasets with **temporal filtering:**

```
From Crunchbase (Dimension 3):
├─ Filter by founding_date for each year
├─ Calculate: startups_2014, startups_2015, ... startups_2024
├─ Growth rate = (2024 - 2014) / 2014 * 100%

From Internet Speed Dataset (Dimension 2):
├─ Filter by year (2015, 2020, 2024)
├─ Calculate speed improvement rate
├─ Growth = (2024_speed - 2015_speed) / 2015_speed

From World Bank API:
├─ Historical GDP (annual 1990-2024)
├─ Historical population growth (annual)
├─ Calculate: 5-year average growth rate

From Patent Data (Dimension 5):
├─ Filter by patent_date (2014, 2019, 2024)
├─ Calculate: patents_2014, patents_2019, patents_2024
├─ Growth rate = (2024 - 2014) / 2014 * 100%

From Tech Jobs Data (Dimension 2):
├─ If timestamp available, filter by year
├─ Compare job volume year-over-year
├─ Calculate growth trend
```

---

### Data Processing for Dimension 7:

```python
import pandas as pd

# Use historical data from Dimension 3 (Crunchbase)
companies = pd.read_csv('companies.csv')

# Extract founding year
companies['founded_year'] = pd.to_datetime(companies['founded_at']).dt.year

# Count startups by year + city
startup_growth = companies.groupby(['city', 'founded_year']).size().unstack(fill_value=0)

# Calculate 5-year growth rate (2019-2024)
startup_growth_rate = {}
for city in startup_growth.index:
    startups_2019 = startup_growth.loc[city, 2019] if 2019 in startup_growth.columns else 0
    startups_2024 = startup_growth.loc[city, 2024] if 2024 in startup_growth.columns else 0
    
    if startups_2019 > 0:
        growth_rate = (startups_2024 - startups_2019) / startups_2019 * 100
    else:
        growth_rate = 0 if startups_2024 == 0 else 999  # New startups (high growth)
    
    startup_growth_rate[city] = growth_rate

# Use Internet Speed historical data (Dimension 2)
internet_speed = pd.read_csv('internet_speed.csv')
speed_growth = {}

for country in internet_speed['country'].unique():
    country_data = internet_speed[internet_speed['country'] == country]
    
    speed_2015 = country_data[country_data['year'] == 2015]['speed_mbps'].mean()
    speed_2024 = country_data[country_data['year'] == 2024]['speed_mbps'].mean()
    
    if speed_2015 > 0:
        growth = (speed_2024 - speed_2015) / speed_2015 * 100
    else:
        growth = 0
    
    speed_growth[country] = growth

# Get World Bank historical data
import wbdata

indicators = {
    'NY.GDP.PCAP.MKTP.KD.ZG': 'gdp_growth',  # GDP growth
    'SP.POP.GROW': 'population_growth'  # Population growth
}

growth_data = wbdata.get_dataframe(indicators)

# Combine all growth metrics
# Calculate growth_trajectory_score (0-10)
# Result: growth_dimension.csv
```

---

## 📋 COMPLETE DATA COLLECTION CHECKLIST

### PRIORITY 1 (MUST HAVE):
```
✅ Crunchbase Companies
   Link: https://www.kaggle.com/datasets/mgmarques/crunchbase-companies
   Size: 500 MB
   Priority: CRITICAL (Dimension 3)

✅ Cost of Living
   Link: https://www.kaggle.com/datasets/mvieira101/global-cost-of-living
   Size: 50 MB
   Priority: CRITICAL (Dimension 1)

✅ Glassdoor Salaries
   Link: https://www.kaggle.com/datasets/zinovyev/glassdoor-salary
   Size: 50 MB
   Priority: CRITICAL (Dimension 1)

✅ Stack Overflow Survey
   Link: https://insights.stackoverflow.com/survey
   Size: 100 MB
   Priority: CRITICAL (Dimension 6)

✅ World Cities
   Link: https://www.kaggle.com/datasets/max-mind/world-cities-database
   Size: 50 MB
   Priority: HIGH (Dimension 4)

✅ University Rankings
   Link: https://www.kaggle.com/datasets/mylesoneill/world-university-rankings
   Size: 10 MB
   Priority: HIGH (Dimension 5)
```

### PRIORITY 2 (RECOMMENDED):
```
⭐ Internet Speed
   Link: https://www.kaggle.com/datasets/taruntiwarihp/internet-speed-by-country
   Size: 5 MB
   Priority: HIGH (Dimension 2)

⭐ Internet Users
   Link: https://www.kaggle.com/datasets/aliashraf/global-internet-users
   Size: 10 MB
   Priority: HIGH (Dimension 2)

⭐ Patents
   Link: https://www.kaggle.com/datasets/trainingdatasus/patent-data
   Size: 200 MB
   Priority: MEDIUM (Dimension 5)

⭐ Tech Jobs
   Link: https://www.kaggle.com/datasets/PromptCloudHQ/tech-jobs-on-dice
   Size: 30 MB
   Priority: MEDIUM (Dimension 2)

⭐ Developer Salaries
   Link: https://www.kaggle.com/datasets/harshsingh2209/developer-salaries-in-2024
   Size: 30 MB
   Priority: MEDIUM (Dimension 6)

⭐ City Temperature
   Link: https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities
   Size: 100 MB
   Priority: LOW (Dimension 4)
```

### PRIORITY 3 (OPTIONAL):
```
◇ Research Papers (ArXiv)
   Link: https://www.kaggle.com/datasets/Cornell-University/arxiv
   Size: 3 GB (LARGE!)
   Priority: OPTIONAL (Dimension 5)
```

### ALWAYS AVAILABLE (FREE API):
```
✅ World Bank Data
   Link: https://data.worldbank.org/
   Access: Python API (wbdata library)
   Priority: CRITICAL (ALL Dimensions)
```

---

## 🎯 TOTAL DATA SIZE

```
Priority 1 + 2 datasets:
├─ Crunchbase: 500 MB
├─ Internet Speed: 5 MB
├─ Internet Users: 10 MB
├─ Patents: 200 MB
├─ Tech Jobs: 30 MB
├─ Dev Salaries: 30 MB
├─ Temperature: 100 MB
├─ Cost of Living: 50 MB
├─ Glassdoor: 50 MB
├─ World Cities: 50 MB
├─ University Rankings: 10 MB
├─ Stack Overflow: 100 MB
└─ TOTAL: ~1.1 GB

All downloadable + usable in 1-2 hours!
```

---

## ✅ NEXT STEP

Sekarang kamu punya complete breakdown:
- ✅ What data each dimension needs
- ✅ Exact Kaggle links untuk setiap dataset
- ✅ CSV filenames + column names
- ✅ Coverage info
- ✅ How to process each one

**Cek availability sendiri:**
1. Go to each Kaggle link
2. Verify dataset still available
3. Check if columns match
4. Check coverage (cities + years)

Atau mau aku buat Claude Code artifact untuk **download + merge semua data secara otomatis?** 🚀