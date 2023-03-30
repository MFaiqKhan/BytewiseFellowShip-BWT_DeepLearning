import numpy as np

# create two matrices 

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 3x3 matrix 
print("A = ", A) 
#  [[1 2 3]
#   [4 5 6]
#   [7 8 9]]

B = np.array([[1, 2, 3], [4, 5, 6], [2,3,1]]) # 2x3 matrix
print("B = ", B)
#  [[1 2 3]
#   [4 5 6]
#  [2 3 1]]


# Matrix addition
C = A + B # cannot add matrices of different sizes 
print("C_addition = ", C)
# ValueError: operands could not be broadcast together with shapes (3,3) (2,3)  

# Matrix Multiplication : (Dot product of rows and columns)
C = np.dot(A,B)
print("C_multiplication = ", C)
# [[15 21 18]
#  [36 51 48]
#  [57 81 78]]


# Matrix Transpose
C = np.transpose(A)
print("C_transpose = ", C)
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]


# Matrix Determinant
C = np.linalg.det(A)
print("C_determinant = ", C)
# 0.0 # singular matrix 


# Matrix Inverse
# C = np.linalg.inv(A) # singular matrix , cannot find inverse
C = np.linalg.inv(B)
print("C_inverse = ", C)
# C_inverse =  [[-1.44444444  0.77777778 -0.33333333]
# [ 0.88888889 -0.55555556  0.66666667]
# [ 0.22222222  0.11111111 -0.33333333]]

# Matrix Rank
# Rank of a matrix is the number of linearly independent rows or columns of a matrix.
C = np.linalg.matrix_rank(A)
print("C_rank = ", C)
# 2

# Eigenvalues and Eigenvectors
# An eigenvector of a linear transformation is a nonzero vector that changes 
# at most by a scalar factor when that linear transformation is applied to it.

# The corresponding eigenvalue is the factor by which the eigenvector is scaled.
C = np.linalg.eig(A)
print("C_eigenvalues = ", C[0])
print("C_eigenvectors = ", C[1])

# C_eigenvalues =  [ 1.61168440e+01 -1.11684397e+00 -1.30367773e-15]
# C_eigenvectors =  [[-0.23197069 -0.78583024 -0.40824829]
#  [-0.52532209 -0.08675134  0.81649658]
#  [-0.8186735   0.61232756 -0.40824829]]





