""" 
Linear Algebra Lab 0: Introduction to Python and NumPy
1. Install Python and NumPy
2. Vectors and Matrices
"""

# %% 1. Install Python and NumPy
#pip install numpy
import numpy as np
# 1.1 What is NumPy ?
# NumPy is a python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.

# %% 2. Vectors and Matrices
# 2.1 How to create a vector in python ?
# 2.1.0 What is vector ?
# A vector is a one-dimensional array of numbers. It can be represented as a row or column vector.
# 2.1.1 Create a row vector
row_vector = np.array([1, 2, 3])
print("Row Vector: ", row_vector)

# 2.1.2 Create a column vector
column_vector = np.array([[1], [2], [3]])
print("Column Vector: \n", column_vector)

# 2.1.3 Create a vector using arange
vector = np.arange(1, 10)
print("arange Vector: ", vector)

# 2.1.4 Create a vector using linspace
vector = np.linspace(1, 10, 5)
print("linear space Vector: ", vector)

# 2.1.5 Create a vector using random
vector = np.random.rand(5)
print("random Vector: ", vector)

# 2.1.6 Create a vector using zeros
vector = np.zeros(5)
print("Zero Vector: ", vector)

# 2.1.7 Create a vector using ones
vector = np.ones(5)
print("Ones Vector: ", vector)

# 2.1.8 Create a vector using full
vector = np.full(5, 3)
print("Full Vector: ", vector)

# 2.1.9 Create a vector using eye but output will be a matrix
vector = np.eye(5)
print("Eye Vector: \n", vector)

# 2.1.10 Create a vector using diag but output will be a matrix
vector = np.diag([1, 2, 3, 4, 5])
print("Diag Vector: \n", vector)

# 2.1.12 Create a vector using randint
vector = np.random.randint(1, 10, 5)
print("RandInt Vector: ", vector)

# 2.1.13 Create a vector using randn
vector = np.random.randn(5)
print("RandNormal Vector: ", vector)

# basic operation on vectors
# 2.2.1 Addition of two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
addition = vector1 + vector2
print("Addition of two vectors: ", addition)

# 2.2.2 Subtraction of two vectors
subtraction = vector1 - vector2
print("Subtraction of two vectors: ", subtraction)

# 2.2.3 Multiplication of two vectors
multiplication = vector1 * vector2
print("Multiplication of two vectors: ", multiplication)

# 2.2.4 Division of two vectors
division = vector1 / vector2
print("Division of two vectors: ", division)

# 2.2.5 Dot product of two vectors
# getting dot product of both the vectors 
# a . b = (a1 * b1 + a2 * b2 + a3 * b3) 
# a . b = (a1b1 + a2b2 + a3b3) 
dot_product = np.dot(vector1, vector2)
print("Dot product of two vectors: ", dot_product)

# 2.2.6 Cross product of two vectors
cross_product = np.cross(vector1, vector2)
print("Cross product of two vectors: ", cross_product)

# 2.2.7 Norm of a vector
norm = np.linalg.norm(vector1)
print("Norm of a vector: ", norm)


# 2.3.1 Scalar multiplication of a vector
# s * v = (s * v1, s * v2, s * v3) 
scalar = 2
scalar_multiplication = scalar * vector1
print("Scalar multiplication of a vector: ", scalar_multiplication)

# 2.3.2 Scalar division of a vector
scalar = 2
scalar_division = vector1 / scalar
print("Scalar division of a vector: ", scalar_division)

# 2.3.3 Scalar addition of a vector
scalar = 2
scalar_addition = scalar + vector1
print("Scalar addition of a vector: ", scalar_addition)

# 2.3.4 Scalar subtraction of a vector
scalar = 2
scalar_subtraction = scalar - vector1
print("Scalar subtraction of a vector: ", scalar_subtraction)




# %%
