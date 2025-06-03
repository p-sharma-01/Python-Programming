# NumPy Array Reshaping
# Reshape From 1-D to 2-D
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarr = arr.reshape(5, 2)
print(newarr) # 1D to 2D


#(2, 2, -1 )means:

# First dimension: 2 blocks

# Second dimension: Each block contains 2 rows

# Third dimension: -1 tells NumPy to figure out automatically how many elements should go in this dimension so the total stays the same.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2,2,-1)

print(newarr)
