import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
re_arr = arr.reshape(5, -1)
# print(arr)
# print()
# print(re_arr)

arr_1d = np.array([10, 20, 30, 40])
for num in arr_1d:
    print(num)

arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for arr in arr_2d:
    print("2d arr : \n", arr)

for arr in np.nditer(arr_2d):
    print("2d arr with nditer: \n", arr)


# operations with array

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

add = a + b
sub = a - b
pro = a * b
div = a / b
exp = b ** 5
re = b % a
"""print(f"Addition of two arrays element wise = {add}")
print(f"Subtraction of two arrays element wise = {sub}")
print(f"product of two arrays element wise = {pro}")
print(f"Division of two arrays element wise = {div}")
print(f"Each element of array {b} raised to the power 5 gives: {exp}")
print(f"Reaminder of {b} divides by {a} element wise gives: {re}")"""

#  Universal Functions (ufuncs)

arr = np.arange(1, 11)
arr_sqrt = np.sqrt(arr)
arr_sin = np.sin(arr)
arr_cos = np.cos(arr)
arr_tan = np.tan(arr)
arr_log = np.log(arr)
arr_logten = np.log10(arr)
arr_exp = np.exp(arr)

"""print("arr_sqrt : \n", arr_sqrt)

print("arr_sin : \n", arr_sin)
print("arr_cos : \n", arr_cos)
print("arr_tan : \n", arr_tan)
print("arr_log : \n", arr_log)
print("arr_logten : \n", arr_logten)
print("arr_exp : \n", arr_exp)"""


#  Statistical Functions
data = np.array([10, 20, 30, 40, 50])

me = np.mean(data)
md = np.median(data)
sd = np.std(data)
v = np.var(data)
minn = np.min(data)
maxx = np.max(data)

"""print(me)
print(md)
print(sd)
print(v)
print(minn)
print(maxx)
print(np.argmin(data))
print(np.argmax(data))"""

# Matrix Creation

A = np.array([
    [100, 2],
    [99, 4]
])

B = np.array([
    [200, 6],
    [7, 50]
])

dit1 = np.linalg.det(A)
dit2 = np.linalg.det(B)

# print("Determinant of a Matrix : \n", dit1)
# print("Determinant of B Matrix : \n", dit2)

# Inverse of a Matrix

inv1 = np.linalg.inv(A)
inv2 = np.linalg.inv(B)

# print("Inverse of a Matrix : \n", inv1)
# print("Inverse of B Matrix : \n", inv2)


# Advanced Mathematical Functions
# Summation & Cumulative Sum
arr = np.array([100, 200, 300, 400])

submition = np.sum(arr)
cum_sum = np.cumsum(arr) 

# print("submition : \n", submition)
# print("Cumulative Sum : \n", cum_sum)

# Finding Unique Elements & Counting Occurrences
arr = np.array([1, 2, 3, 1, 2, 3, 4, 4, 4])

uniq_arr, count = np.unique(arr, return_counts=True)

# print("unique array : \n", uniq_arr)
# print("unique count : \n", count)

# Sorting an Array
arr = np.array([3, 1, 4, 1, 5, 9])

# print("Sorting an Array : \n", np.sort(arr))
# print("Sorting an Array : \n", np.sort(arr)[::-1])
# print("index of sorted element : \n", np.argsort(arr)[::-1])

# Finding Percentiles & Quantiles
data = np.array([10, 20, 30, 40, 50])

q1 = np.percentile(data, 25)
md = np.percentile(data, 50)
q3 = np.percentile(data, 75)

print("finding percentile : \n", q1)

A = np.array([
    [8, 3, -2],
    [-4, 7, 5],
    [3, 4, -12]
])

b = np.array([9, 15, 35])

cal = np.linalg.solve(A, b)
print("linalg solve : \n", cal)

# vectorization and numpy.