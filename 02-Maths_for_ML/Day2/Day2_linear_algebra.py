# Linear Transformations

import numpy as np
kx, ky = 1.5, 0.5
# A = transforming matrix

A = np.array([
    [kx, 0],
    [0, ky]
])

x = np.array([2,3])
Tx = A @ x
print("original vector : \n", x)
print("scalled vector : \n", Tx)

# 4.2 Rotation
theta = np.pi / 2 #90 degrees

A = np.array([
    [np.cos(-theta), -np.sin(-theta)],
    [np.sin(-theta), np.cos(-theta)]
])

x = np.array([3,2]) #original vector
roted_vector = A @ x

print("Original vector : \n", x)
print("Rotated vector : \n", roted_vector)

#  Reflection about x-axis

A = np.array([
    [1, 0],
    [0, -1] #for reflextion along x axis
])

x = np.array([3, 4])
reflected_vector = A @ x

print("Original vector : \n", x)
print("Reflected vector : \n", reflected_vector)

# 5 Composition of Linear Transformations

A = np.array([
    [2,3],
    [4, 9]
])

B = np.array([
    [4,7],
    [4, 10]
])

x  = np.array([1,2])
result1  = B @ (A @ x)

intermediate_matrix = B @ A
result2 = intermediate_matrix @ x

print("result1 : \n", result1)
print("result2 : \n", result2)
