# NumPy Copy vs View
#copy()
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arrcopy = arr.copy()
arr[0] = 42 # change will not reflect in main copy (shallow copy)

print(arr)
print(arrcopy)

# NumPy Copy vs View
#view()
arr = np.array([1, 2, 3, 4, 5])
arrview = arr.view()
arr[0] = 42 # change will reflect in main copy (deep copy)

print(arr)
print(arrview)