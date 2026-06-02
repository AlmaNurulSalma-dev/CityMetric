# CityMetric — Methodology

## Overview

CityMetric builds a composite **Opportunity Index** for 55 global cities using
a 6-phase pipeline: data collection → preprocessing → feature engineering →
clustering (WEKA K-Means) → visualization → dashboard.

---

## Phase 1 — Data Collection

Eight data sources are loaded and standardised:

| Source | Type | Coverage |
|--------|------|----------|
| Numbeo Cost of Living | Kaggle CSV (4,956 cities) | Global |
| MaxMind World Cities | Kaggle CSV (3.1M entries) | Global (lat/lon/pop) |
| NOAA City Temperature | Kaggle CSV (1995–2020) | ~100 major cities |
| World Bank API (wbdata) | REST API | 200+ countries, 13 indicators |
| CWUR University Rankings | Kaggle CSV (2012–2015) | 100+ countries |
| Times Higher Education | Kaggle CSV (2011–2016) | 100+ countries |
| Shanghai Rankings | Kaggle CSV (2005–2015) | 100+ countries |
| Stack Overflow Survey | Official CSV (2024) | 149 countries |

Only **923 Numbeo entries** with `data_quality=1` (high confidence) are used.
World Bank and university data are country-level, mapped to cities by country.

---

## Phase 2 — Preprocessing

### Missing value strategy
- Quantitative columns: filled with **regional median** (grouped by region),
  then global median for any remaining gaps.
- Result: zero missing values in all key columns across 55 cities.

### City deduplication
- Exact city-name duplicates from country-join fan-out are removed (keep first).

---

## Phase 3 — Feature Engineering

### Normalization
All raw metrics are normalized to **0–10** using Min-Max scaling:

```
score = (x - min) / (max - min) × 10
```

For metrics where **lower = better** (e.g. rent, food costs), the formula is
inverted:

```
score = (max - x) / (max - min) × 10
```

### Dimension formulas

#### 1. Affordability Score
```
salary_to_rent  = avg_net_salary / (rent_1br_city_center + 1)

affordability = 0.35 × norm(salary_to_rent)
              + 0.25 × norm(avg_net_salary)
              + 0.20 × norm_inv(rent_1br_city_center)
              + 0.10 × norm_inv(meal_inexpensive_restaurant)
              + 0.05 × norm_inv(utilities_monthly_85m2)
              + 0.05 × norm_inv(monthly_pass_transport)
```

#### 2. Digital Score
```
digital = 0.35 × norm(internet_users_pct)
        + 0.30 × norm(broadband_per_100)
        + 0.20 × norm(mobile_per_100)
        + 0.15 × norm_inv(internet_monthly_60mbps)
```

#### 3. Urban Score
```
temp_comfort = 10 − norm(|avg_temp_c − 20|)   # peaks at 20 °C

urban = 0.30 × norm(urban_pop_pct)
      + 0.20 × norm(population, cap_95th)
      + 0.30 × temp_comfort
      + 0.20 × norm_inv(temp_std_c)
```

#### 4. Innovation Score
```
innovation = 0.25 × norm(rd_spending_pct_gdp)
           + 0.25 × norm(scientific_articles)
           + 0.20 × norm(high_tech_exports_pct)
           + 0.20 × norm(cwur_top_uni_score)
           + 0.10 × norm(cwur_patents)
```

#### 5. Talent Score
```
dev_density = so_developer_count / (log(population) + 1)

talent = 0.30 × norm(tertiary_enrollment_pct)
       + 0.20 × norm(adult_literacy_pct)
       + 0.15 × norm(edu_spending_pct_gdp)
       + 0.25 × norm(dev_density)
       + 0.10 × norm(so_senior_dev_pct)
```

#### 6. Growth Score
```
growth = 0.30 × norm(gdp_per_capita_usd)
       + 0.25 × norm(pop_growth_rate)
       + 0.25 × norm(high_tech_exports_pct)
       + 0.20 × norm_inv(temp_trend_c)
```

#### Overall Opportunity Index
```
opportunity_index = mean(affordability, digital, urban, innovation, talent, growth)
```

*Note: Startup Ecosystem (Dimension 3) was excluded — no reliable open data
source was available for all 55 cities.*

---

## Phase 4 — Clustering (WEKA + scikit-learn)

### Input features
The 6 normalized dimension scores (0–10) are used as clustering features.
Scores are re-scaled with MinMaxScaler before clustering.

### Algorithm
**K-Means (SimpleKMeans in WEKA)** with:
- K = 5 clusters
- Seed = 42 (reproducibility)
- Max iterations = 300
- Distance: Euclidean

K=5 was chosen based on the project specification and competition requirement.
The elbow curve showed diminishing inertia improvement beyond K=5.

### Evaluation
| Metric | Value | Interpretation |
|--------|-------|---------------|
| Silhouette score | 0.236 | Acceptable for real-world geographic data |
| Davies-Bouldin | 1.229 | Moderate — clusters overlap on some dimensions |

Real-world city data does not cluster cleanly because cities are multidimensional
and many overlap on individual dimensions. A silhouette of 0.24 is typical for
this type of socioeconomic dataset.

### Cluster profiles

| Cluster | Name | Cities | Characteristic |
|---------|------|--------|---------------|
| C0 | Established Hubs | NYC, LA, SF, London, Istanbul… | High talent + innovation, expensive |
| C1 | Balanced Cities | Barcelona, Prague, Bangkok… | Balanced across all dimensions |
| C2 | Rising Stars | Seoul, Bangalore, Kuala Lumpur… | Affordable + high growth |
| C3 | Digital Leaders | Tokyo, Singapore, Amsterdam… | Highest digital + growth scores |
| C4 | Emerging Markets | Jakarta, Cairo, Lagos, Mumbai… | Low digital, affordable, high growth potential |

---

## Limitations

1. **University rankings are 2012–2016** — innovation scores may not reflect current state.
2. **Stack Overflow survey is country-level** — developer density is a proxy, not city-specific.
3. **Startup ecosystem excluded** — Crunchbase/AngelList data requires paid API.
4. **Temperature data covers ~85% of cities** — 8 cities use regional imputation.
5. **World Bank literacy data sparse** — only 40% of cities have direct values; rest imputed.
6. **K-Means assumes spherical clusters** — real city relationships may be non-spherical.
