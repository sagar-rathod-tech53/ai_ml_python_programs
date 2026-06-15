import numpy as np
import pandas as pd

data = pd.read_csv("Students.csv")

data["add all marks"] = data["math score"] + data["reading score"] + data["writing score"]

top_performer = data.groupby("gender")[["math score", "reading score", "writing score", "add all marks"]].max().round(2).reset_index()

print("Top Performar student is :: \n",top_performer)