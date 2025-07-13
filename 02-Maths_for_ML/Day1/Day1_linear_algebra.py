# Linear Algebra

"""
# Key Concepts

Vector
Metrix - A 2D array of number structure
Scalar -> A singal number, use to scale vectore or matrix
Linear Transformation -> A function that maps vectors to other vectors

"""

# Linear Transformation
# T(x) = ax
# ax = cooficent matrix


import numpy as np # numpy 
import scipy.linalg as la

# Vector

v = np.array([1,2,3])
print("vector v:",v)


# Scalar Multiplication

v_scaled = 8 * v # 10 -> scalar
print("Scaled vector (8*v):", v_scaled)

# Metrix example
"""
1 2
3 4  -> 2 X 2

"""
A = np.array([
    [1, 2],
    [3, 4]
    ])

print("Matrix A:\n", A)

# second matrix
B = np.array([[2, 4], [6, 8]])
"""
A X B != B X A
mul = A @ B
"""

print("Matrix B:\n", B)

# Matrix multiplication
C = A @ B

mul = A * B
print("Matrix product A @ B:\n", C)
print("element mul:\n", mul)

# Addition
add_v = A + B
print("Add vector :\n", add_v)


# Transpose
A_Transpose = A.T
print("Transpose :\n", A_Transpose)

# 2x + 3y = 8, 5x + 4y = 13
# b = [8, 13]

"""
A = 
2   3
5   4

"""
A = np.array([
    [2,3],
    [5,4]
])
b = np.array([8,13])

x = np.linalg.solve(A, b)
print(f"Solution = {x}")

A = np.array([
    [8,3,-2],
    [-4, 7, 5],
    [3,4,-12]

])

b = np.array([9,15,35])

x = np.linalg.solve(A, b)
print("solve :\n", x)

# LU Decomposition
A = np.array([
    [2,4,5],
    [1,3,2],
    [4,2,1]
])

P, L, U = la.lu(A) # [P_val, L_val, U_val]

print("Permited matrix :\n", P)
print("Lower traingular matrix :\n", L)
print("Upper traingular matrix :\n", U)

# QR Decomposition
# Q (orthogonal)
# R (upper traingular)

A = np.array([
    [1,2,3],
    [3,4,5]
])

Q, R = np.linalg.qr(A)

print("Q, orthogonal :\n", Q)
print("R, upper traingular :\n", R)

result = Q @ R
print(A)
print(result)

# Types of Systems:
"""
# Consistent System (At least one solution)
# Inconsistent System (No solution)
# Independent System (Exactly one solution)
# Dependent System (Infinitely Many solution)

"""
