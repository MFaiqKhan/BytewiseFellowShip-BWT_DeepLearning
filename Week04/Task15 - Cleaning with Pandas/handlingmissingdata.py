import pandas as pd
import numpy as np

s_data = pd.Series(['Pakistan', 'Chile', np.nan , 'London'])
print(s_data)
# output
# 0    Pakistan
# 1       Chile
# 2         NaN
# 3      London
# dtype: object

# using isnull() function
print(s_data.isnull())
# output
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool

s_data[0] = None # None is also a missing value and treated as NaN/NA .
print(s_data.isnull())
# output
# 0     True
# 1    False
# 2     True
# 3    False
# dtype: bool

from numpy import nan as NA # here NA is alias of NaN

s_data = pd.Series([1, 99,1, 3.5, NA, NA])
print(s_data) # output: 0     1.0 1 99.0 2 1.0 3 3.5 4 NaN 5 NaN dtype: float64

# using dropna() function, it will drop all rows with missing values
print(s_data.dropna())
# output
# 0     1.0
# 1    99.0
# 2     1.0
# 3     3.5
# dtype: float64

print(s_data[s_data.notnull()]) # output: 0 1.0 1 99.0 2 1.0 3 3.5 dtype: float64
# above code will return all rows with non-missing values , same as dropna() function


# dataFrame with missing values----------------

df_data = pd.DataFrame([[1, 99, 1, 3.5, NA, NA], [2, 99, 1, 3.5, NA, NA], [3, 99, 1, 3.5, NA, NA]])
print(df_data)
# output
#    0   1  2    3   4   5
# 0  1  99  1  3.5 NaN NaN
# 1  2  99  1  3.5 NaN NaN
# 2  3  99  1  3.5 NaN NaN

# using dropna() function, it will drop all rows with missing values
print(df_data.dropna())
# output
# Empty DataFrame
# Columns: [0, 1, 2, 3, 4, 5]
# Index: []

df_data = pd.DataFrame([[2, 99, 1, 3.5,4 , 2.5], [2, 99, NA, 3.5, 1, NA], [3, NA, 1, 3.5, 7.0, NA]])
print(df_data)
# output
#    0   1    2    3    4    5
# 0  2  99  1.0  3.5  4.0  2.5
# 1  2  99  NaN  3.5  1.0  NaN
# 2  3  NA  1.0  3.5  7.0  NaN

print("------------------------------")
print(df_data.dropna())
# output
#    0     1    2    3    4    5
# 0  2  99.0  1.0  3.5  4.0  2.5

#how='all' will drop all rows with all missing values , 
# if any row has one non-missing value then it will not drop that row

print("------------------------------")
print(df_data.dropna(how='all'))

print("------------------------------")

df_data[4] = NA # adding NA in 4th column
print(df_data)

print("------------------------------")
print(df_data.dropna(how='all', axis=1)) # axis=1 means columns , axis=0 means rows , default is axis=0
# drop all columns with all missing values , if any column has one non-missing value then it will not drop that column
print("------------------------------")

# thresh is used to specify minimum number of non-missing values for a row/column to be kept
print(df_data.dropna(thresh=4)) # it will drop all rows with less than 4 non-missing values
# dropped 2nd row because it has only 3 non-missing values
# and first row has 3 non-missing values
# only zeroth row has 4 non-missing values

print("------------------------------")

