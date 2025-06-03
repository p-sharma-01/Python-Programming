import numpy as np
M1 = [[1,2,3],[5,6,7]]
M2 = [[0,3,4], [3,4,5],[1,1,1]]
arr1 = np.array(M1)
arr2 = np.array(M2)
if arr1.shape == arr2.shape:
  result = np.add(arr1,arr2)
  print(result)
  
else:
  print("Matrix multiplication.")
  print(arr1.dot(arr2))


