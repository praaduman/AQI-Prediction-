import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Air Quality Index Predictor", layout="centered")
st.title("Air Quality Index (AQI) Predictor")
st.write("Predict the Air Quality Index based on environmental parameters.")

# Load the pre-trained model
model = joblib.load("LR_AQI_Prediction.joblib")

# Input fields for the features
pm25 =st.number_input("PM2.5 (µg/m³)", min_value=0.0, max_value=500.0, value=50.0)
pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, max_value=500.0, value=80.0)
no2 = st.number_input("NO2 (ppb)", min_value=0.0, max_value=200.0, value=40.0)
so2 = st.number_input("SO2 (ppb)", min_value=0.0, max_value=200.0, value=20.0)
co = st.number_input("CO (ppm)", min_value=0.0, max_value=50.0, value=1.0)
temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)

input_data = np.array([[pm25, pm10, no2, so2, co, temperature, humidity]])

def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


if st.button("Predict AQI"):
    predicted_aqi = model.predict(input_data)
    st.success(f"Predicted AQI Value: {round(predicted_aqi[0], 2)}")
    st.info(f"AQI Category: {aqi_category(predicted_aqi[0])}")






    