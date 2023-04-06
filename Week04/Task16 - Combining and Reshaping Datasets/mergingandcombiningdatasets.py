import pandas as pd
import numpy as np

# database style DataFrame merging
# merge or join operations combine datasets by linking rows using one or more keys
# merge is a database style DataFrame join operation e.g. SQL
# merge is a function in the pandas namespace

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)
print("---------------------------------------------")
print(df2)
print("---------------------------------------------")

# many to one merge
merge  = pd.merge(df1, df2) # merge on common column
print(merge)

print("---------------------------------------------")
merge2 = pd.merge(df1, df2, on='key') # merge on common column 'key' and print
print(merge2)
print("---------------------------------------------")

# different column names
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df3)
print("---------------------------------------------")
print(df4)
print("---------------------------------------------")

merge3 = pd.merge(df3, df4, left_on='lkey', right_on='rkey') # merge on common column 'key' and print
print(merge3)
# by default merge does an inner join; the keys in the result are the intersection

print("---------------------------------------------")
merge4 = pd.merge(df1, df2, how='outer') # merge on common column 'key' and print
print(merge4)

print("---------------------------------------------")
# many to many merge

"""
In a many-to-one merge, one of the dataframes contains multiple rows with the same key, 
while the other dataframe contains only unique keys. This type of merge results in a dataframe 
with the same number of rows as the original dataframe with multiple rows with the same key, 
and additional columns from the second dataframe.
In contrast, in a many-to-many merge, both dataframes contain multiple rows with the same key. 
As a result, the resulting dataframe will have a number of rows that is 
equal to the product of the number of matching rows in each dataframe. 
This type of merge is useful when there are many-to-many relationships between the two dataframes, 
and you want to preserve all of the matching rows in the final result.
For example, consider two dataframes A and B, where A contains columns ['id', 'val'] and 
B contains columns ['id', 'category']:

A:
   id  val
0   1    2
1   2    4
2   3    6
3   1    3

B:
   id  category
0   1         A
1   1         B
2   2         A
3   3         C

A many-to-one merge on the 'id' column would result in:

merged = pd.merge(A, B, on='id')

   id  val category
0   1    2        A
1   1    2        B
2   1    3        A
3   1    3        B
4   2    4        A
5   3    6        C

Whereas a many-to-many merge would result in:

merged = pd.merge(A, B, on='id', how='outer')

   id  val category
0   1    2        A
1   1    2        B
2   1    3        A
3   1    3        B
4   2    4        A
5   3    6        C
6   2  NaN        A
7   3  NaN        C

Note that the many-to-many merge includes all possible combinations of matching rows between A and B, 
and includes NaN values where there are no matches.

"""

df3 = pd.DataFrame({'key': ['a','a','b','b','c','c'], 'value': range(6)})
df4 = pd.DataFrame({'key': ['a','b','b','d'], 'value': range(4)})
print(df3)
print("---------------------------------------------")
print(df4)
print("---------------------------------------------")

print(pd.merge(df3, df4, on='key', how='outer')) # merge on common column 'key' and print
print("---------------------------------------------")
print(pd.merge(df3, df4, on='key', how='inner')) # merge on common column 'key' and print
print("---------------------------------------------")



# merging with multiple keys
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                        'key2': ['one', 'two', 'one'],
                        'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                        'key2': ['one', 'one', 'one', 'two'],
                        'rval': [4, 5, 6, 7]})
print(left)
print("---------------------------------------------")
print(right)
print("---------------------------------------------")

print(pd.merge(left, right, on=['key1', 'key2'], how='outer')) # merge on common column 'key' and print
print("---------------------------------------------")

# overlapping column names
# overlapping column names are handled by suffixing the column names with _x and _y
# to make them unique
print(pd.merge(left, right, on='key1')) # here key2_x and key2_y are created to make the column names unique
print("---------------------------------------------")
# using suffixes
# suffixes can be specified to make the column names unique
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right'))) 
print("---------------------------------------------")

# merging on index
# merge can also be performed on the index
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                        'value': range(6)}) 
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b']) # index is a column in the dataframe 
print(left1)
print("---------------------------------------------")
print(right1)
print("---------------------------------------------")

print(pd.merge(left1, right1, left_on='key', right_index=True)) 
# right_index=True means that the index of the right dataframe is used as the key
# only the values of the index are used as the key of right dataframe while merging which is a and b
print("---------------------------------------------")

# outer join
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))
print("---------------------------------------------")

# hierarchical index
# merge can also be performed on the index of a dataframe with a hierarchical index
# means that the index of the dataframe is a multi-level index
# the merge is performed on the lowest level of the index

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                        'key2': [2000, 2001, 2002, 2001, 2002],
                        'data': np.arange(5.)}) # 5 rows and 3 columns, arange(5) returns 0 to 4
righth = pd.DataFrame(np.arange(12).reshape((6, 2)), # arange(12) returns 0 to 11
                        index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                                [2001, 2000, 2000, 2000, 2001, 2002]],
                        columns=['event1', 'event2'])

# right dataframe is represented as a multi-level index
# the first level of the index is the state and the second level is the year
# the index is used as the key for merging




print(lefth)
print("---------------------------------------------")
print(righth)
print("---------------------------------------------")

print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)) 
# merge on the common columns 'key1' and 'key2' and the index of the right dataframe
print("---------------------------------------------")
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'))


print("---------------------------------------------")

# concat function
# concat function is used to concatenate pandas objects along a particular axis
# the default axis is 0 which means that the objects are concatenated along the rows
# the axis can be set to 1 to concatenate along the columns

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
print(s1)
print("---------------------------------------------")
print(s2)
print("---------------------------------------------")
print(s3)
print("---------------------------------------------")

print(pd.concat([s1, s2, s3])) # concatenate along the rows
print("---------------------------------------------")

print(pd.concat([s1, s2, s3], axis=1)) # concatenate along the columns 
# produces a dataframe with NaN values where there are no values
print("---------------------------------------------")
# COMBINING DATA WITH OVERLAP
# pandas has a function combine_first which can be used to combine two datasets
# the data in the calling object is given preference

df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                        'b': [np.nan, 2., np.nan, 6.],
                        'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                        'b': [np.nan, 3., 4., 6., 8.]})
print(df1)
print("---------------------------------------------")
print(df2)
print("---------------------------------------------")

print(df1.combine_first(df2)) # combine the two dataframes 
# the data in df1 is given preference
# the data in df2 is used where there is no data in df1
# means that the dataframe we will get will have the data from df1 and df2\
# df1 data will be used where there is data in df1 and df2
# df2 data will be used where there is no data in df1 and there is data in df2
print("---------------------------------------------")



