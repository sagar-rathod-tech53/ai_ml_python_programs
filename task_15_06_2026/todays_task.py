import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Students.csv")

data["add all marks"] = data["math score"] + data["reading score"] + data["writing score"]

average_marks = data["add all marks"].mean()
print("Students Average Marks is :: ",average_marks)

compared_data = data.groupby("gender")[["math score","reading score","writing score", "add all marks"]].mean().round(2).reset_index()
print("Compared data :: \n",compared_data)

analysed_data = data.groupby("parental level of education")[["math score","reading score","writing score", "add all marks"]].mean().round(2).reset_index()
print("Analysed data :: \n",analysed_data)

top_performer = data.groupby("gender")[["math score", "reading score", "writing score", "add all marks"]].max().round(2).reset_index()
print("Top Performar student is :: \n",top_performer)

# data["add all marks"].hist(bins=10)
# plt.title("Math Score Distribution")
# plt.xlabel("Score")
# plt.ylabel("Number of Students")
# plt.show()

sns.histplot(data=data, x="add all marks", hue="parental level of education", bins=10, kde=True)
plt.title("Math Score Distribution by Gender")
plt.show()