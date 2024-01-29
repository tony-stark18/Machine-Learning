import numpy as np;

#numpy array operation
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Addition
result_add = arr1 + arr2

# Subtraction
result_sub = arr1 - arr2

# Multiplication
result_mul = arr1 * arr2

# Division
result_div = arr1 / arr2

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)


# NumPy provides many universal functions for element-wise operations.
arr = np.array([1, 2, 3, 4, 5])

# Square root
result_sqrt = np.sqrt(arr)

# Exponential
result_exp = np.exp(arr)

# Trigonometric functions (sin, cos, tan, etc.)
result_sin = np.sin(arr)

print(result_sqrt)
print(result_exp)
print(result_sin)

# Aggregation Functions:

arr = np.array([1, 2, 3, 4, 5])

# Sum
arr_sum = np.sum(arr)

# Mean
arr_mean = np.mean(arr)

# Maximum and Minimum
arr_max = np.max(arr)
arr_min = np.min(arr)

print(arr_sum, arr_mean, arr_max, arr_min)


