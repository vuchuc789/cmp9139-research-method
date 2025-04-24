#!/usr/bin/env python3

#
# University of Lincoln, School of Computer Science
# CMP9139 Research Methods
# Workshop Week 3
# 2024-2025
# Dr Paul Baxter
#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

print()
print("CMP9139 Research Methods Workshop 3")
print()

# This dataset comes from MASH:
#  https://guides.library.lincoln.ac.uk/mash/datasets
#  (it has been modified slightly for our use here...)
data = pd.read_csv("data-3.csv")
print()

# split the data by condition: what does this tell you?
Smith = data[data.Tutor == "Smith"]
print(Smith)
Dickens = data[data.Tutor == "Dickens"]
print(Dickens)
print()

# information about the conditions using scipy: what does this tell you?
print("Info about conditionOne (scipy):")
print(stats.describe(Smith["Combined"]))
print()
print("Info about conditionTwo (scipy):")
print(stats.describe(Dickens["Combined"]))
print()

# simple scatter plot of all data by condition
data.plot.scatter(x="Tutor", y="Combined")
plt.show()

# histograms of both conditions on single axes
plt.hist(
    Smith["Combined"],
    edgecolor="black",
    color="green",
    bins=10,
    label="Smith",
    alpha=0.5,
)
plt.hist(
    Dickens["Combined"],
    edgecolor="black",
    color="blue",
    bins=10,
    label="Dickens",
    alpha=0.5,
)
plt.legend(loc="upper right")
plt.show()

# boxplot of data from both conditions side by side
# - what does this tell you?
boxdata = [Smith["Combined"], Dickens["Combined"]]
plt.boxplot(
    boxdata,
    tick_labels=["Smith", "Dickens"],
)
plt.show()
print()

# test of normality for the two conditions
# - how to interpret these results?
# - what is the null hypothesis of this test?
# - look up the documentation for this command...
print("Smith: ", stats.normaltest(Smith["Combined"]))
print("Dickens: ", stats.normaltest(Dickens["Combined"]))
print()

# comparing the two distributions: H0 is that no difference between them
# - what does this outcome mean?
print(stats.ttest_ind(Smith["Combined"], Dickens["Combined"]))
print()

# How to interpret this result?

# Finally, 95% CI for each groups (not of difference between them...)
print(
    "Smith 95%CI: ",
    stats.t.interval(
        confidence=0.95,
        df=len(Smith["Combined"]) - 1,
        loc=np.mean(Smith["Combined"]),
        scale=stats.sem(Smith["Combined"]),
    ),
)
print(
    "Dickens 95%CI: ",
    stats.t.interval(
        confidence=0.95,
        df=len(Dickens["Combined"]) - 1,
        loc=np.mean(Dickens["Combined"]),
        scale=stats.sem(Dickens["Combined"]),
    ),
)

# Exercise - how to find the 95% CI of the difference of the means?

print()

