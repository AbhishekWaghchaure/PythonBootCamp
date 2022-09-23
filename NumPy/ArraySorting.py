import numpy as np

arr = np.array([[7,3,8,6,4],[7,2,9,8,6], [5,4,2,3,1]])
print(arr)

mergeSort = np.sort(arr ,axis = 1, kind = 'mergesort')
print(mergeSort)

mergeSort2 = np.sort(arr ,axis = 0, kind = 'mergesort')
print(mergeSort2) 
