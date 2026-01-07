'''
arr.reshape(2,3) It Converts 1D Array into 2D or multidimensional array 
the 2 indicates rows
the 3 indicates columns
it give modified array in return
.ravel converts Multidimensional array into 1D Array It gives modified array
.flatten it is same as .ravel but it gives copy of array in return
'''

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
reshaped = arr.reshape(2,4)

# print(reshaped)

arr_2 = np.array([[1,2,3,4],
                  [5,6,7,8]])
    

ay = arr_2.ravel()
print(arr_2)
print(ay)

# ay1 = arr_2.flatten()
# print(ay1)

# print(arr_2)

