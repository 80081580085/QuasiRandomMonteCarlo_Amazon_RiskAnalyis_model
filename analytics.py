"""
Calculates the main properties of the data
"""
import numpy as np
import pandas as pd


def log_returns(dat):
    """
    Calculates log return values
    :param dat: pandas series containing the historical data of the stock
    :return: returns the daily log returns of the stock without any nan values as a pandas series
    """
    log_return = np.log(dat["Close"]) - np.log(dat["Close"].shift(1))
    log_return = log_return.dropna()
    return log_return


def drift_and_volatility(log_returns_series):
    """
    Calculates annual drift and annual volatility
    :param log_returns_series: a pandas series containing the log return values
    :return: returns drift and volatility as a tuple
    """
    daily_volatility = log_returns_series.std()
    daily_average = log_returns_series.mean()

    drift = (daily_average + (0.5 * (daily_volatility ** 2))) * 252
    volatility = daily_volatility * np.sqrt(252)

    return drift, volatility

