import numpy as np
arr1 = np.array([[1,2,3,4],
                 [5,6,7,8]])
arr2 = np.array([[8,7,6,5],
                 [4,3,2,1]])

print(np.sort(arr2,axis = 1, kind= 'mergesort'))

conArr1 = np.hstack((arr1, arr2))
print(conArr1)

conArr2 = np.vstack((arr1, arr2))
print(conArr2)

conArr3 = np.concatenate((arr1, arr2), axis = 1)
print(conArr3)

conArr4 = np.concatenate((arr1, arr2), axis = 0)
print(conArr4)

print(np.hsplit(conArr4, 1))
print(np.vsplit(conArr4, 2))