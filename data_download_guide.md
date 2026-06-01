# 📥 DATA DOWNLOAD & ORGANIZATION GUIDE

## ✅ FOLDER STRUCTURE SUDAH SIAP!

Folder structure sudah dibuat otomatis di: `/data_sources/`

```
data_sources/
│
├── 01_affordability_cost_of_living/
│   ├── metadata.txt
│   └── [DOWNLOAD → cost_of_living.csv DISINI]
│
├── 02_digital_worldbank_api/
│   ├── metadata.txt
│   ├── [EXTRACT → internet_penetration.csv DISINI]
│   ├── [EXTRACT → broadband_subscriptions.csv DISINI]
│   └── [EXTRACT → mobile_subscriptions.csv DISINI]
│
├── 03_urban_world_cities/
│   ├── metadata.txt
│   └── [DOWNLOAD → worldcities.csv DISINI]
│
├── 04_urban_city_temperature/
│   ├── metadata.txt
│   └── [DOWNLOAD → city_temperature.csv DISINI]
│
├── 05_innovation_university_rankings/
│   ├── metadata.txt
│   └── [DOWNLOAD → university_rankings.csv DISINI]
│
└── 06_talent_stackoverflow_survey/
    ├── metadata.txt
    └── [DOWNLOAD → survey_results_public.csv DISINI]
```

---

## 🎯 DOWNLOAD INSTRUCTIONS PER DATASET

Sekarang kamu tinggal download 6 dataset ini dan masukkan ke folder yang sesuai.

### 1️⃣ AFFORDABILITY - Global Cost of Living

**Folder:** `01_affordability_cost_of_living/`

**Link:** https://www.kaggle.com/datasets/mvieira101/global-cost-of-living

**Steps:**
```
1. Buka link di atas
2. Klik "Download" button (top right)
3. File akan download sebagai ZIP
4. Extract ZIP file
5. Ambil file "cost_of_living.csv"
6. Pindahkan ke folder: data_sources/01_affordability_cost_of_living/

Result:
data_sources/01_affordability_cost_of_living/
├── metadata.txt
└── cost_of_living.csv  ✅
```

**File size:** ~50 MB
**CSV name:** `cost_of_living.csv`

---

### 2️⃣ DIGITAL - World Bank API

**Folder:** `02_digital_worldbank_api/`

**Link:** https://data.worldbank.org/

**Method:** Extract via Python (NO MANUAL DOWNLOAD!)

**Script:**
```python
# Install dulu
pip install wbdata pandas

# Jalankan script ini
import wbdata
import pandas as pd

print("Extracting World Bank digital indicators...")

# Indicator untuk digital infrastructure
indicators = {
    'IT.NET.USER.ZS': 'internet_users_pct',
    'IT.NET.BBND.P2': 'broadband_subscriptions_per_100',
    'IT.CEL.SETS.P2': 'mobile_subscriptions_per_100'
}

# Get data
data = wbdata.get_dataframe(indicators)

# Save masing-masing
data[['internet_users_pct']].to_csv('internet_penetration.csv')
data[['broadband_subscriptions_per_100']].to_csv('broadband_subscriptions.csv')
data[['mobile_subscriptions_per_100']].to_csv('mobile_subscriptions.csv')

print("✅ Selesai! Pindahkan ke folder: data_sources/02_digital_worldbank_api/")
```

**Result:**
```
data_sources/02_digital_worldbank_api/
├── metadata.txt
├── internet_penetration.csv  ✅
├── broadband_subscriptions.csv  ✅
└── mobile_subscriptions.csv  ✅
```

---

### 3️⃣ URBAN - World Cities Database

**Folder:** `03_urban_world_cities/`

**Link:** https://www.kaggle.com/datasets/max-mind/world-cities-database

**Steps:**
```
1. Buka link di atas
2. Klik "Download" button
3. Extract ZIP file
4. Cari file "worldcities.csv"
5. Pindahkan ke folder: data_sources/03_urban_world_cities/

Result:
data_sources/03_urban_world_cities/
├── metadata.txt
└── worldcities.csv  ✅
```

**File size:** ~50 MB
**CSV name:** `worldcities.csv`

---

### 4️⃣ URBAN - City Temperature Data

**Folder:** `04_urban_city_temperature/`

**Link:** https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities

**Steps:**
```
1. Buka link di atas
2. Klik "Download" button
3. Extract ZIP file
4. Cari file "city_temperature.csv"
5. Pindahkan ke folder: data_sources/04_urban_city_temperature/

Result:
data_sources/04_urban_city_temperature/
├── metadata.txt
└── city_temperature.csv  ✅
```

**File size:** ~100 MB
**CSV name:** `city_temperature.csv` (atau `daily_temperature.csv`)

---

### 5️⃣ INNOVATION - University Rankings

**Folder:** `05_innovation_university_rankings/`

**Link:** https://www.kaggle.com/datasets/mylesoneill/world-university-rankings

**Steps:**
```
1. Buka link di atas
2. Klik "Download" button
3. Extract ZIP file
4. Cari file "university_rankings.csv" (atau timesData.csv)
5. Rename jadi "university_rankings.csv" (untuk consistency)
6. Pindahkan ke folder: data_sources/05_innovation_university_rankings/

Result:
data_sources/05_innovation_university_rankings/
├── metadata.txt
└── university_rankings.csv  ✅
```

**File size:** ~10 MB
**CSV name:** `university_rankings.csv`

---

### 6️⃣ TALENT - Stack Overflow Developer Survey

**Folder:** `06_talent_stackoverflow_survey/`

**Link:** https://insights.stackoverflow.com/survey

