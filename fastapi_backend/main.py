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
