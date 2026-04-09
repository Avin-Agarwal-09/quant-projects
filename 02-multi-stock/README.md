# Project 02 — Multi-Asset Return Comparison

## What This Does
Compares the cumulative returns of three assets over a 2-year period (2023–2025):
- **SPY** — S&P 500 ETF
- **QQQ** — Nasdaq 100 ETF
- **BTC-USD** — Bitcoin

All assets are normalised to a starting value of 100, representing the growth of $100 invested on 1 January 2023.

## Files
- `multi_stock_returns.py` — main script
- `multi_stock_returns.png` — output chart

## Libraries
`yfinance` · `matplotlib` · `pandas`

## Findings
Over the 2-year period, Bitcoin dramatically outperformed both equity ETFs, with $100 growing to approximately $630 at its peak before closing near $570. However, this came with significant volatility — BTC dropped sharply in mid-2024 before surging again in Q4 2024.

QQQ returned approximately 2x over the period, driven by the AI-related rally in Nasdaq tech stocks. SPY delivered steady but more modest growth of around 60%.

The chart illustrates the classic risk-return tradeoff: higher potential returns from crypto come with far greater drawdowns and uncertainty compared to diversified equity ETFs.

## Key Concepts
- **Normalisation** — dividing by the first price to compare assets on the same scale
- **Cumulative return** — total growth from the starting investment
- **Risk-return tradeoff** — higher returns typically require accepting higher volatility