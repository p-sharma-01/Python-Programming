import numpy as np
carr = np.array([
               [ [1,2,4,5] ],
               [ [1,2,3,2] ] , 
               [ [1,2,2,1] ]
            ])

print(carr)
print("Dimension of carr = ",carr.ndim)
print(carr.shape) #(3,1,4) [no. of elements in each bracket seperated by comma.]