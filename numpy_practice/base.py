import numpy as np
arr = np.array([1, 2, 3, 4, 5])
c = arr.copy()
v = arr.view()

print(c.base) # None as independent copy
print(v.base) # return arr dependent copy on arr and changes wil reflect in arr