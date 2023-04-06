import pandas as pd
import numpy as np

# Outlier detection
# Outliers are the values that are far away from the other values in the data set
# Outliers can be detected using the following methods:
# 1. Z-score method
# 2. IQR method
# 3. Box plot method
# 4. Scatter plot method


# lets consider a normally distributed data set
# we will generate a random data set with 1000 values
df = pd.DataFrame(np.random.randn(1000, 4)) # 1000 rows and 4 columns of random numbers
print(df.head())
print("---------------------------------------------")
print(df.describe()) # describe method gives the statistical summary of the data set

print("---------------------------------------------")

# find values exceeding 3 in one column
col = df[1] # select the second column
print(col[np.abs(col) > 3]) # find the values exceeding 3 in the second column

print("---------------------------------------------")

# find values exceeding 3 in all columns
print(df[(np.abs(df) > 3).any(1)]) # find the values exceeding 3 in all columns and print the rows
# any(1) means any row that has a value exceeding 3 

""" 
The code selects all rows of a pandas DataFrame 'data' in which the absolute
value of any element in the row is greater than 3. 
The first part of the code, np.abs(data) > 3, 
creates a boolean DataFrame where True indicates that the 
absolute value of the corresponding element is greater than 3, 
and False otherwise. Then, the any(1) method is used to check 
if there is at least one True value in each row of the DataFrame. 
If so, the row is selected and returned as a new DataFrame.
So, the output of this code shows all the rows in which at least one element 
has an absolute value greater than 3 or less than -3.
"""

print("---------------------------------------------")

# replace the values exceeding 3 with 3
df[np.abs(df) > 3] = np.sign(df) * 3 # replace the values exceeding 3 with 3
# np.sign(df) returns the sign of the values in the data frame 
# np.sign(df) * 3 returns the sign of the values in the data frame multiplied by 3
print(df.describe()) # describe method gives the statistical summary of the data set

print("---------------------------------------------")

print(np.sign(df).head()) # returns the sign of the values in the data frame
# it returns 1 for positive values, 0 for zero and -1 for negative values