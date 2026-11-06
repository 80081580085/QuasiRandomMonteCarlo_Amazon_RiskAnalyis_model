import time
start_time = time.perf_counter()
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import yfinance as yf
import seaborn as sns
import pandas as pd
import os
from functools import wraps


#decorator function for measuring runtime
def timeit(func):
    @wraps(func)  # Keeps the original function's name and documentation intact
    def wrapper(*args, **kwargs):
        # 1. Record start time using high-precision clock
        start = time.perf_counter()

        # 2. Call the actual function you decorated
        result = func(*args, **kwargs)

        # 3. Record end time and calculate elapsed duration
        end = time.perf_counter()
        print(f"[{func.__name__}] finished in {end - start:.4f} seconds")

        # 4. Return the original function's result so your code doesn't break
        return result

    return wrapper

#get 5 year data of Amazon tickr "AMZN" from yfinance and store it locally
ticker = "AMZN"
data_file = f"{ticker}_prices.pkl"
refresh_pkl = False
if os.path.exists(data_file) and refresh_pkl != True:
    dat = pd.read_pickle(data_file)
else:
    dat = yf.download(ticker, start="2021-11-05", end="2026-11-05")
    dat.to_pickle(data_file)

print(dat.empty)
print(dat.info())
print(dat.head())

close_price = dat["Close", ticker]
dat["50_day_avarage"] = close_price.rolling(window=50).mean()

#plot the closing prices and the 50-day moving avarage
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12,6))
plt.plot(dat.index, close_price, label="Closing Price", linewidth=1.5)
plt.plot(dat.index, dat["50_day_avarage"], label="50Day avarage", linewidth=1.5)
plt.title(f"{ticker} Closing price from 2021-11-05 to 2026-11-05 with 50-day moving avarage")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.legend()
plt.tight_layout()

#end runtime measurement and print result
end_time = time.perf_counter()
print(f"\nExecution time: {end_time - start_time:.4f} seconds")

#show plot after measuring runtime to avoid any blocking of the running of the previous
plt.show()

