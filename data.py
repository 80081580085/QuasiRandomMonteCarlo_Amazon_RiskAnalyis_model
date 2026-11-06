"""Data ingestion and preprocessing module for quantitative finance pipeline.

Handles downloading, caching, and cleaning historical asset pricing data from
Yahoo Finance."""
# ==========================================
# 1. IMPORTS
# ==========================================
import yfinance as yf
import pandas as pd
import os

# ==========================================
# 2. Configuration global variables
# ==========================================
ticker = "AMZN"
start = "2021-11-05"
end = "2026-11-05"
refresh = False


# ==========================================
# 3. Core function
# ==========================================
def get_data(ticker: str, start: str, end: str, refresh: bool) -> pd.DataFrame:
    """Gets data from yfinance and returns them in a database.

    Parameters:
        ticker (str): Fetches the desired financial data based on the ticker.
        start (str): Start date of the data to get.
        end (str): End date of the data to get (end not included).
        refresh (bool): Should the local .pkl file be refreshed.

    Returns:
        pd.DataFrame: Returns database as a pandas DataFrame.
    """
    data_file = f"{ticker}_prices.pkl"
    if os.path.exists(data_file) and  refresh != True:
        dat = pd.read_pickle(data_file)
    else:
        dat = yf.download(ticker, start=f"{start}", end=f"{end}")
        dat.to_pickle(data_file)

    if isinstance(dat.columns, pd.MultiIndex):
        dat.columns = dat.columns.get_level_values(0)

    print(dat.empty)
    print(dat.info())
    print(dat.head())

    close_price = dat["Close"]
    dat["50_day_average"] = close_price.rolling(window=50).mean()

    return dat
