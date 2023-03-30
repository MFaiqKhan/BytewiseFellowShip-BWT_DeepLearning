import numpy as np

arr = np.array([[1,3.4,4.1], [2.2,3.5,4.2], [3.3,4.6,5.3]])
print(arr) # array([[1. , 3.4, 4.1], [2.2, 3.5, 4.2], [3.3, 4.6, 5.3]])
print(arr.shape) # (3, 3)  # 3 rows, 3 columns
print(arr.dtype) # float64
print(arr.ndim) # 2

# Multiply all elements by 2
print(arr * 2) # array([[ 2. , 6.8, 8.2], [ 4.4, 7. , 8.4], [ 6.6, 9.2, 10.6]])

# Add 1 to all elements
print(arr + 1) # array([[2. , 4.4, 5.1], [3.2, 4.5, 5.2], [4.3, 5.6, 6.3]])

# Add two arrays
arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr + arr2) # array([[ 2. , 5.4, 7.1], [6.2, 8.5, 10.2], [10.3, 12.6, 14.3]])

# Multiply two arrays
print(arr * arr2) # array([[ 1. , 6.8, 12.3], [8.8, 17.5, 25.2], [23.1, 36.8, 48.7]])
