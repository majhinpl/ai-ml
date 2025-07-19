# Brodcasting

import numpy as np
# S -> V
arr = np.array([1, 2, 3, 4, 5]) # v
s = 5 # s

new_arr = arr * s

# print(arr)
# print(new_arr)

mat = np.array([
    [2, 4, 7],
    [3, 4, 6],
    [4, 6, 9]
])

v = np.array([1, 2 , 3])
new_mat = mat + v

# print("matrix:", mat)
# print("broadcasting:", new_mat)

## sorting
a = np.array([5, 3, 2, 7, 99])
# print(np.sort(a)[::-1])

m = np.array([[6, 4, 9],
              [2, 1, 8],
              [7, 9, 1]])

col_sort = np.sort(m, axis=1)
row_sort = np.sort(m, axis=0)

# print("Accending order sort column wise (axis=1): \n", col_sort)
# print("Accending order sort row wise (axis=1): \n", row_sort)

# Append
mtx = np.array([
    [1, 2, 3],
    [2, 3, 6]
])

new_row = np.array([
    [2, 5, 7] #dimention needs to be equal with original matrix.
])

new_mtx = np.append(mtx, new_row, axis=0)

# print("Matrix : \n", mtx)

# print("Apended Matrix row (axis=0): \n", new_mtx)
# print("Matrix : \n", mtx)

# print("Apended Matrix row (axis=0): \n", new_mtx)

# column wise appending
mtx = np.array([
    [1, 2, 3],
    [2, 3, 6]
])

new_col = np.array([])