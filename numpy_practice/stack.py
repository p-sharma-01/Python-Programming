# stacking is done along a new axis
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([5,6,7])
arr = np.stack((arr1, arr2), axis=1) #  it is like zip but here size must be same.
print(arr)
print(arr.ndim)