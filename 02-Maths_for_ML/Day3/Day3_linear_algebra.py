# Linear Transformations

# Linear Independence : No vector in the basis can be written as a linear combination of the others.

# Rank
# The rank of a matrix 𝐴 is the dimension of the vector space spanned by its columns (or equivalently, its rows).

"""
R2 = [1 0
      0 1] # Basic standard of R2

R3 = [1 0 0
      0 1 0
      0 0 1] # Basic standard of R3

"""
import numpy as np

# NumPy Example: Checking for a Basis

v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])

A = np.column_stack((v1,v2, v3))

Rank = np.linalg.matrix_rank(A)

print("Rank of matrix : \n", Rank)


v1 = np.array([1,2])
v2 = np.array([2,4])

A = np.column_stack((v1, v2))
Rank = np.linalg.matrix_rank(A)
print("Matrix rank : \n", Rank)

v1 = np.array([1, 2, 3])
v2 = np.array([2,4,6])
v3 = np.array([9,8,10])

A = np.column_stack((v1,v2,v3))
Rank = np.linalg.matrix_rank(Rank)
print("Rank of Matrix : \n", Rank)