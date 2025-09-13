# Air Quality Index Prediction using Random Forest Regressor

## 📌 Project Overview  
This project is a **machine learning-based application** that predicts the **Air Quality Index (AQI)** for a location based on key pollutant levels using a **Random Forest Regressor**. It includes **data preprocessing, model training, evaluation, and a REST API built with FastAPI**. 

## 🚀 Features  
- **Trained Random Forest model** for accurate AQI predictions
- **REST API** for programmatic access
- **Input validation** using Pydantic
- **Visualization** of actual vs predicted AQI (in development) 

## 📂 Project Structure  
- `aqi_model.pkl` → Trained Random Forest model
- `appp.py` → FastAPI application for AQI predictions
- `AQI-and-Lat-Long-of-Countries.csv` → Dataset used for training
- `requirements.txt` → List of dependencies
- `predictAQI.ipynb` → Jupyter Notebook for exploring data, training the model, and testing AQI predictions.

__pycache__ → Automatically generated folder storing Python bytecode files for faster execution.

## 🛠 Installation & Usage  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/Nayana739/AQI-PROJECT.git
   cd AQI-PROJECT
   ```  
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```  
3. **Run the FASTAPI app**  
   ```bash
   uvicorn main:app --reload
   ```  
4. **Use the API**

- Visit http://127.0.0.1:8000/docs → to access the interactive Swagger UI.
- Send a POST request to /predict with JSON payload:
```bash
{
  "co": 0.5,
  "ozone": 12.3,
  "no2": 20.1,
  "pm25": 35.2
}
 ``` 

## 📌 Model & Optimization  
This model is a **baseline Random Forest Regressor**. Improvements can include:
- Testing **other regression models** (XGBoost, Gradient Boosting, etc.)
- **Hyperparameter tuning** for better accuracy
- Incorporating **more pollutant features or meteorological data**

## 🤝 Contributions  
Feel free to **fork**, **improve**, and **contribute**!  

