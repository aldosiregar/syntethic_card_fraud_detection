import pandas as pd

df = pd.read_csv("./../synthetic_financial_data.csv")

df.to_excel("synthetic_financial_data.xlsx", sheet_name="Financial Data", index=False)