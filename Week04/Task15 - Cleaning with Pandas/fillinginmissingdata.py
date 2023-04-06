import numpy as np 
import pandas as pd

s_data = pd.Series(['Pakistan', 'Chile', np.nan, 'London'])
print(s_data)
print("-----------------------")
print(s_data.isnull())

# fill missing data with a string
s_data = s_data.fillna('NewYork')
print(s_data)
print("-----------------------")
print(s_data.isnull())

print("-----------------------")

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = np.nan # set 2nd column 3rd row and below to NaN values 
df.iloc[4:, 2] = np.nan # set 3rd column 5th row and below to NaN values
print(df)
print("-----------------------")

# fill missing data with a value
df_new = df.fillna(0)
print(df_new)
print("-----------------------")

# filling with dictionary
df_n = df.fillna({1: 0.5, 2: 0}) # fill 1st column with 0.5 and 2nd column with 0
print(df_n)
print("-----------------------")

# fillna returns a new object, but you can modify the existing object
df.fillna(9, inplace=True)
print(df)
print("-----------------------")

new_data = pd.Series([np.nan, 2., np.nan, 4., 5.])
print(new_data)

print(new_data.fillna(new_data.mean())) # fill missing values with mean of the series

# forward and backward fill means that we can use the previous value to fill the next value
print(new_data.fillna(method='ffill', limit=2)) # forward fill, limit=2 means fill 2 missing values
print(new_data.fillna(method='bfill')) # backward fill