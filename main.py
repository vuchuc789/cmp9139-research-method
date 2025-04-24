import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

# Define the path to the original CSV data file
data_path = "./btc-price-data.csv"
# Define the path to the cached pickle file
cache_path = "./btc-price-data.pkl"

# Check if the cached pickle file exists
if os.path.exists(cache_path):
    # If it exists, load the data from the pickle file
    data = pd.read_pickle(cache_path)
else:
    # If it doesn't exist, read the data from the CSV file
    data = pd.read_csv(
        data_path,
        dtype={
            # "Timestamp": np.float64,
            # "Open": np.float64,
            # "High": np.float64,
            # "Low": np.float64,
            "Close": np.float64,
            # "Volume": np.float64,
        },
        # parse_dates=["datetime"],
        converters={"Timestamp": lambda x: pd.to_datetime(float(x), unit="s")},
        usecols=["Timestamp", "Close"],
        index_col="Timestamp",
    )
    # Save the data to a pickle file for future use
    data.to_pickle(cache_path)

# Rename the columns for easier use
data.rename(columns={"Timestamp": "timestamp", "Close": "price"}, inplace=True)

# Sort the data by timestamp
data.sort_index(inplace=True)

data = data[(data.index >= "2019-01-01") & (data.index < "2024-01-01")]

# Resample to daily frequency, using the last Close of each day
data = data.resample("1D").last().dropna()

# Calculate the log returns
data["log_return"] = np.log(data["price"] / data["price"].shift(1))
# Remove rows with NaN values in the log_return column
data.dropna(subset=["log_return"], inplace=True)

# Print the data types of the columns
print(data.info())
# Print the first few rows of the data
print(data.head())
print(stats.describe(data["log_return"]))

print(stats.normaltest(data["log_return"]))

plt.figure(figsize=(10, 6))
plt.hist(data["log_return"], bins=200, edgecolor="black")
# plt.xlim(-0.4, 0.4)
plt.title("Histogram of Log Returns")
plt.xlabel("Log Return")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot(data["log_return"])
# plt.ylim(-0.4, 0.4)
plt.title("Box Plot of Log Returns")
plt.xlabel("Log Return")
plt.grid(True)
plt.show()
