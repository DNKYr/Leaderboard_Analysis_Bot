import yfinance as yf
import pandas as pd

stocks = set()

df = pd.read_csv("Test.csv")

for i in df["Symbol"]:
    stocks.add(i)

data = yf.download(stocks, start="2024-01-01", end="2025-01-07")
print(data[0])