**Steps:**
```
1. Buka link di atas
2. Scroll ke bawah
3. Cari tombol "Download Survey Results"
4. Pilih tahun terbaru (2024 atau 2023)
5. Download CSV file
6. File akan bernama: survey_results_public.csv
7. Pindahkan ke folder: data_sources/06_talent_stackoverflow_survey/

Result:
data_sources/06_talent_stackoverflow_survey/
├── metadata.txt
└── survey_results_public.csv  ✅
```

**File size:** ~100 MB
**CSV name:** `survey_results_public.csv`

**Alternative (jika tidak ada di website):**
```
Cari di Kaggle: "Stack Overflow survey results"
Ada beberapa dataset komunitas yang mirip
Pilih yang paling baru + banyak responses
```

---

## ✅ DOWNLOAD CHECKLIST

Print atau screenshot ini untuk tracking:

```
DATASET DOWNLOAD STATUS:
═════════════════════════════════════════

✅ PRIORITY 1 (Download hari ini):
  □ 01_affordability_cost_of_living/cost_of_living.csv (50 MB)
  □ 03_urban_world_cities/worldcities.csv (50 MB)
  □ 05_innovation_university_rankings/university_rankings.csv (10 MB)

⭐ PRIORITY 2 (Download kemudian):
  □ 04_urban_city_temperature/city_temperature.csv (100 MB)
  □ 06_talent_stackoverflow_survey/survey_results_public.csv (100 MB)
  
✨ SPECIAL (Extract via Python):
  □ 02_digital_worldbank_api/internet_penetration.csv
  □ 02_digital_worldbank_api/broadband_subscriptions.csv
  □ 02_digital_worldbank_api/mobile_subscriptions.csv

TOTAL SIZE: ~410 MB

DOWNLOAD TIME ESTIMATE:
- Kaggle datasets: 2-3 hours
- World Bank API: 30 minutes
- Total: 3-4 hours
```

---

## 📊 AFTER DOWNLOAD - VERIFICATION

Setelah semua file di-download, verify struktur:

```bash
# Check folder structure
find data_sources -type f -name "*.csv" | sort

# Expected output:
data_sources/01_affordability_cost_of_living/cost_of_living.csv
data_sources/02_digital_worldbank_api/internet_penetration.csv
data_sources/02_digital_worldbank_api/broadband_subscriptions.csv
data_sources/02_digital_worldbank_api/mobile_subscriptions.csv
data_sources/03_urban_world_cities/worldcities.csv
data_sources/04_urban_city_temperature/city_temperature.csv
data_sources/05_innovation_university_rankings/university_rankings.csv
data_sources/06_talent_stackoverflow_survey/survey_results_public.csv
```

---

## 🔧 QUICK VERIFICATION SCRIPT

Setelah download selesai, jalankan script ini untuk verify:

```python
import os
import pandas as pd

data_sources_path = 'data_sources'

# Expected files
expected_files = {
    '01_affordability_cost_of_living': ['cost_of_living.csv'],
    '02_digital_worldbank_api': [
        'internet_penetration.csv',
        'broadband_subscriptions.csv',
        'mobile_subscriptions.csv'
    ],
    '03_urban_world_cities': ['worldcities.csv'],
    '04_urban_city_temperature': ['city_temperature.csv'],
    '05_innovation_university_rankings': ['university_rankings.csv'],
    '06_talent_stackoverflow_survey': ['survey_results_public.csv']
}

print("Verifying downloaded files...")
print("=" * 60)

all_good = True

for folder, files in expected_files.items():
    folder_path = os.path.join(data_sources_path, folder)
    
    if not os.path.exists(folder_path):
        print(f"❌ {folder}: FOLDER NOT FOUND")
        all_good = False
        continue
    
    print(f"✅ {folder}/")
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        
        if os.path.exists(file_path):
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            
            # Try to read CSV to verify integrity
            try:
                df = pd.read_csv(file_path, nrows=1)
                print(f"   ✅ {file} ({size_mb:.1f} MB) - {len(df.columns)} columns")
            except Exception as e:
                print(f"   ⚠️  {file} - ERROR: {str(e)}")
                all_good = False
        else:
            print(f"   ❌ {file} - NOT FOUND")
            all_good = False

print("=" * 60)

if all_good:
    print("✅ All files downloaded successfully!")
    print("Ready to start data processing!")
else:
    print("⚠️  Some files are missing. Please download them first.")
```

---

## 📝 NEXT STEPS

After all files downloaded:

1. **Verify struktur** dengan script di atas
2. **Update metadata.txt** untuk setiap folder dengan actual download date
3. **Mulai PHASE 2** - Data Preprocessing

Example updated metadata.txt:
```
Downloaded: 2026-06-01
Files verified: YES
File size: 50 MB
Rows: 4,542
Columns: 14
Status: READY FOR PROCESSING
```

---

## ❓ TROUBLESHOOTING

### Problem: Kaggle dataset tidak bisa didownload

**Solution:**
```
1. Buat akun Kaggle (free): https://www.kaggle.com/
2. Login
3. Setup API credentials:
   - Buka Settings → API
   - Klik "Create New Token"
   - Download kaggle.json
   - Simpan di ~/.kaggle/kaggle.json
4. Coba download lagi
```

### Problem: File ZIP corrupted setelah download

**Solution:**
```
1. Delete file ZIP yang corrupt
2. Download ulang
3. Jika masih error, try beda browser
```

### Problem: CSV file tidak terbaca (encoding issue)

**Solution:**
```python
import pandas as pd

# Try different encodings
for encoding in ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']:
    try:
        df = pd.read_csv('file.csv', encoding=encoding)
        print(f"✅ Works with {encoding}")
        break
    except:
        continue
```

---

**READY TO DOWNLOAD?** 

Follow checklist di atas dan mulai download dari Priority 1 dulu! 🚀

Let me know kalau ada masalah atau pertanyaan! 💪