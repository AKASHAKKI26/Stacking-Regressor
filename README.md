# Stacking-Regressor
# Gold Price Forecasting using Stacking Regressor

This project is a Machine Learning web application built using Streamlit and Stacking Regressor.

The application predicts future gold prices based on market indicators and date information.

---

## Features Used

- SPX
- USO
- SLV
- EUR/USD
- Year
- Month
- Day

---

## Target

```text
GLD (Gold Price)
```

---

## Machine Learning Algorithms

### Base Models
- Linear Regression
- Decision Tree Regressor
- KNN Regressor
- SVR

### Meta Model
- Random Forest Regressor

### Final Model
- Stacking Regressor

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Project Structure

```text
GoldPriceForecasting/
│
├── app.py
├── gold_forecast_model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
└── README.md
```

---

## Installation

Install required libraries using:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Input Features

| Feature | Description |
|---|---|
| SPX | S&P 500 Index |
| USO | Oil ETF |
| SLV | Silver ETF |
| EUR/USD | Euro to USD Ratio |
| Year | Future Year |
| Month | Future Month |
| Day | Future Day |

---

## Output

The application predicts:

```text
Future Gold Price
```

Example:

```text
Predicted Gold Price: ₹ 5,43,210.00
```

---

## Model Description

The model is trained using:

- Gold Price Dataset
- Feature Engineering
- Date Feature Extraction
- Feature Scaling
- Ensemble Learning using Stacking Regressor

---

## Expected Performance

```text
R² Score: 95% to 99%
```

---

## Author

Machine Learning Mini Project
