import numpy as np

test_array = np.array([1, 2, 3, 4], int)

# reshape() : Array의 shape 크기를 변경
print(test_array.shape)
print(test_array)
print(test_array.reshape(2, 2))
# 단, 바꾸려는 차원의 size와 현재 ndarray의 size가 같아야 변형가능하다.

# flatten() : 다차원 array를 1차원 array로 변환
print(test_array.reshape(2, 2).flatten())