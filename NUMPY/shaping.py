import numpy as np
arr= np.array([1,2,3,4,5,6,7,8,9])
arr.shape = 3,3
print(arr)

# arange(start,stop,step)
arr2 = np.arange(1,10,.5)
print(list(arr2))


# linspace(start,stop,number of sample)

data = np.linspace(1,5,10) # manages its stepsize according to the provided number.
print(list(data))

# Maximum
ma = np.max(arr)
print(ma)

# minimum
mi = np.min(arr)
print(mi)

# around
round = np.around([1.23, 3.45, 45.76, 432.65443],2)
print(round)

