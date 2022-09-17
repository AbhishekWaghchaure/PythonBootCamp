import numpy as np

print(np)
list = [[1, 2, 3],
        [9, 8, 7],
        [6, 5, 4]]
print(list)
print(type(list))

# convert list into array
array = np.array(list)
print(array)
print(type(array))
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)

# creating new array
custArray = np.zeros((3,5))
print(custArray)
