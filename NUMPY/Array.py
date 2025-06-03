import numpy as np

# ndarray = np.array(data[SEQUENTIAL | ITERATIVE] , dtype = object , ndmin =0)
data = range(1,10)
arr = np.array(data, ndmin=3) # dtype = complex
print(arr)
print(arr.shape) # return size in tuple form. (row,column)
print(arr.ndim) # Return dimension
k= np.array([[1,2,3,4,5]])
print(type(k[0])) # <class 'numpy.ndarray'>
print(type(k[0][1])) # <class 'numpy.int64'>
print(k.shape)