import numpy as np

ndarray = np.array([1,2,3,4], np.float32)
print(ndarray.reshape(4,-1)[1,0])