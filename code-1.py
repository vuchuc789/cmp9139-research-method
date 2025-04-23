#!/usr/bin/env python3

#
# University of Lincoln, School of Computer Science
# CMP9139 Research Methods
# 2024-2025
# Dr Paul Baxter
#

import pandas as pd

print()
print("CMP9139 Research Methods Workshop 1")
print()

# ######################
# PART 1: FILE READING #
# ######################
# print()
# print(">> Manually opening and reading data file")
# print()
#
# # opening the file in read mode
# in_file = open("data-1.csv", "r")
#
# # # reading the file, then closing it
# input_data = in_file.read()
# in_file.close()
#
# # # splitting the text when newline ('\n') occurs
# data_into_list = input_data.split("\n")
# print(data_into_list)
# print()
#
# # # further splitting the strings
# data_list = []
# for l in data_into_list:
#     data_list += l.split(",")
# print(data_list)
# print()
#
# # # see just what conditions there are
# conditions = data_list[::2]
# print(conditions)
# print()

# Questions:
#   - how is the data presented?
#   - Is this useful?
#   - What would you need to do to use this data?

#
# print()


# ######################
# PART 2: USING PANDAS #
# ######################
print()
print(">> Using Pandas DataFrame")
print()

# read data into a pandas DataFrame structure
data = pd.read_csv("data-1.csv")

# data.plot(kind="scatter", x="Condition", y="Data")
# plt.show()

# view the data imported from the data file into a DataFrame
# print(data)
# print()

# # view the types of the data in the DataFrame
# print(data.dtypes)
# print()

# # view only the chosen data type
# print(data["Condition"])
# print(data["Data"])
# print()

# # split the data by condition and then view
# conditionOne = data[data.Condition == "Group1"]
# print(conditionOne)
# conditionTwo = data[data.Condition == "Group2"]
# print(conditionTwo)

# Questions:
#   - how is the data presented?
#   - Is this useful?
#   - How does this compare to reading manually from the data file?

#
