import numpy as np
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9,]])
arr2 = np.array([[9,8,7],
                 [6,5,4],
                 [3,2,1]])
arr3 = np.array([1,2,3,4,5,6,7])

print(arr)
print(arr2)

print(arr+arr2)
print(arr*arr2)
print(arr.dot(arr2))
print(arr3[:3])
print(arr3[2:])
print(np.dot(arr,arr2))
print(np.cross(arr, arr2))