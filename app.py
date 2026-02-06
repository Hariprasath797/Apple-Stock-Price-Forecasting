import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Apple Stock Price Forecasting",
    layout="centered"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Project Info")
st.sidebar.markdown("""
**Model:** SARIMA  
**Forecast Horizon:** 30 Business Days  
**Deployment:** Streamlit Cloud (Free Tier)

⚠️ Forecasts are indicative and for educational purposes only.
""")

# ---------------- MAIN TITLE ----------------
st.title("🍎 Apple Stock Price Forecasting")
st.markdown(
    "This application forecasts **Apple stock prices for the next 30 business days** "
    "using a time-series SARIMA model."
)

st.divider()

# ---------------- MODEL TRAINING ----------------
@st.cache_resource
def train_model():
    df = pd.read_excel("Apples_stock price dataset.xlsx")

    df['Date'] = pd.to_datetime(df.iloc[:, 0])
    df.set_index('Date', inplace=True)
    df = df.sort_index()
    df = df.asfreq('B')

    ts = df['stock_price']
    ts_log = np.log(ts)

    model = SARIMAX(
        ts_log,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 5),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    fitted_model = model.fit(disp=False)
    return fitted_model, ts


# ---------------- ACTION ----------------
st.subheader("🚀 Generate Forecast")

if st.button("Generate 30-Day Forecast"):
    with st.spinner("Training model and generating forecast..."):
        model, ts = train_model()

        forecast = model.get_forecast(steps=30)
        forecast_values = np.exp(forecast.predicted_mean)

        future_dates = pd.bdate_range(
            start=ts.index[-1],
            periods=30
        )

        forecast_df = pd.DataFrame({
            "Date": future_dates,
            "Predicted Stock Price": forecast_values.values
        })

        st.success("Forecast generated successfully!")

        # ---------------- OUTPUT TABLE ----------------
        st.subheader("📊 Forecast Table")
        st.dataframe(
            forecast_df.style.format(
                {"Predicted Stock Price": "{:.2f}"}
            ),
            use_container_width=True
        )

        # ---------------- PLOT ----------------
        st.subheader("📈 Forecast Trend")

        plt.figure(figsize=(10, 4))
        plt.plot(
            forecast_df["Date"],
            forecast_df["Predicted Stock Price"],
            marker="o",
            linewidth=2
        )
        plt.xlabel("Date")
        plt.ylabel("Predicted Stock Price")
        plt.grid(True)
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # ---------------- NOTE ----------------
        st.info(
            "ℹ️ Stock prices are influenced by many unpredictable factors. "
            "This forecast demonstrates the modeling and deployment workflow, "
            "not guaranteed market prediction."
        )
