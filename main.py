import math
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

data_path = "./btc-price-data.csv"
cache_path = "./btc-price-data.pkl"

if os.path.exists(cache_path):
    # Load pre-processed data from pickle cache
    data = pd.read_pickle(cache_path)
else:
    # Read only necessary columns and convert timestamp to datetime
    data = pd.read_csv(
        data_path,
        usecols=[
            "Timestamp",
            # "Open",
            # "High",
            # "Low",
            "Close",
        ],
        dtype={
            # "Open": np.float64,
            # "High": np.float64,
            # "Low": np.float64,
            "Close": np.float64,
        },
        converters={"Timestamp": lambda x: pd.to_datetime(float(x), unit="s")},
        index_col="Timestamp",
    )
    # Save to cache for future fast loading
    data.to_pickle(cache_path)

# Ensure data is sorted by datetime index
data.sort_index(inplace=True)

# Focus on daily data from 2015 to end of 2024
data = data[(data.index >= "2015-01-01") & (data.index < "2025-01-01")]

# Resample to daily frequency, using the last price of each day
data = data.resample("1D").last().dropna()

# Print sample data
# print(data.head())

# Rename columns for clarity
data.rename(columns={"Close": "price"}, inplace=True)

# Calculate daily logarithmic returns
data["log_return"] = np.log(data["price"] / data["price"].shift(1))
data.dropna(subset=["log_return"], inplace=True)

# Print Basic Info
print(data.info())
print()
print(data.head())
print()
description = stats.describe(data["log_return"])
print(description)
print("Standard Deviation: ", math.sqrt(description.variance))
print()

log_returns = data["log_return"]
log_returns_standardized = stats.zscore(log_returns)

print("Shapiro-Wilk:", stats.shapiro(log_returns))
print()
print("Kolmogorov-Smirnov:", stats.kstest(log_returns_standardized, "norm"))
print()
print("D’Agostino and Pearson:", stats.normaltest(log_returns))
print()
print("Jarque-Bera:", stats.jarque_bera(log_returns))
print()
print("Anderson-Darling:", stats.anderson(log_returns, "norm"))
print()

fig, axes = plt.subplots(
    1,
    2,
    figsize=(10, 8),
    gridspec_kw={"width_ratios": [4, 1]},
)

# Histogram
axes[0].hist(log_returns, bins=200, edgecolor="black")
axes[0].set_title("Histogram of Log Returns")
axes[0].set_xlabel("Log Return")
axes[0].set_ylabel("Frequency")
axes[0].grid(True)

# Box Plot
axes[1].boxplot(log_returns, vert=True)
axes[1].set_title("Box Plot")
axes[1].set_ylabel("Log Return")
axes[1].grid(True)

plt.tight_layout()
plt.show()


# Histogram with Overlaid Normal Curve
plt.figure(figsize=(8, 8))
plt.hist(
    log_returns_standardized,
    bins=100,
    density=True,
    alpha=0.6,
    color="skyblue",
    label="Standardized Log Returns",
)

x = np.linspace(-7, 6, 300)
plt.plot(x, stats.norm.pdf(x, 0, 1), "r", lw=2, label="Standard Normal PDF")

plt.title("Histogram of Standardized Log Returns with Normal Curve")
plt.xlabel("Z-score")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()

# Q-Q Plot
fig, ax = plt.subplots(figsize=(8, 8))
stats.probplot(log_returns_standardized, dist="norm", plot=ax)
ax.set_title("Q-Q Plot of Log Returns")
plt.tight_layout()
plt.show()
