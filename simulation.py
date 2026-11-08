import numpy as np
import pandas as pd

def simulate_MC(
        drift: float,
        volatility: float,
        start_price: float,
        days: int=252,
        num_simulations: int=1000)->pd.DataFrame:

    dt = 1/252

