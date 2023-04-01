# Pandas : Is a library for data manipulation and analysis

import pandas as pd
import numpy as np

# Series in pandas is a one-dimensional labeled array capable of holding any data type

# Creating a series from a list
s = pd.Series([1, 3, 5, -1, 4])
print(s)

s.values # returns the values of the series s
print(s.values)

s.index # returns the index of the series s
print(s.index)

# creating Index objects manually and assigning them to a series
s = pd.Series([1, 3, 5, -1, 4], index=['a', 'b', 'c', 'd', 'e'])
print(s)

s['a'] # returns the value of the series s at index 'a'
print(s['a'])

s[['a', 'c', 'e']] # returns the values of the series s at indices 'a', 'c', and 'e'
print(s[['a', 'c', 'e']]) # passing a list of indices to the series s returns a series

s.index
print(s.index)


# using numpy functions on series
s = pd.Series([1, 3, 5, -1, 4])
# Filtering with boolean arrays
s[s > 0] # returns the values of the series s that are greater than 0
print(s[s > 0])

s[s > s.median()] # returns the values of the series s that are greater than the median of the series s
print(s[s > s.median()])

s * 2 # returns the values of the series s multiplied by 2
print(s * 2)

np.exp(s) # returns the exponential of the values of the series s
print(np.exp(s))


# Creating a series from a dictionary
d = {'a': 99, 'b': 100, 'c': 101, 'd': 102, 'e': 103}
s = pd.Series(d)
print(s)

# Series can be used as a fixed-length, ordered dict as it is a mapping of index values to data values
'b' in s # returns True if the index 'b' is in the series s
print('b' in s)

'f' in s # returns False if the index 'f' is not in the series s
print('f' in s)

# passing only a dictionary to the Series function, the index will have the dict’s keys in sorted order
numbers = ['gggg', 'b', 'c', 'd', 'e'] # here gggg won't be in the series s
ss = pd.Series(d, index=numbers)
print(s)

# isnull and notnull functions in pandas can be used to detect missing data
pd.isnull(s) # returns True if the value of the series s is null
print(pd.isnull(s))
print(s.isnull()) # instance method isnull() can also be used, similar to the isnull() function

pd.notnull(s) # returns True if the value of the series s is not null
print(pd.notnull(s))

# Series automatically aligns differently-indexed data in arithmetic operations
s + s # returns the sum of the values of the series s
print(s + ss) # here a is Nan because it is not in the series ss
# gggg is Nan because it is not in the series s


# altering the name of the series
s.name = 'numbers'
print(s)
s.index.name = 'letters'
print(s)

# altering the index of the series
s.index = ['A', 'B', 'C', 'D', 'E']
print(s)