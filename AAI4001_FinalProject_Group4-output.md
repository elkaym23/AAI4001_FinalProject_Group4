# 📁 PROJECT EXPORT FOR LLMs

## 📊 Project Information

- **Project Name**: `AAI4001_FinalProject_Group4`
- **Generated On**: 2025-12-04 17:16:13 (Etc/GMT+5 / GMT-05:00)
- **Total Files Processed**: 8
- **Export Tool**: Easy Whole Project to Single Text File for LLMs v1.1.0
- **Tool Author**: Jota / José Guilherme Pandolfi

### ⚙️ Export Configuration

| Setting | Value |
|---------|-------|
| Language | `en` |
| Max File Size | `1 MB` |
| Include Hidden Files | `false` |
| Output Format | `both` |

## 🌳 Project Structure

```
├── 📁 fastapi_backend/
│   ├── 📄 main.py (1.43 KB)
│   ├── 📄 model.pkl (343.3 MB)
│   ├── 📄 preprocessing.pkl (3.87 KB)
│   └── 📄 requirements.txt (55 B)
├── 📁 streamlit_frontend/
│   ├── 📄 requirements.txt (34 B)
│   └── 📄 streamlit_app.py (1.95 KB)
├── 📄 README.md (405 B)
└── 📄 test.txt (20 B)
```

## 📑 Table of Contents

**Project Files:**

