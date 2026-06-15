import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'C'],
    'Age': [20, np.nan, 25, 25]
})



print(df.isnull())
print(df)
# df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
# df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)