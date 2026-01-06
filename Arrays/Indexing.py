# #Indexing Is To Access A Specific Value In Array 

import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[0:5:2]) #0 Is Starting Index 5 Is stoping indexing it excludes one index 2 is steping index

print(arr[[1,2,4]])

print(arr[arr>20]) #Boolean Masking Is That Uses conditions in it

print(arr[::-1]) #Reversing Array 