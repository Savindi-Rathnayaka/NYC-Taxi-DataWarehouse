import pandas as pd

df = pd.read_parquet(
    "data/yellow_tripdata_2026-01.parquet"
)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())