import numpy as np
array = np.array([1,2,3,4,5,6,7,5,4,3,2,1])
print(array)
print(array[1])
print(array[3:])
print(array[3 :-3])
array2 = np.array([[1,2,3],
                   [4,5,6],
                   [7,5,4],
                   [3,2,1]])
print(array2)
print(array2[ : 2, : ]) # first 2 rows
print(array2[2 : , : ]) #all the rows except first 2 rows
print(array2[1 : , 1: ])