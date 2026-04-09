import yfinance as yf
import matplotlib.pyplot as plt

# Pull 2 years of data
spy = yf.download("SPY",     start="2023-01-01", end="2025-01-01")
qqq = yf.download("QQQ",     start="2023-01-01", end="2025-01-01")
btc = yf.download("BTC-USD", start="2023-01-01", end="2025-01-01")

# Grab closing prices
spy_close = spy["Close"]
qqq_close = qqq["Close"]
btc_close = btc["Close"]

# Normalise to 100 at start (growth of $100 invested)
spy_norm = (spy_close / spy_close.iloc[0]) * 100
qqq_norm = (qqq_close / qqq_close.iloc[0]) * 100
btc_norm = (btc_close / btc_close.iloc[0]) * 100

# Plot
plt.figure(figsize=(12, 6))
plt.plot(spy_norm, label="SPY — S&P 500",    linewidth=1.8, color="blue")
plt.plot(qqq_norm, label="QQQ — Nasdaq 100", linewidth=1.8, color="orange")
plt.plot(btc_norm, label="BTC — Bitcoin",    linewidth=1.8, color="purple")
plt.axhline(y=100, color="grey", linestyle="--", linewidth=0.8, alpha=0.6)
plt.title("Cumulative Returns: SPY, QQQ, BTC (2023–2025)")
plt.xlabel("Date")
plt.ylabel("Growth of $100 Invested")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("multi_stock_returns.png", dpi=150)
plt.show()
print("Chart saved.")