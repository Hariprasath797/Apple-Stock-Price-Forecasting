import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

st.set_page_config(page_title="Apple Stock Forecast", layout="centered")

st.title("🍎 Apple Stock Price Forecasting (SARIMA)")
st.write("Generate a 30-day stock price forecast")

@st.cache_resource
def train_model():
    df = pd.read_excel("Apples_stock price dataset.xlsx")

    df['Date'] = pd.to_datetime(df.iloc[:, 0])
    df.set_index('Date', inplace=True)
    df = df.asfreq('B')

    ts = df.iloc[:, -1]

    model = SARIMAX(
        ts,
        order=(1,1,1),
        seasonal_order=(0,1,1,12),  # lighter than before
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    return model.fit(disp=False), ts


if st.button("🚀 Generate 30-Day Forecast"):
    with st.spinner("Training model & generating forecast..."):
        sarima_model, ts = train_model()

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

        st.subheader("📊 Forecast Data")
        st.dataframe(forecast_df)

        st.subheader("📈 Forecast Visualization")
        plt.figure(figsize=(10,4))
        plt.plot(forecast_df["Date"], forecast_df["Predicted Stock Price"])
        plt.xticks(rotation=45)
        st.pyplot(plt)
