from datetime import datetime
import yfinance as yf
import pandas as pd
import numpy as np

def datetime_to_datetime64ns(dt_obj):
  return np.datetime64(dt_obj)

stocks = set()

df = pd.read_csv("Test.csv")

for i in df["Symbol"]:
    stocks.add(i)
historical_stock_price = yf.download(stocks, start="2024-01-01", end="2025-01-07")

date_str = df["Date"][0]
date_object = datetime.strptime(date_str, "%m/%d/%Y").date()
date_object = date_object.strftime("%Y-%m-%d")

print(historical_stock_price.loc[date_object])



