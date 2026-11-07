from data import get_data
from analytics import log_returns, drift_and_volatility

# 1. Fetch data
df = get_data("AAPL", "2023-01-01", "2026-01-01", refresh=False)

# 2. Run analytics
log_vals = log_returns(df)
drift, vol = drift_and_volatility(log_vals)

print(f"Annual Drift: {drift:.4f}")
print(f"Annual Volatility: {vol:.4f}")