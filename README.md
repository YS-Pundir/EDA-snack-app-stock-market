# 🍿 EDA-Snack-App: Stock Market Pulse

A bite-sized, end-to-end data pipeline that fetches real-time stock data via the Alpha Vantage API. This project serves as a comprehensive **Data Ingestion & EDA** capstone, marking the successful completion of **Module 1** in my journey toward becoming an AI Engineer.

## 🚀 Live Dashboard
[**Click here to view the Live App on Streamlit Cloud**](https://ys-pundir-eda-snack-app-stock-market-file-hbrih4.streamlit.app/)

---

## 🛠️ Technical Workflow
This application demonstrates a professional data lifecycle:
1.  **Data Ingestion:** Programmatic fetching of dynamic JSON data using the `requests` library.
2.  **Data Cleaning:** Flattening nested JSON responses into structured `Pandas DataFrames`.
3.  **Type Engineering:** Automated conversion of API string values to `float64` and `datetime` objects for time-series analysis.
4.  **Exploratory Data Analysis (EDA):** * **Univariate:** Statistical distribution of trading volume and price points.
    * **Bivariate:** Analysis of price trends over 100-day windows.
    * **Multivariate:** Correlation Heatmaps to identify relationships between trading volume and price volatility.

## 🧪 The Tech Stack
* **Python 3.10+**
* **Pandas & NumPy:** For robust data manipulation.
* **Plotly Express:** For interactive, high-fidelity visualizations.
* **Streamlit:** For rapid web deployment and UI/UX design.
* **Dotenv:** For secure API credential management.

---

## 📈 Key Insights from EDA
* **Volatility Detection:** Used Boxplots to successfully identify statistical outliers in trading volume, highlighting high-impact news days.
* **Metric Correlation:** Confirmed near-perfect linear correlation between Open/Close metrics, while discovering the inverse relationship between volume and price stability.
* **Pipeline Reliability:** Developed logic to handle API output sizes and sort data chronologically for accurate trend mapping.

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/YS-Pundir/EDA-snack-app-stock-market.git](https://github.com/YS-Pundir/EDA-snack-app-stock-market.git)
cd EDA-snack-app-stock-market
