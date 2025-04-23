#!/usr/bin/env python3

#
# University of Lincoln, School of Computer Science
# CMP9139 Research Methods
# Workshop Week 2
# 2024-2025
# Dr Paul Baxter
#

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

print()
print("CMP9139 Research Methods Workshop 2")
print()

data = pd.read_csv("data-2.csv")
# QUESTION 1:
# - ensure you understand the concept of DataFrame from last workshop...
# - what is the structure of the csv file assumed to be?
# print(data)
# print()

# view the types of the data in the DataFrame
# print(data.dtypes)
# print()

# QUESTION 2:
# - Are the following two printouts useful for anything?
# - Uncomment to see what they display
# print(data["Condition"])
# print(data["Data"])

# split the data by condition
conditionOne = data[data.Condition == "Group1"]
# print(conditionOne)
conditionTwo = data[data.Condition == "Group2"]
# print(conditionTwo)
# print()

# information about the conditions using pandas
# print("Info about conditionOne (pandas):")
# print(conditionOne.info())
# print()
# print("Info about conditionTwo (pandas):")
# print(conditionTwo.info())
# print()

# # information about the conditions using scipy
print("Info about conditionOne (scipy):")
print(stats.describe(conditionOne["Data"]))
print()
print("Info about conditionTwo (scipy):")
print(stats.describe(conditionTwo["Data"]))
# print()


# # basic mean of each condition
# print()
# print("Group 1 mean: ", conditionOne["Data"].mean())
# print("Group 2 mean: ", conditionTwo["Data"].mean())
# # QUESTION 3:
# # - how would you display the median or mode of the data?
# # - you should refer to the DataFrame documentation...
# # - e.g. see: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html
#
# # simple scatter plot of all data by condition
# data.plot.scatter(x="Condition", y="Data")
# plt.show()
#
# # histogram of all data - no distinction between conditions
# ax = data.plot.hist(bins=10, alpha=0.5)
# ax.set_xlabel("Data Value")
# ax.set_ylabel("Frequency")
# plt.show()
#
# # histograms of both conditions on single axes
# plt.hist(
#     conditionOne["Data"],
#     edgecolor="black",
#     color="green",
#     bins=10,
#     label="Group1",
#     alpha=0.5,
# )
# plt.hist(
#     conditionTwo["Data"],
#     edgecolor="black",
#     color="blue",
#     bins=10,
#     label="Group2",
#     alpha=0.5,
# )
# plt.legend(loc="upper right")
# plt.show()
# # QUESTION 4:
# # - examine the histograms: what characterisics do they have? e.g. shape, skew, etc
# # - compare with the characteristics covered in the lecture
#
# # individual boxplots by condition
# ax = conditionOne.boxplot()
# ax.set(xlabel="Group One", ylabel="Data Value")
# plt.show()
# ax = conditionTwo.boxplot()
# ax.set(xlabel="Group Two", ylabel="Data Value")
# plt.show()
#
# # boxplot of data from both conditions side by side
# print()
# # QUESTION 5:
# # - look at the relationship between the boxplots and the histograms...
# # - what are their relative uses? is one more informative than the other?
#
# # descriptive stats
print("Group 1 description:")
print(conditionOne.describe())
print()
print("Group 2 description:")
print(conditionTwo.describe())
print()
boxdata = [conditionOne["Data"], conditionTwo["Data"]]
plt.boxplot(
    boxdata,
    labels=["Group1", "Group2"],
)
plt.show()
# # QUESTION 6:
# # - what statistics are covered here?
# # - relate this in particular to the boxplots
#
#
# print()
#

