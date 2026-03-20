# Time Series Analysis: Stock Price Forecasting

## Project Overview
This project aims to forecast future stock prices based on historical time-series data. The dataset used is `stock_price.csv`, specifically focusing on the `last_value` column which represents the closing price.

## Problem Statement
Forecast future values of a stock based on its historical performance using various time-series forecasting techniques and compare their accuracy.

## Dataset
- **File**: `stock_price.csv`
- **Key Columns**: `date` (Index), `last_value` (Target Variable).

## Techniques Used
1.  **Moving Average**: To smooth out short-term fluctuations and highlight longer-term trends.
2.  **ARIMA (AutoRegressive Integrated Moving Average)**: A statistical model for analyzing and forecasting time series data.
3.  **LSTM (Long Short-Term Memory)**: A type of Recurrent Neural Network (RNN) capable of learning order dependence in sequence prediction problems.

## Tasks Implemented
1.  **Time Series Visualization**: Plotting the historical data to understand trends.
2.  **Decomposition**: Breaking down the series into trend, seasonality, and residual components.
3.  **Stationarity Check**: Using the Augmented Dickey-Fuller (ADF) test to check if the data is stationary.
4.  **Forecasting**:
    -   Moving Average (30-day window).
    -   ARIMA Model.
    -   LSTM Neural Network.
5.  **Evaluation**: Comparing predicted vs actual values using RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error).

## Requirements
To run this project, install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## How to Run
1.  Ensure `stock_price.csv` is in the project directory.
2.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook time_series_analysis.ipynb
    ```
3.  Run all cells to see the analysis and forecasts.

## Results
The project outputs visualizations for each step and prints error metrics (RMSE, MAE) for the ARIMA and LSTM models to compare their performance.
