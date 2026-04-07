# Moving Average Crossover — SPY

## What This Is
A simple visualisation of the 50-day and 200-day moving average 
crossover on SPY (S&P 500 ETF) from 2023 to 2025.

## What a Moving Average Is
A moving average smooths out daily price noise by averaging the 
closing price over a rolling window. The 50-day MA tracks short-term 
trend. The 200-day MA tracks long-term trend.

## What a Crossover Signals
When the 50-day MA crosses above the 200-day MA (called a Golden Cross) 
it is traditionally read as a bullish signal. When it crosses below 
(Death Cross) it is bearish. These signals are used by real traders 
as a basic momentum indicator.

## What I Found
Spy did not have any crossovers. 200-Day moving average remained consistently lower then the
50 day moving average.

## How to Run
```bash
pip install yfinance matplotlib pandas
python moving_average.py
```

## Libraries Used
- yfinance — pull real stock market data
- matplotlib — plot the chart
- pandas — handle the data table