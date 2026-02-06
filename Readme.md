# 🍎 Apple Stock Price Forecasting  
_Time Series & Machine Learning_

🚀 **Live Application**  
https://apple-stock-price-forecasting-hmxxmgzggm7ybkxw5et6nl.streamlit.app/

---

## 📌 Project Overview

This project focuses on forecasting **Apple Inc. (AAPL) stock prices** using a combination of  
**statistical time-series models** and **machine learning techniques**.

The primary goal is to build an **end-to-end forecasting solution** that covers:
- Business understanding
- Exploratory Data Analysis (EDA)
- Model building and comparison
- Model selection
- Cloud deployment with an interactive user interface

The project is designed to support **investors, traders, and financial analysts** in understanding short-term stock price trends.

---

## 🎯 Business Objective

To predict Apple stock prices for the **next 30 business days** using historical market data, enabling data-driven insights for potential buy/sell decision analysis.

---

## 📊 Dataset Description

The dataset consists of **historical daily Apple stock price records**, structured in strict chronological order to support time-series modeling.

### Dataset Characteristics
- Daily observations (business days)
- Time-ordered records
- Target variable: `stock_price`
- Additional macroeconomic and market-related variables used in extended analysis

This structure makes the dataset suitable for both **time-series forecasting models** and **machine learning regressors**.

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed to:
- Understand long-term trends and volatility
- Identify seasonality and temporal dependency
- Check for missing values and outliers
- Validate data suitability for forecasting models

Time-series visualizations revealed non-stationary behavior, justifying the use of transformations and advanced forecasting techniques.

---

## 🧠 Models Explored

Multiple models were implemented and evaluated to identify the most suitable forecasting approach.

### Statistical Time-Series Models
- **ARIMA** – Captures trend but lacks seasonal handling
- **SARIMA** – Captures both trend and seasonality ✅
- **VAR** – Explored for multivariate time-series relationships

### Machine Learning Models
- **Random Forest Regressor**
- **XGBoost Regressor**

For machine learning models, lag-based feature engineering was applied to transform time-series data into a supervised learning format.

---

## ⚙️ Model Evaluation & Selection

### Key Observations
- ARIMA handled trends but failed to capture seasonal effects
- SARIMA produced stable and interpretable forecasts for univariate time-series data
- Random Forest and XGBoost captured non-linear patterns but required extensive feature engineering
- XGBoost demonstrated strong learning capability but increased deployment complexity

### Final Decision
- **SARIMA** was selected for deployment due to:
  - Stability on time-series data
  - Lower computational cost
  - Better suitability for cloud deployment
- **XGBoost** remains part of the full analytical comparison documented in the notebook

---

## 🌐 Deployment Strategy

The final forecasting solution is deployed as a **live web application** using **Streamlit Community Cloud**.

### Deployment Highlights
- Lightweight, cloud-friendly architecture
- Dynamic model training at runtime
- Interactive forecast generation
- Results displayed as both **tabular output** and **visual trends**

🔗 **Live App**  
https://apple-stock-price-forecasting-hmxxmgzggm7ybkxw5et6nl.streamlit.app/

---

## ⚠️ Deployment Note (Important)

The deployed Streamlit application represents a **lightweight demonstration version** of the project.

The **complete project work** includes:
- Extensive EDA
- Multiple economic indicators
- Model comparisons (ARIMA, SARIMA, VAR, Random Forest, XGBoost)
- Larger trained models not suitable for free-tier cloud hosting

Due to **free-tier cloud CPU and memory constraints**, the live application focuses on demonstrating the **end-to-end forecasting workflow and deployment capability**, while the full analytical depth is documented in the Jupyter notebook and project presentation.

---

## 🗂 Project Structure

Apple-Stock-Price-Forecasting/
│
├── app.py # Streamlit application
├── forcasting_project.ipynb # EDA, feature engineering & model building
├── Apples_stock price dataset.xlsx # Dataset
├── Business Objective.docx # Business problem statement
├── APPLE FORCASTING TEAM 4.pptx # Final presentation
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 🛠 Technologies Used

- **Python**
- **Pandas, NumPy**
- **Matplotlib**
- **Statsmodels (ARIMA, SARIMA, VAR)**
- **XGBoost**
- **Scikit-learn**
- **Streamlit**
- **Excel**

---

## 📈 Output

- 30-business-day Apple stock price forecast
- Interactive forecast table
- Time-series trend visualization
- Live cloud-hosted web application

---

## 🚨 Disclaimer

This project is developed for **educational and demonstration purposes only**.  
Stock market prices are influenced by numerous unpredictable factors, and the forecasts generated should **not be considered financial advice**.

---

## 👥 Project Ownership & Contribution

This project was developed as a **group project** as part of an data science program initiative.

### My Contribution
I was primarily responsible for:
- Exploratory Data Analysis (EDA) and data preparation
- Time-series modeling using **SARIMA**
- Machine learning modeling using **XGBoost**
- Model comparison and selection
- Streamlit application development and cloud deployment
- GitHub repository management and documentation

GitHub: https://github.com/hariprasath797
  
---

## ⭐ Why This Project Stands Out

- Combines **statistical time-series forecasting** with **machine learning (XGBoost)**
- Demonstrates **model comparison and informed selection**
- Handles **real-world cloud deployment constraints**
- Provides a **live, interactive forecasting application**
- Showcases a complete **end-to-end data science workflow**


