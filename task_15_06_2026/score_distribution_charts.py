import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Students.csv")

data["add all marks"] = data["math score"] + data["reading score"] + data["writing score"]

top_performer = data.groupby("gender")[["math score", "reading score", "writing score", "add all marks"]].max().round(2).reset_index()

print("Top Performar student is :: \n",top_performer)

data["add all marks"].hist(bins=10)
plt.title("Math Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.show()

sns.histplot(data=data, x="math score", hue="gender", bins=10, kde=True)
plt.title("Math Score Distribution by Gender")
plt.show()