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
# 2. Core function
# ==========================================
def get_data(ticker: str, start: str, end: str, refresh: bool=False) -> pd.DataFrame:
    """Gets data from yfinance and returns them in a database.

    Parameters:
        ticker (str): Fetches the desired financial data based on the ticker.
        start (str): Start date of the data to get.
        end (str): End date of the data to get (end not included).
        refresh (bool): Should the local .pkl file be refreshed.

    Returns:
        pd.DataFrame: Returns database as a pandas DataFrame.
    """
    data_file = f"{ticker, start, end}_prices.pkl"
    if os.path.exists(data_file) and  refresh != True:
        dat = pd.read_pickle(data_file)
    else:
        dat = yf.download(ticker, start=f"{start}", end=f"{end}")
        dat.to_pickle(data_file)
    if dat is None or dat.empty:
        raise ValueError(f"No data found for {ticker} form {start} to {end}!")


    if isinstance(dat.columns, pd.MultiIndex):
        dat.columns = dat.columns.get_level_values(0)


    return dat
