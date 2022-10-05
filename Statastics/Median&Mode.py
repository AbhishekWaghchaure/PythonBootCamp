import numpy as np
import collections as cp
array = np.array([1,2,3,4,5])
print(np.median(array))

# even samples
array2 = np.array([1,5,2,2,2,3,3,5,4,5,6,6,6,6,3])
print(np.median(array2))

# Mode
sort = np.sort(array2, kind = 'merge sort')
count = cp.Counter(sort)
print(count)
print(count.most_common(1))