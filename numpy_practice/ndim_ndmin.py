import numpy as np
narr = np.array([1, 2, 3, 4], ndmin=5)
 
print(narr)
print('number of dimensions :', narr.ndim)

print(narr[0]) # 4-d
print(narr[0,0]) # 3-d print 0th element of 0th row
print(narr[0,0,0]) # 2-d
print(narr[0,0,0,0]) # 1-d
print(narr[0,0,0,0,1]) #2nd element from above 1-d array