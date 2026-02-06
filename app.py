import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

st.title("Apple Stock Price Forecasting (SARIMA)")
st.write("30-day stock price forecast")

# Load dataset
df = pd.read_excel("Apples_stock price dataset.xlsx")

# Show columns (for safety)
st.write("Dataset Columns:", df.columns.tolist())

# Convert date column (change if needed)
df['Date'] = pd.to_datetime(df.iloc[:, 0])
df.set_index('Date', inplace=True)

# Target column (last column assumed as stock price)
ts = df.iloc[:, -1]

# Train SARIMA model
model = SARIMAX(ts, order=(1,1,1), seasonal_order=(1,1,1,12))
sarima_model = model.fit(disp=False)

if st.button("Generate 30-Day Forecast"):
    forecast = sarima_model.get_forecast(steps=30)
    forecast_values = forecast.predicted_mean

    future_dates = pd.bdate_range(
        start=ts.index[-1],
        periods=30
    )

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Predicted Stock Price": forecast_values.values
    })

    st.subheader("Forecast Data")
    st.dataframe(forecast_df)

    st.subheader("Forecast Visualization")
    plt.figure(figsize=(10,4))
    plt.plot(forecast_df["Date"], forecast_df["Predicted Stock Price"])
    plt.xticks(rotation=45)
    st.pyplot(plt)
