import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os

print("Current Directory:", os.getcwd())
print("Files:", os.listdir())

df = pd.read_csv("sales_data.csv")
print(df.head())
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("Dataset :: ")

print(df)

total_revenue = df["Revenue"].sum()
print(f"Total Revenue: {total_revenue}")

product_revenue = df.groupby('Product')['Revenue'].sum().reset_index()
print("Product Revenue :: ")
print(product_revenue)

region_revenue = df.groupby('Region')['Revenue'].sum().reset_index()
print("Region Revenue :: ")
print(region_revenue)

# Region Revenue Chart
plt.figure(figsize=(10, 6))

sns.barplot(
    data=region_revenue,
    x="Region",
    y="Revenue",
    hue="Region",
    legend=False,
    palette="magma"
)

plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(
    df["Revenue"], bins=5,kde=True, color="skyblue"
)

plt.title("Revenue Distribution")
plt.show()


plt.figure(figsize=(10, 6))
sns.heatmap(
    df[['Units_Sold', 'Unit_Price', 'Revenue']].corr(),
    annot=True,
    cmap='coolwarm',

)
plt.title("Correlation Matrix")
plt.show()