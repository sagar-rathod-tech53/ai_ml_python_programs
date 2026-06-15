import numpy as np
import pandas as pd

data = pd.read_csv("Students.csv")
data["add all marks"] = data["math score"] + data["reading score"] + data["writing score"]

analysed_data = data.groupby("parental level of education")[["math score","reading score","writing score", "add all marks"]].mean().round(2).reset_index()
print("Analysed data :: \n",analysed_data)