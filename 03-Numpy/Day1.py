# Creating Multi-Dimentional Arrays
# 3D

import numpy as np

arr_3d = np.array([
    [
        [2,3,5],
        [7,9,3]
    ],
    [
        [3,4,7],
        [9,7,6]
    ]
])

print(arr_3d)

# Creating 3 X 3 matrix with elements 0

zeros_arr = np.zeros((3,3))
print(zeros_arr)

# Creating 3 X 3 matrix with elements 1 

ones_arr = np.ones((3,3))
print(ones_arr)

# Identity Matrix

identity_matrix = np.eye((6))

print("square marix : \n", identity_matrix)

#  Creating an Array with a Range of Values

# Creates an array first 50 numbers starting from 1

arr = np.arange(1, 51, 6)
print("Creating an Array with a Range: \n", arr)

arr = np.arange(2, 101, 2)
print("Creating an Array with a Range: \n", arr)

# Creating an Array with Evenly Spaced Values
# we need an array having 5 values from 1 to 10 evenly spaced

sp_arr = np.linspace(1, 20, 5)
print("array having 5 values : \n", sp_arr)

# Creating a Random Array

random_arr = np.random.rand(4, 4) #creates a 4 X 4 matrix with all values ranging from 0-2

print(random_arr)

random_arr = np.random.randint(1, 11, size=(3, 3))
print("random ranges matrix : \n", random_arr)

# Array Attributes
# NumPy arrays have several attributes that provide important information about their properties.

arr_attr = np.array([
    [10, 30, 15],
    [30, 45, 62],
    [24, 42, 21]
])

print("arrays attri : \n", arr_attr)
print("arrays attri Shape of array : \n", arr_attr.shape)
print("arrays attri Size of array : \n", arr_attr.size)
print("arrays attri Number of dimensions : \n", arr_attr.ndim)
print("arrays attri Data type of elements : \n", arr_attr.dtype)
print("arrays attri Item size in bytes : \n", arr_attr.itemsize)
print("arrays attri Total memory consumed : \n", arr_attr.nbytes)

# Array Indexing and Slicing
arr_1d = np.array([10, 20, 30, 40, 50])

print(arr_1d[0])

print("Slicing", arr_1d[::4])

#  Accessing Elements in a 2D Array

arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
    ])

print("2D Array : \n", arr_2d)

print("Accessing row Elements in a 2D Array : \n",
      arr_2d[ 2, :])

print("Accessing column Elements in a 2D Array : \n",
      arr_2d[ :, 1])

print("Accessing column Elements in a 2D Array : \n",
      arr_2d[ 1, 1:])

print("Accessing column Elements in a 2D Array : \n",
      arr_2d[ 0,: 2])


anti_diag = np.fliplr(arr_2d).diagonal()

print(anti_diag)