- [📄 fastapi_backend/main.py](#📄-fastapi-backend-main-py)
- [📄 fastapi_backend/requirements.txt](#📄-fastapi-backend-requirements-txt)
- [📄 streamlit_frontend/requirements.txt](#📄-streamlit-frontend-requirements-txt)
- [📄 streamlit_frontend/streamlit_app.py](#📄-streamlit-frontend-streamlit-app-py)
- [📄 README.md](#📄-readme-md)
- [📄 test.txt](#📄-test-txt)

---

## 📈 Project Statistics

| Metric | Count |
|--------|-------|
| Total Files | 8 |
| Total Directories | 2 |
| Text Files | 6 |
| Binary Files | 2 |
| Total Size | 343.31 MB |

### 📄 File Types Distribution

| Extension | Count |
|-----------|-------|
| `.txt` | 3 |
| `.py` | 2 |
| `.pkl` | 2 |
| `.md` | 1 |

## 💻 File Code Contents

### <a id="📄-fastapi-backend-main-py"></a>📄 `fastapi_backend/main.py`

**File Info:**
- **Size**: 1.43 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `fastapi_backend/main.py`
- **Relative Path**: `fastapi_backend`
- **Created**: 2025-12-04 17:07:22 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-12-04 05:49:13 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `a782e61baf469136dcdd5781f491196f`
- **SHA256**: `c5b8183a22137ee56b7e8236ae2fd5d60105c7c357203e51cf1e147dc7ae38b1`
- **Encoding**: ASCII

**File code content:**

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Industrial ML Crop Yield Prediction API",
    description="Predicts crop yield (hg/ha) using rainfall, temperature, pesticides, crop type, and year.",
    version="1.0"
)

# Load saved preprocessing pipeline and the optimized RandomForest model
preprocessor = joblib.load("preprocessing.pkl")
model = joblib.load("model.pkl")

# training features
FEATURE_COLUMNS = [
    "Item",
    "Year",
    "average_rain_fall_mm_per_year",
    "avg_temp",
    "pesticides_tonnes"
]

# How FastAPI receives data from the frontend
class CropInput(BaseModel):
    Item: str
    Year: int
    average_rain_fall_mm_per_year: float
    avg_temp: float
    pesticides_tonnes: float

@app.get("/")
def home():
    return {
        "message": "Crop Yield Prediction API is running successfully.",
        "required_fields": FEATURE_COLUMNS
    }

@app.post("/predict")
def predict(input_data: CropInput):

    # Convert input into a DataFrame
    df = pd.DataFrame([input_data.dict()], columns=FEATURE_COLUMNS)

    # Apply preprocessing steps
    transformed = preprocessor.transform(df)

    # Predict using optimized RandomForest (best_random_model)
    prediction = model.predict(transformed)[0]

    return {
        "input": input_data.dict(),
        "predicted_yield_hg_per_ha": float(prediction)
    }

```

---

### <a id="📄-fastapi-backend-requirements-txt"></a>📄 `fastapi_backend/requirements.txt`

**File Info:**
- **Size**: 55 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `fastapi_backend/requirements.txt`
- **Relative Path**: `fastapi_backend`
- **Created**: 2025-12-04 17:07:23 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-12-04 08:21:05 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `6d2d7becc116ced52ebad136ad68d497`
- **SHA256**: `f9b2edd0881072e7d775abfe0a31b913df26854bdfb9ce762b5da5742924274e`
- **Encoding**: ASCII

**File code content:**

```text
fastapi
uvicorn
pandas
numpy
joblib
scikit-learn

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `fastapi_backend/model.pkl`
- `fastapi_backend/preprocessing.pkl`

### <a id="📄-streamlit-frontend-requirements-txt"></a>📄 `streamlit_frontend/requirements.txt`

**File Info:**
- **Size**: 34 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `streamlit_frontend/requirements.txt`
- **Relative Path**: `streamlit_frontend`
- **Created**: 2025-12-04 17:07:23 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-12-04 08:20:37 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `c6771932daa49391f3b3022e5f238b5f`
- **SHA256**: `635668ffeb84a3d0686735972f9babe9763411572cf6f420a42fb6e564047b05`
- **Encoding**: ASCII

**File code content:**

```text
streamlit
requests
pandas
numpy
```

---

### <a id="📄-streamlit-frontend-streamlit-app-py"></a>📄 `streamlit_frontend/streamlit_app.py`

**File Info:**
- **Size**: 1.95 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `streamlit_frontend/streamlit_app.py`
- **Relative Path**: `streamlit_frontend`
- **Created**: 2025-12-04 17:07:23 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-12-04 16:55:12 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `9ceeeac5bccddc47535fa8ab2db6ba37`
- **SHA256**: `88cc81814a5d9fad864b52efe42d8163f0967aa86a8a30610a5f9363c11eefda`
- **Encoding**: UTF-8

**File code content:**

```python
import streamlit as st
import requests

st.set_page_config(
    page_title="Crop Yield Prediction",
    layout="centered"
)

st.title("🌾 Crop Yield Prediction App")
st.write("Enter climate and agricultural inputs to estimate crop yield (hg/ha).")

# --------------------------- #
# Input fields for the user
# --------------------------- #

# Crop dropdown (based on dataset)
crop_list = [
    "Maize", "Potatoes", "Rice, paddy", "Wheat", "Sorghum", 
    "Soybeans", "Sweet potatoes", "Plantains and others", "Yams"
]

Item = st.selectbox("Crop Type", crop_list)

Year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2012,
    value=2000,
    step=1
)

average_rain_fall_mm_per_year = st.number_input(
    "Average Rainfall (mm per year)",
    min_value=0.0,
    max_value=4000.0,
    value=1200.0
)

avg_temp = st.number_input(
    "Average Temperature (°C)",
    min_value=0.0,
    max_value=40.0,
    value=20.0
)

pesticides_tonnes = st.number_input(
    "Pesticides (tonnes)",
    min_value=0.0,
    max_value=400000.0,
    value=500.0
)

# --------------------------- #
# Prediction button
# --------------------------- #

if st.button("Predict Yield"):
    payload = {
        "Item": Item,
        "Year": int(Year),
        "average_rain_fall_mm_per_year": float(average_rain_fall_mm_per_year),
        "avg_temp": float(avg_temp),
        "pesticides_tonnes": float(pesticides_tonnes)
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            prediction = response.json()["predicted_yield_hg_per_ha"]
            st.success(f"🌱 Predicted Yield: **{prediction:,.2f} hg/ha**")
        else:
            st.error("Request failed. Check FastAPI server.")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Powered by FastAPI + Streamlit + RandomForestRegressor")

```

---

### <a id="📄-readme-md"></a>📄 `README.md`

**File Info:**
- **Size**: 405 B
- **Extension**: `.md`
- **Language**: `text`
- **Location**: `README.md`
- **Relative Path**: `root`
- **Created**: 2025-12-04 17:07:20 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-12-04 08:21:36 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `7a37d8209640a933550cc00070e06b88`
- **SHA256**: `acf933872beaf87f2676bad46ce7fb6f01bff28b5671c8c24eccdb6b23144f65`
- **Encoding**: ASCII

**File code content:**

````markdown
# AAI4001_FinalProject_Group4
AAI4001_FinalProject


How to Run the FastAPI Backend
1. Navigate to the backend folder: cd fastapi_backend
2. pip install -r requirements.txt
3. Start the API: uvicorn main:app --reload

How to Run the Streamlit Frontend
1. Navigate to the frontend folder: cd streamlit_frontend
2. pip install -r requirements.txt
3. Run the app: streamlit run streamlit_app.py

````

---

### <a id="📄-test-txt"></a>📄 `test.txt`

**File Info:**
- **Size**: 20 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `test.txt`
- **Relative Path**: `root`
- **Created**: 2025-12-04 17:16:05 (Etc/GMT+5 / GMT-05:00)
- **Modified**: 2025-12-04 17:16:13 (Etc/GMT+5 / GMT-05:00)
- **MD5**: `56530b62682e3319a320152a78e4a3bf`
- **SHA256**: `4b3be81687585e40dd59c54ffd8360c8179f6918656b423e797bf68bda1edfe6`
- **Encoding**: ASCII

**File code content:**

```text
Will you push now?

```

---

