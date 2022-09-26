import pandas as pd
import numpy as np

list = [1,2,3,4,5]
print(list)
print(np.array(list))

print(pd.Series([list]))


array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(array)

df = pd.DataFrame(array, columns=['a','b','c'])
print(type(df))
print(df)
del(df)