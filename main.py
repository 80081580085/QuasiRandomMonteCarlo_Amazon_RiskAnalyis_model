"""
Main execution script for the Monte Carlo simulation engine with visualization.
"""

import matplotlib.pyplot as plt
from analytics import drift_and_volatility, log_returns
from data import get_data
from simulation import simulate_MC


def main():
  # 1. Define your parameters
  ticker = "AAPL"
  start_date = "2023-01-01"
  end_date = "2026-01-01"

  print(f"--- 1. Fetching data for {ticker} ---")
  df = get_data(ticker, start_date, end_date)
  latest_price = df["Close"].iloc[-1]
  print(f"Latest Price ({ticker}): ${latest_price:.2f}")

  print(f"--- 2. Computing Analytics ---")
  # 1. Convert raw prices to log returns first!
  returns = log_returns(df)

  # 2. Then calculate drift and volatility from those returns
  drift, volatility = drift_and_volatility(returns)

  print(f"Annualized Drift: {drift:.4f}")
  print(f"Annualized Volatility: {volatility:.4f}")

  print(f"--- 3. Running Monte Carlo Simulation ---")
  sim_df = simulate_MC(
      drift=drift,
      volatility=volatility,
      start_price=latest_price,
      df=5,
      days=1500,
      num_simulations=1000,
  )
  print("Simulation complete!")

  print(f"--- 4. Plotting Simulation Paths ---")
  plt.figure(figsize=(12, 6))

  # Plot individual simulation paths with high transparency (alpha)
  plt.plot(sim_df, color="steelblue", alpha=0.03, linewidth=0.8)

  # Compute statistical summary lines across the paths
  median_path = sim_df.median(axis=1)
  p5 = sim_df.quantile(0.05, axis=1)
  p95 = sim_df.quantile(0.95, axis=1)

  # Plot key statistical boundaries
  plt.plot(median_path, color="darkorange", linewidth=2, label="Median Path")
  plt.plot(
      p95, color="crimson", linestyle="--", linewidth=1.5, label="95th Percentile"
  )
  plt.plot(
      p5, color="crimson", linestyle="--", linewidth=1.5, label="5th Percentile"
  )

  plt.title(
      f"Monte Carlo Price Simulation for {ticker} (Student-t Fat Tails, df=5)",
      fontsize=14,
  )
  plt.xlabel("Trading Days (1 Year)", fontsize=11)
  plt.ylabel("Simulated Price ($)", fontsize=11)
  plt.legend(loc="upper left")
  plt.grid(True, alpha=0.3)
  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  main()