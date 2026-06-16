import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("employee_attrition.csv")

# Basic Information
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Attrition Count
plt.figure(figsize=(6,4))
sns.countplot(x='Attrition', data=df)
plt.title('Employee Attrition Count')
plt.show()

# Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', hue='Attrition', data=df)
plt.title('Gender vs Attrition')
plt.show()

# Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.show()

# Monthly Income Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['MonthlyIncome'], bins=30, color='green')
plt.title('Monthly Income Distribution')
plt.show()

# Job Role Analysis
plt.figure(figsize=(12,6))
sns.countplot(
    y='JobRole',
    hue='Attrition',
    data=df
)
plt.title('Attrition by Job Role')
plt.show()

# Correlation Matrix
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(12,8))
sns.heatmap(
    numeric_df.corr(),
    cmap='coolwarm',
    annot=False
)
plt.title('Correlation Heatmap')
plt.show()

# Attrition by Overtime
plt.figure(figsize=(6,4))
sns.countplot(
    x='OverTime',
    hue='Attrition',
    data=df
)
plt.title('Overtime vs Attrition')
plt.show()

# Monthly Income by Attrition
plt.figure(figsize=(8,5))
sns.boxplot(
    x='Attrition',
    y='MonthlyIncome',
    data=df
)
plt.title('Income vs Attrition')
plt.show()

# Average Age by Attrition
avg_age = df.groupby('Attrition')['Age'].mean()

print("\nAverage Age:")
print(avg_age)

# NumPy Analysis
income_mean = np.mean(df['MonthlyIncome'])
income_median = np.median(df['MonthlyIncome'])
income_std = np.std(df['MonthlyIncome'])

print("\nIncome Statistics")
print("Mean:", income_mean)
print("Median:", income_median)
print("Standard Deviation:", income_std)

# Top Factors Correlated with Attrition
corr = numeric_df.corr()

print("\nCorrelation with Monthly Income:")
print(corr['MonthlyIncome'].sort_values(ascending=False).head(10))