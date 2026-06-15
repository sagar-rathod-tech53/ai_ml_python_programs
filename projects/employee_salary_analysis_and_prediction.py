import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

n = 500

df = pd.DataFrame({
    'Employee_ID' : range(1, n+1),
    'Age' : np.random.randint(21, 60, n),
    'Experience' : np.random.randint(1, 20, n),
    'Department' : np.random.choice(
        [
            'IT', 'HR', 'Finance', 'Marketing'
        ],
        n
    ),
    'Performance_Score' : np.random.randint(60, 100, n)
})

df['Salary'] = (
    20000 + 
    df['Experience'] * 5000 +
    df['Performance_Score'] * 1000 +
    np.random.randint(-10000, 10000, n)
)

print(df.head(10))


dept_salary = (
    df.groupby('Department')['Salary'].mean().reset_index()
)

print(dept_salary)


# plt.figure(figsize=(8, 5))
# sns.barplot(
#     data=dept_salary,
#     x='Department',
#     y='Salary',
#     palette='Set2'
# )

# plt.title('Average Salary by Department')
# plt.show()


# plt.figure(figsize=(8, 5))
# sns.scatterplot(
#     data=df,
#     x='Experience',
#     y='Salary',
#     hue='Department',
# )

# plt.title('Salary vs Experience by Department')
# plt.show()


# corr = df[['Age', 'Experience', 'Performance_Score', 'Salary']].corr()

# plt.figure(figsize=(6, 4))
# sns.heatmap(
#     corr,
#     annot=True,
#     cmap='coolwarm',
#     fmt='.2f'
# )
# plt.title('Correlation Matrix')
# plt.show()

# plt.figure(figsize=(8, 5))
# sns.boxplot(
#     y=df['Salary']
# )

# plt.title("Salary Outliers")
# plt.show()

top10 = df.sort_values(by='Salary', ascending=False).head(10)

print(top10)

plt.figure(figsize=(10, 5))

sns.boxplot(
    data=top10,
    x='Department',
    y='Salary',)

plt.title('Top 10 Salaries by Department')
plt.show()


avg_salary = df['Salary'].mean()

high_paid = df[
    df['Salary'] > avg_salary
]

print(high_paid.head())