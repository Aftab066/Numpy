import numpy as np

arr = np.array([100,200,300])
discount = 10
result = arr - (arr*discount/100)
print(result)

# Before numpy if we want to do any mathematical operation on a list elements we need to use loops
#But after numpy we convert the list to array and write any mathematical operation we need to use 
#Numpy Automatically does the operations sepratley on it 