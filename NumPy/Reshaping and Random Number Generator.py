import numpy as np
# randomArray = np.random.random((3,3))
# print(randomArray)

if np.random.random() > 0.5:
    print("run the function")
else:
    print("dont run the function")


print(np.arange(1,10,1))

print(np.linspace(1,7,10))

randomArray = np.random.random((4,3))
print(randomArray)

randomArray2 = np.reshape(randomArray, (6,2))
print(randomArray2)

print(randomArray2.flatten())
