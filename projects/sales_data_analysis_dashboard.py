import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

n = 500

data = {
    'Order_ID' : range(1, n+1),
    'Product' : np.random.choice(['Laptop', 'Mobile', 'Tablet', 'Headphones'], n),
    'City' : np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Pune'], n),
    'Quantity' : np.random.randint(1, 10, n),
    'Price' : np.random.randint(500, 50000, n),
    'Month' : np.random.choice(['January', 'February', 'March', 'April', 'May', 'June'], n)
}

df = pd.DataFrame(data)

df['Revenue'] = df['Quantity'] * df['Price']

# print(df.head())

# print(df.info())

# print(df.describe())

# print(df.isnull().sum())

product_sales = df.groupby('Product')['Revenue'].sum()

# print(product_sales)


# plt.figure(figsize=(10, 6))
# product_sales.plot(
#     kind='bar',
#     color='skyblue'
# )

# plt.title('Total Revenue by Product')
# plt.xlabel('Product')
# plt.ylabel('Total Revenue')

# plt.show()

city_revenue = df.groupby('City')['Revenue'].sum().reset_index()

# plt.figure(figsize=(8, 5))

# sns.barplot(
#     data=city_revenue,
#     x='City',
#     y='Revenue',
#     palette='viridis'
# )

# plt.title('Total Revenue by City')
# plt.show()

month_revenue = df.groupby('Month')['Revenue'].sum().reset_index()

# plt.figure(figsize=(10, 5))
# sns.lineplot(
#     data=month_revenue,
#     x='Month',
#     y='Revenue',
#     marker='o',
#     color='coral'
# )
# plt.title('Total Revenue by Month')
# plt.show()

# plt.figure(figsize=(6, 4))

# corr = df[['Quantity', 'Price', 'Revenue']].corr()

# sns.heatmap(
#     corr,
#     annot=True,
#     cmap='coolwarm',
# )

# plt.title('Correlation Heatmap')
# plt.show()


plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,x='Quantity',
    y='Revenue',
    hue='Product',
)

plt.title('Revenue vs Quantity by Product')
plt.show()