import numpy as np

list =np.array([1,2,3,4,5,6,7,8,9])

#Traditional way
# count = 0
# for x in list :
#     if(x > 5):
#         count = count + 1
#         print(x)
# print(count)

#using numpy
print(list > 5)

# for x in list:
#     print(x)

print(list[list > 5])
print(list[list % 3 == 0])
