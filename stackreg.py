import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("gold_forecast_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.set_page_config(
    page_title="Gold Price Forecasting",
    layout="centered"
)

st.title("Gold Price Forecasting App")

st.write("Predict Future Gold Prices in Indian Rupees")

future_date = st.date_input("Select Future Date")

spx = st.number_input("SPX", value=1500.0)

uso = st.number_input("USO", value=50.0)

slv = st.number_input("SLV", value=20.0)

eurusd = st.number_input("EUR/USD", value=1.10)

if st.button("Predict Future Gold Price"):

    # Extract Date Features
    year = future_date.year
    month = future_date.month
    day = future_date.day

    input_data = np.array([[
        spx,
        uso,
        slv,
        eurusd,
        year,
        month,
        day
    ]])

    input_scaled = scaler.transform(input_data)
    prediction_usd = model.predict(input_scaled)[0]

    usd_to_inr = 96

    prediction_inr = prediction_usd * usd_to_inr

    st.success(
        f"Predicted Gold Price: ₹{prediction_inr:,.2f} INR"
    )