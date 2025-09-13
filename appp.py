from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

# Load trained model
with open("aqi_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define input schema
class AQIInput(BaseModel):
    co: float
    ozone: float
    no2: float
    pm25: float

app = FastAPI(title="AQI Prediction API")

@app.post("/predict")
def predict(data: AQIInput):
    # Convert input to DataFrame
    input_data = pd.DataFrame([[data.co, data.ozone, data.no2, data.pm25]],
                              columns=['co aqi value','ozone aqi value','no2 aqi value','pm2.5 aqi value'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    return {"Predicted_AQI": round(float(prediction), 2)}

@app.get("/")
def home():
    return {"message": "AQI Prediction API is running. Go to /docs to use it."}
