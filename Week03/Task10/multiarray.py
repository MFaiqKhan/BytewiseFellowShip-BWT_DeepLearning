import numpy as np

# Create a 2D array of numbers from 0 to 9
data2 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]] # Create a list of numbers from 0 to 9
arr8 = np.array(data2) # Create a 2D array from data1 list, conversion from list to numpy array
print(arr8) # array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]])

# Display the number of dimensions of the array
print(arr8.ndim) # 2

# shape of array
print(arr8.shape) # (2, 10)  # 2 rows and 10 columns

# data type of array elements
print(arr8.dtype) # int32

# Zero array
arr9 = np.zeros((3, 10)) 
# array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], 
# [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], 
# [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
print(arr9)
print(arr9.dtype) # float64 (default data type for ones() and zeros() functions)

#