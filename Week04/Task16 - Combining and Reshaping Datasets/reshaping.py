import pandas as pd
import numpy as np

# reshape in numpy 
""" a = np.arange(1, 10) 
print(a)
print(a.reshape(3, 3)) # reshape to 3x3 matrix
print(a.reshape(9,)) # transpose the matrix
# reshape to column vector
print(a.reshape(9, 1)) 
"""

df = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['A', 'B', 'C'])
print(df)

# reshape in pandas
print("---------------------------------------------")
# stack # rotates or pivots the data from the columns into rows
result = df.stack()
print(result)
print("---------------------------------------------")

# unstack # rotates or pivots the data from the rows into columns
print(df.unstack())
print("---------------------------------------------")

# unstacking a specific level
print(df.unstack(0)) # unstack level 0 (row index) into columns
print("---------------------------------------------")
print(df.unstack(1)) # unstack level 1 (column index) into columns

print("---------------------------------------------")
# stacking with missing values
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df)
print("---------------------------------------------")
df2 = df.iloc[:2, :2] # get first 2 rows and first 2 columns
print(df2)
print("---------------------------------------------")
print(df2.stack())
print("---------------------------------------------")
new_df = pd.concat([df2, pd.DataFrame(columns=['D'])]) # add a new column
print(new_df)
print("---------------------------------------------")
print(new_df.stack())
print("---------------------------------------------")
print(new_df.stack(dropna=False)) # keep the NaN values

# unstacking in dataframe 
print("---------------------------------------------")
df = pd.DataFrame({'L1': {0: 'A', 1: 'B', 2: 'C'},
                     'L2': {0: 1, 1: 2, 2: 2},
                        'C': {0: 2, 1: 4, 2: 5}})
print(df)
print("---------------------------------------------")
print(df.set_index(['L1', 'L2']).unstack('L1')) # unstack L1 into columns
print("---------------------------------------------")

# pivoting long to wide
# means to convert a dataframe from a long format to a wide format
print("---------------------------------------------")
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                        'B': {0: 1, 1: 3, 2: 5},    
                        'C': {0: 2, 1: 4, 2: 6}})
print(df)
print("---------------------------------------------")
print(df.pivot(index='A', columns='B', values='C')) # pivot C into columns
print("---------------------------------------------")

# pivoting wide to long
# means to convert a dataframe from a wide format to a long format
print("---------------------------------------------")
df = pd.DataFrame({'A': ['a', 'b', 'c'],

'B': [1, 3, 5],

'C': [2, 4, 6],

'D': [1, 2, 3]})

print(df)
print("---------------------------------------------")
print(pd.melt(df, id_vars=['A', 'B'], value_vars=['C', 'D'])) 
# melt C and D into rows with A and B as identifiers
print("---------------------------------------------")




