import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr + 5)
print(arr - 5)
print(arr * 5)
print(arr / 5)
arr = arr + 1
print(arr)

print(arr.max())
print(arr.min())

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr.max())
print(arr.max(axis = 0)) #maximum element column wise
print(arr.max(axis = 1)) #maximum elements row wise

print(arr.min(axis = 0)) #minimum element column wise
print(arr.min(axis = 1)) #minimum element row wise

print(arr.sum())

array = np.random.random((3,4))
print(array)
arrayResize = np.reshape(array,(6,2))
print(arrayResize)
