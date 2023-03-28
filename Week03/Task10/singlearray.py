import numpy as np

# Create a 1D array of numbers from 0 to 9
data1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Create a list of numbers from 0 to 9
arr1 = np.array(data1) # Create a 1D array from data1 list, conversion from list to numpy array
print(arr1) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 


# Display the number of dimensions of the array
print(arr1.ndim) # 1

# shape of array
print(arr1.shape) # (10,)  # 10 rows and 0 columns

# data type of array elements
print(arr1.dtype) # int32

# Zero array
arr2 = np.zeros(10) # array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
print(arr2)

# One array
arr3 = np.ones(10) # array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
print(arr3.dtype) # float64 (default data type for ones() and zeros() functions)
print(arr3)

# Empty array
# np.empty() function creates an array whose initial content is random and depends on the state of the memory
# can give unexpected results
arr4 = np.empty(10) # array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
print(arr4)
print(arr4.dtype) # float64

# zeros_like() function takes an existing array and produces a zeros array of the same shape and dtype
arr5 = np.zeros_like(arr1) # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(arr5)

# arange(), built in range function, but returns an array instead of a list

arr6 = np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr6)

# asarray() function converts input to an array but does not copy if the input is already an array means 
# if the input is already an array, it is passed through as is and no new object is created
arr7 = np.asarray(data1) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr7)


