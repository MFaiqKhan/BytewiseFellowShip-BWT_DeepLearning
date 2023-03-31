# Broadcasting in numpy arrays is a very useful feature that allows us to perform 
# operations on arrays of different shapes.

# broadcasting using scalar values
import numpy as np
a = np.array([1, 2, 3, 4])
b = 2
print(a + b)
# [3 4 5 6] 
# here the scalar value 2 is broadcasted to all the elements of the array a and then added to each element of the array a

b = np.array([2, 2, 2, 2])
print(a * b)
# [4 4 4 4]

# demeaning an array using broadcasting 
# demeaning is the process of subtracting the mean of an array from each element of the array

arr = np.random.randn(4, 3) # 4 rows and 3 columns having random values from a standard normal distribution
print(arr)

# The axis=0 argument specifies that we want to calculate the mean along each column.
col_means = arr.mean(axis=0) # mean of each column of the array arr in a 1D array
print(col_means) 

# Broadcasting the mean of each column to each column of the array arr
demeaned = arr - col_means
print(demeaned)

print(demeaned.mean(axis=0)) # mean of each column of the demeaned array


# Demeaning array using axis 1 (along each row)
arr_2 = np.random.randn(4, 3)
print(arr_2)
row_means = arr_2.mean(axis=1) # mean of each row of the array arr_2 in a 1D array
print(row_means)

# Broadcasting the mean of each row to each row of the array arr_2
demeaned_2 = arr_2 - row_means.reshape(4, 1) # reshaping the row_means array to a 4x1 array
print(demeaned_2)
# reshaping is necessary because the shape of the row_means array is (4,) 
# and the shape of the demeaned_2 array is (4, 3) and the two arrays cannot be subtracted from each other
# so we reshape the row_means array to a 4x1 array so that it can be broadcasted to the demeaned_2 array

print(demeaned_2.mean(axis=1)) # mean of each row of the demeaned_2 array.


# Adding an axis to an array using np.newaxis, for broadcasting:
arr_3 = np.ones((3,3)) # 3x3 array
print(arr_3) 
print(arr_3.shape) # (3, 3)
arr_3d = arr_3[:, np.newaxis, :] # adding an axis to the array arr_3
print(arr_3d)
print(arr_3d.shape) # (3, 1, 3)

arr1d = np.random.normal(size=3) # 1D array of size 3
print(arr1d)
print(arr1d.shape) # (3,)
arr2d = arr1d[:, np.newaxis] # adding an axis to the array arr1d
print(arr2d)
print(arr2d.shape) # (3, 1)

arr1d = arr1d[np.newaxis, :] # adding an axis to the array arr1d
print(arr1d)
print(arr1d.shape) # (1, 3)

# demeaning axis 2 in a 3D array
arr_3d = np.random.randn(2, 4, 5) # 2x4x5 array of random values from a standard normal distribution
print(arr_3d,'\n')

# demeaning axis 2
depth_means = arr_3d.mean(axis=2) # mean of each depth of the array arr_3d in a 2D array
print(depth_means,'\n')

# shape of the array arr_3d is (2, 4, 5) and the shape of the array depth_means is (2, 4)

# Broadcasting the mean of each depth to each depth of the array arr_3d
demeaned_3d = arr_3d - depth_means[:, :, np.newaxis] # adding an axis to the array depth_means
print(demeaned_3d,'\n')

print(depth_means[:, :, np.newaxis]) # mean of each depth of the depth_means array (error

print(demeaned_3d.mean(axis=2)) # mean of each depth of the demeaned_3d array



# Setting arrays values by broadcasting
print("------Setting arrays values by broadcasting------")
arr_4 = np.zeros((4, 3))
print(arr_4,'\n')
arr_4[:] = 5 # broadcasting the value 5 to all the elements of the array arr_4 and then assigning it to the array arr_4
print(arr_4,'\n') # all the elements of the array arr_4 are now 5

col = np.array([1.28, -0.42, 0.44, 1.6])
print(col[:, np.newaxis],'\n')
arr_4[:] = col[:, np.newaxis] # broadcasting the values of the array col to the array arr_4
print(arr_4,'\n') # all the elements of the array arr_4 are now the values of the array col

arr_4[:2] = [[-1.37], [0.509]] # broadcasting the values of the array [[-1.37], [0.509]] to the first two rows of the array arr_4
print(arr_4,'\n') # the first two rows of the array arr_4 are now [[-1.37], [0.509], [1.28], [-0.42]]

 