"""
Choose the library you are most unfamiliar with and complete the tasks.

libraries:
- pandas (import pandas as pd)
- xarray (import xarray as xr)
- polars (import polars as pl)

We will use matplotlib for plotting, hint:
import matplotlib.pyplot as plt
"""
import polars as pl
"""
Load the data in trade.csv into a dataframe
"""
df = pl.read_csv("trade.csv")
print(type(df))

"""
Count the number of samples per trade region using polars
"""
number_of_samples_count = df.groupby("").count()
print(number_of_samples_count)
"""
Group by trade region and plot the mean trade per category in a bar chart
"""
number_of_samples_mean = df.groupby("").mean()
# print(number_of_samples_mean)

"""
Select those trade region with more than 5 samples. 
For that selection compute the standard deviation over the 'Agriculture' column.

"""
# filter the polars dataframe to only include those trade regions with more than 5 samples

df_more_than5 = number_of_samples_count.filter(pl.col("count")>5)
df_more_than5 = list(df_more_than5[""])

df_filtered = df.filter(pl.col("").is_in(df_more_than5))
# For that selection compute the standard deviation over the 'Agriculture' column.
df_std = df_filtered.groupby("").agg([pl.std("Agriculture")]) 