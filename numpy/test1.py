import numpy as np

ndarray = np.array([1,2,3,4], np.float32)
print(ndarray.reshape(4,-1)[1,0])
arange = np.arange(10,100).reshape(10, -1)

row5 = arange[4,]
print(row5)
brow5 = np.where(row5 <= 50)
taken = row5[brow5]
print(taken)
taken = row5.take(brow5)
print(taken[0,1])
