import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Page config
st.set_page_config(page_title="Apple Stock Price Forecasting", layout="centered")

st.title("🍎 Apple Stock Price Forecasting (SARIMA)")
st.write("30-day Apple stock price forecast using time-series modeling")

# Cache model so it trains only once
@st.cache_resource
def train_sarima_model():
    # Load dataset
    df = pd.read_excel("Apples_stock price dataset.xlsx")

    # Convert first column to Date
    df['Date'] = pd.to_datetime(df.iloc[:, 0])
    df.set_index('Date', inplace=True)

    # Sort by date (VERY IMPORTANT)
    df = df.sort_index()

    # Business-day frequency
    df = df.asfreq('B')

    # Explicit target column (CHANGE only if your column name differs)
    ts = df['stock_price']

    # Log transform for stability
    ts_log = np.log(ts)

    # SARIMA model (light + stable for cloud)
    model = SARIMAX(
        ts_log,
        order=(1, 1, 1),
        seasonal_order=(0, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    fitted_model = model.fit(disp=False)
    return fitted_model, ts


# Button action
if st.button("🚀 Generate 30-Day Forecast"):
    with st.spinner("Training model and generating forecast..."):
        model, ts = train_sarima_model()

        # Forecast
        forecast = model.get_forecast(steps=30)
        forecast_log = forecast.predicted_mean

        # Convert back from log scale
        forecast_values = np.exp(forecast_log)

        # Future business dates
        future_dates = pd.bdate_range(
            start=ts.index[-1],
            periods=30
        )

        forecast_df = pd.DataFrame({
            "Date": future_dates,
            "Predicted Stock Price": forecast_values.values
        })

        # Output table
        st.subheader("📊 Forecast Output")
        st.dataframe(forecast_df)

        # Plot
        st.subheader("📈 Forecast Visualization")
        plt.figure(figsize=(10, 4))
        plt.plot(forecast_df["Date"], forecast_df["Predicted Stock Price"], marker='o')
        plt.xlabel("Date")
        plt.ylabel("Stock Price")
        plt.xticks(rotation=45)
        plt.grid(True)
        st.pyplot(plt)
