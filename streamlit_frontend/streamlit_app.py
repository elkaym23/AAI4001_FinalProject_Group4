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


AAI4001_FinalProject_Group4