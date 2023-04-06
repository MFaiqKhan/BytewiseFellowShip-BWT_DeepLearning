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


""" 
A z-score, also known as a standard score, 
is a measure of how many standard deviations a 
data point is from the mean of a distribution. 
The formula for calculating the z-score of a data point is:
z = (x - μ) / σ
where x is the data point, μ is the mean of the distribution, 
and σ is the standard deviation of the distribution. 
A positive z-score indicates that the data point is above the mean, 
while a negative z-score indicates that the data point is below the mean.
Z-scores are useful for identifying outliers in a dataset. 
Typically, data points with a z-score greater than 3 or less than -3 are considered to be outliers.
"""

# Create a sample DataFrame with outliers
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1212121],
    'B': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,99999]
})

# Calculate z-scores for each value in the DataFrame
z_scores = np.abs((df - df.mean()) / df.std())
print(z_scores)

# Keep only the rows that do not contain outliers
df_no_outliers = df[(z_scores < 3).all(axis=1)]

# Print the original DataFrame and the DataFrame with no outliers
print("Original DataFrame:\n", df)
print("\nDataFrame with no outliers:\n", df_no_outliers) 

# In this example, the z-scores are calculated using the formula (x - mean) / std,
#  where x is each value in the DataFrame, and mean and std are the mean and 
# standard deviation of the DataFrame, respectively. The boolean mask is then 
# created by selecting only the rows where all the z-scores are less than 3. 
# Finally, a new DataFrame is created with only the selected rows.