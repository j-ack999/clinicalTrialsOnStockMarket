import yfinance as yf
import pandas as pd

df = yf.download("MRNA", start="2020-01-01", end="2024-01-01")
print(df.head())