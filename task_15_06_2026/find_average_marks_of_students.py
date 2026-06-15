import numpy as np 
import pandas as pd


data = pd.read_csv("Students.csv")

# print("Data :: ")
# print(data)
# print("Full Information about dataset :: ", data.info)
# print("Full Description :: ",data.describe)
# print("Size of the dataset ::  ",data.shape)
# print("Check total null values :: ", data.isnull().sum())
# print("Check Duplicate values :: ",data.duplicated)


# print(data)
# print(data.isnull().sum())
# print(data.dropna())
# print(data.drop_duplicates())

# print(data.columns)
data["add all marks"] = data["math score"] + data["reading score"] + data["writing score"]

print("Updated Data :: ",data)
print("All Marks :: ",data["add all marks"])
average_marks = data["add all marks"].mean()
print("Students Average Marks is :: ",average_marks)