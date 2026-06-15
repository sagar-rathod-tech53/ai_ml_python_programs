import numpy as np 
import pandas as pd 
# import matplotlib.plot as plt

data = pd.read_csv("Students.csv")

# print(data["gender"].head())
# compared_data = data.groupby("gender").apply(lambda x: (x["y_true"] == x["y_pred"]).mean())

# print("Compared data Male and Female :: ",compared_data)
# males = data["gender"] == "male"
# females = data["gender"] == "female"
# print("Total Male :: ",males.mean())
# print("Total Female :: ",females.mean())
data["add all marks"] = data["math score"] + data["reading score"] + data["writing score"]

compared_data = data.groupby("gender")[["math score","reading score","writing score", "add all marks"]].mean().round(2).reset_index()

print("Compared data :: \n",compared_data)