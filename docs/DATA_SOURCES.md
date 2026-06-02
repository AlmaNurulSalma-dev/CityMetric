# CityMetric — Data Sources

## Summary

| # | Source | Dimension | Format | Access | Size |
|---|--------|-----------|--------|--------|------|
| 1 | Numbeo Cost of Living | Affordability | Kaggle CSV | Free | 1.5 MB |
| 2 | MaxMind World Cities | Urban (coords) | Kaggle CSV | Free | 157 MB |
| 3 | NOAA City Temperature | Urban (climate) | Kaggle CSV | Free | 134 MB |
| 4 | World Bank API | Digital, Urban, Innovation, Talent, Growth | REST API | Free | ~10 KB |
| 5 | CWUR Rankings | Innovation | Kaggle CSV | Free | 0.2 MB |
| 6 | Times Higher Education | Innovation | Kaggle CSV | Free | 0.3 MB |
| 7 | Shanghai Rankings | Innovation | Kaggle CSV | Free | 0.4 MB |
| 8 | Stack Overflow Survey | Talent | Official CSV | Free | 34 MB |

---

## 1. Numbeo Cost of Living

- **Kaggle dataset:** `mvieira101/global-cost-of-living`
- **File:** `data_sources/1_affordability_livability/01_cost_of_living_numbeo/data.csv`
- **Rows used:** 923 (data_quality = 1 only)
- **Key columns used:** rent_1br_city_center, avg_net_salary, meal_inexpensive_restaurant,
  utilities_monthly_85m2, monthly_pass_transport, internet_monthly_60mbps, price_per_m2_city_center
- **Note:** Columns are named x1–x55 in the Kaggle version; mapped to real names
  using the standard Numbeo column order documented in `scripts/01_data_collection.py`.

## 2. MaxMind World Cities

- **Kaggle dataset:** `max-mind/world-cities-database`
- **File:** `data_sources/4_urban_development/01_world_cities_kaggle/data.csv`
- **Rows:** 3.17 million — filtered to target 55 cities
- **Key columns used:** City (lowercase), AccentCity, Population, Latitude, Longitude
- **Use:** Geographic reference — coordinates and population for each target city.

## 3. NOAA City Temperature

- **Kaggle dataset:** `sudalairajkumar/daily-temperature-of-major-cities`
- **File:** `data_sources/4_urban_development/02_city_temperature_kaggle/city_temperature.csv`
- **Rows:** 2.9 million daily records (1995–2020)
- **Key columns used:** City, Year, AvgTemperature (converted from °F to °C)
- **Derived metrics:** avg_temp_c (annual mean), temp_std_c (climate variance), temp_trend_c (warming trend)
- **Coverage:** 47 of 55 target cities; 8 missing cities filled with regional median.

## 4. World Bank API

- **Library:** `wbdata` 1.1.0
- **File:** `data/raw/worldbank_indicators.csv`
- **Years fetched:** 2018–2023 average
- **Indicators:**

| Indicator ID | Column name | Dimension |
|---|---|---|
| IT.NET.USER.ZS | internet_users_pct | Digital |
| IT.NET.BBND.P2 | broadband_per_100 | Digital |
| IT.CEL.SETS.P2 | mobile_per_100 | Digital |
| NY.GDP.PCAP.CD | gdp_per_capita_usd | Growth |
| SI.POV.GINI | gini_index | Affordability |
| SP.URB.TOTL.IN.ZS | urban_pop_pct | Urban |
| SP.POP.GROW | pop_growth_rate | Urban / Growth |
| GB.XPD.RSDV.GD.ZS | rd_spending_pct_gdp | Innovation |
| IP.JRN.ARTC.SC | scientific_articles | Innovation |
| TX.VAL.TECH.MF.ZS | high_tech_exports_pct | Innovation / Growth |
| SE.TER.ENRR | tertiary_enrollment_pct | Talent |
| SE.ADT.LITR.ZS | adult_literacy_pct | Talent |
| SE.XPD.TOTL.GD.ZS | edu_spending_pct_gdp | Talent |

## 5–7. University Rankings (CWUR / Times / Shanghai)

- **Files:** `data_sources/5_innovation_readiness/01_university_rankings_kaggle/`
- **cwurData.csv** — Center for World University Rankings, 2012–2015
  - Key columns: patents, citations, publications, score
- **timesData.csv** — Times Higher Education, 2011–2016
  - Key columns: research, citations, total_score
- **shanghaiData.csv** — Academic Ranking of World Universities, 2005–2015
  - Key columns: total_score, uni_count (per country)
- **Mapping:** All three are country-level. Aggregated by country (max top score +
  count of ranked universities) then joined to cities by country.

## 8. Stack Overflow Developer Survey

- **Source:** insights.stackoverflow.com/survey (2024)
- **File:** `data_sources/6_talent_human_capital/01_stackoverflow_survey_official/data.csv`
- **Rows:** 11,361 usable respondents across 149 countries
- **Key columns used:** Country, Employment, YearsCode, ConvertedCompYearly
- **Derived metrics:** so_developer_count (per country), so_employed_dev_count,
  so_median_salary_usd, so_senior_dev_pct (≥10 years experience)
- **Note:** This is a partial sample (~11K of ~65K full survey). Results are
  proportionally valid as a talent density proxy but not absolute counts.
