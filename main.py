import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

# === Load Data Efficiently ===
data_path = "./btc-price-data.csv"
cache_path = "./btc-price-data.pkl"

if os.path.exists(cache_path):
    # Load pre-processed data from pickle cache
    data = pd.read_pickle(cache_path)
else:
    # Read only necessary columns and convert timestamp to datetime
    data = pd.read_csv(
        data_path,
        usecols=["Timestamp", "Close"],
        dtype={"Close": np.float64},
        converters={"Timestamp": lambda x: pd.to_datetime(float(x), unit="s")},
        index_col="Timestamp",
    )
    # Save to cache for future fast loading
    data.to_pickle(cache_path)

# Rename columns for clarity
data.rename(columns={"Close": "price"}, inplace=True)

# Ensure data is sorted by datetime index
data.sort_index(inplace=True)

# === Data Filtering and Preprocessing ===
# Focus on daily data from 2019 to end of 2023
data = data[(data.index >= "2019-01-01") & (data.index < "2024-01-01")]

# Resample to daily frequency, using the last price of each day
data = data.resample("1D").last().dropna()

# Calculate daily logarithmic returns
data["log_return"] = np.log(data["price"] / data["price"].shift(1))
data.dropna(subset=["log_return"], inplace=True)

# === Print Basic Info ===
print(data.info())
print()
print(data.head())
print()
print(stats.describe(data["log_return"]))
print()

# === Normality Tests ===
log_returns = data["log_return"]
log_returns_standardized = stats.zscore(log_returns)

print("D’Agostino and Pearson:", stats.normaltest(log_returns))
print()
print("Shapiro-Wilk:", stats.shapiro(log_returns))
print()
print("Kolmogorov-Smirnov:", stats.kstest(log_returns_standardized, "norm"))
print()
print("Jarque-Bera:", stats.jarque_bera(log_returns))
print()
print("Anderson-Darling:", stats.anderson(log_returns, "norm"))
print()

# === Combined Plot: Histogram + Box Plot ===
fig, ax = plt.subplots(
    2, 1, figsize=(10, 8), sharex=True, gridspec_kw={"height_ratios": [4, 1]}
)

# Histogram (top)
ax[0].hist(log_returns, bins=200, edgecolor="black")
ax[0].set_title("Histogram of Log Returns")
ax[0].set_ylabel("Frequency")
ax[0].grid(True)

# Box Plot (bottom)
ax[1].boxplot(log_returns, vert=False)
ax[1].set_xlabel("Log Return")
ax[1].grid(True)

plt.tight_layout()
plt.show()

# === Plot: Q-Q Plot & Histogram with Overlaid Normal Curve ===
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Q-Q Plot
stats.probplot(log_returns_standardized, dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot of Log Returns")

# Histogram with Normal Curve
x = np.linspace(log_returns.min(), log_returns.max(), 100)
pdf = stats.norm.pdf(x, log_returns.mean(), log_returns.std())
axes[1].hist(
    log_returns,
    bins=100,
    density=True,
    alpha=0.6,
    color="skyblue",
    label="Log Returns Histogram",
)
axes[1].plot(x, pdf, "r", lw=2, label="Normal PDF")
axes[1].set_title("Histogram with Normal Curve")
axes[1].legend()

plt.tight_layout()
plt.show()
