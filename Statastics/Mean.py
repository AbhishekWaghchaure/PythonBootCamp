import numpy as np
array = np.array([1,2,3,4,5,6])
mean = np.mean(array)
print(mean)

#weighted average
array = np.array([1,2,2,6,5,9])
w = np.array([1,2,3,4,5,6])
print(np.average(array,weights=w))

#for 2D arrays
array2 = np.array([[1,2,3],[4,5,6]])
print(np.mean(array2))
print(np.mean(array2, axis= 0)) #column wise mean
print(np.mean(array2, axis=1)) # row wise mean

