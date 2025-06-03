# NumPy Array Slicing
# taking elements from one given index to another given index.
# [start:end] or [start:end:step].
import numpy as np
arr = np.array([15, 32, 23, 24, 55,76, 87])

print(arr)
print(arr[0:len(arr):1])

print(arr[1:5])
print(arr[1:5:1])

print(arr[1:5:2])

print(arr[:5])
print(arr[1:])
print(arr[::2])
print(arr[1::2])


# Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# [dim1:dim2, elementindex1: elementindex2]
print(arr[0, 1:4], end = "\n\n")

print(arr[0:2, 3], end = "\n\n")

print(arr[0:2, 1:4:2], end = "\n\n")