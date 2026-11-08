import numpy as np
import pandas as pd
import scipy

def simulate_MC(
        drift: float,
        volatility: float,
        start_price: float,
        df: int,
        days: int=252,
        num_simulations: int=1000)->pd.DataFrame:

    dt = 1/252


    Z = scipy.stats.t.rvs(df, size=(days , num_simulations))

    daily_returns = np.exp((drift - 0.5 * (volatility**2)) * dt + (volatility * np.sqrt(dt) * Z))
    price_path = pd.DataFrame(start_price * np.cumprod(daily_returns, axis=0))

    return price_path
