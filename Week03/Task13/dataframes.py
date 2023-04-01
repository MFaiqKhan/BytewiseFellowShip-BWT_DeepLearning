import pandas as pd
import numpy as np

# DataFrame: Is a 2D labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
# It is generally the most commonly used pandas object.
# Like Series, DataFrame accepts many different kinds of input:
# Dict of 1D ndarrays, lists, dicts, or Series
# 2-D numpy.ndarray
# Structured or record ndarray
# A Series
# Another DataFrame
# NumPy MaskedArray



# Creating a DataFrame from a dictionary of Series objects
# The keys of the dictionary are the column names and the values are the data.
# The index of the DataFrame is the union of the indexes of the Series objects.

data = {'Car': ['BMW', 'Audi', 'Toyota', 'Honda', 'Nissan'],
    'Type': ['Sedan', 'SUV', 'Sedan', 'Sedan', 'SUV'],
    'Price': [100000, 120000, 80000, 90000, 110000]}
df = pd.DataFrame(data)

print('dataframe from a dictionary of Series objects', df)

# using head and tail methods to display the first and last 5 rows of the DataFrame
print('head', df.head())
print('tail', df.tail())

# specifying the number of rows to display 
print('head', df.head(3))

# using colmumn to arrange the columns of the DataFrame
df1 = pd.DataFrame(data, columns=['Car', 'Price', 'Type'])
print('dataframe with columns rearranged', df1)

# passing a column that isn't contained in the dict, it will appear with missing values in the result
df2 = pd.DataFrame(data, columns=['Car', 'Price', 'Type', 'Year'])
print('dataframe with a column that isn\'t contained in the dict', df2)

# accessing a column of the DataFrame as a Series
print('accessing a column of the DataFrame', df['Car']) # using dictionary style
print('accessing a column of the DataFrame', df.Car) # using attribute style

# accessing a row of the DataFrame as a Series
print('accessing a row of the DataFrame', df.loc[0]) # using loc method to access a row of the DataFrame

# assigning the empty column 'Year' to a Series
df2['Year'] = pd.Series([2018, 2019, 2017, 2016, 2015], index=[0, 1, 2, 3, 4])
print('dataframe with a column assigned to a Series', df2)

# assigning the empty column 'Year' to a scalar value
df2['Year'] = 2020
print('dataframe with a column assigned to a scalar value', df2)

# assigning a column that doesn't exist will create a new column
df2['BMW'] = df2.Car == 'BMW'
print('dataframe with a column assigned to a scalar value', df2)
print('dataframe with a column assigned to a scalar value', df2.columns)

# deleting a column
del df2['BMW']
print('dataframe with a column deleted', df2.columns)

# using the pop method to delete a column
df2.pop('Year')
print('dataframe with a column deleted', df2.columns)

# transpose the DataFrame, rows become columns and columns become rows
print('transpose the DataFrame', df2.T)

# using the describe method to display a summary of the DataFrame
print('summary of the DataFrame', df2.describe())

# values attribute to display the data contained in the DataFrame as a 2D ndarray
print('data contained in the DataFrame', df2.values)
