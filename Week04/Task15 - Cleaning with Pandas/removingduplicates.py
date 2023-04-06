import numpy as np
import pandas as pd

# create a dataframe with duplicate values
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                     'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'D': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
})

print(df)

print("-----------------------")

print(df.duplicated()) # check for duplicates in the dataframe
# returns a series of boolean values, True if the row is a duplicate and False if it is not a duplicate

print("-----------------------")

df1 = pd.DataFrame({'A' : [1, 1, 2, 3, 2, 3, 3, 1, 5],
                    'B' : [1, 1, 2, 3, 2, 3, 3, 1, 5],
                    'C' : [1, 1, 2, 3, 2, 3, 3, 1, 5],
                    })

print(df1)

print("-----------------------")

print(df1.duplicated()) # check for duplicates in the dataframe

print("-----------------------")
print(df1.drop_duplicates()) # remove duplicates from the dataframe, remove the first occurence of the duplicate

print("-----------------------")

df1['D'] = range(9) # will give valueerror if you add less than 9 values
print(df1) 
print("-----------------------")
print(df1.drop_duplicates(['A'])) # this will remove the duplicates in column A, but will keep the first occurence of the duplicate
""" 
   A  B  C  D
0  1  1  1  0
2  2  2  2  2
3  3  3  3  3
8  5  5  5  8
"""

print("-----------------------")

# keep the last occurence of the duplicate
print(df1.drop_duplicates(['A'], keep='last'))
"""
   A  B  C  D
4  2  2  2  4
6  3  3  3  6
7  1  1  1  7
8  5  5  5  8
"""