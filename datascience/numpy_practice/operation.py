import numpy as np

test_array = np.arange(1, 11)
print(test_array)

# sum : ndarray의 element 간의 합을 구함 (list의 sum과 동일)
print(test_array.sum(dtype=np.int8))

# axis : 모든 operation function을 실행시 기준이 되는 dimension 축
# 2차원에서는 0이면 row, 1이면 col / 3차원이면 1인경우 row, 2인경우 col
test_array2 = test_array.reshape(5, 2)
print(test_array2.sum(axis=1))  # col 방향으로 sum

# mean & std : 평균과 표준편차를 구함
print(test_array2.mean(axis=0, dtype=np.int32))
print(test_array2.std(axis=0, dtype=float))

# vstack : vertical(수직) 방향으로 ndarray를 합치는 함수, 만약 합치는 ndarray들의 차수가 맞지 않으면 오류 발생
a = np.arange(1, 4)
b = np.arange(5, 8)
c = np.arange(10, 13)
d = np.vstack((a, b, c))  # 주의! 합칠 ndarray들을 하나의 튜플 / 리스트 형식으로 전달해야한다.
print(d)

# hstack : horizonal(수평) 방향으로 ndarray를 합치는 함수, 만약 합치는 ndarray들의 차수가 맞지 않으면 오류 발생
a = np.array([[1], [2]])
b = np.array([[3], [4]])
c = np.array([[5], [6]])
d = np.hstack((a, b, c))
print(d)

# concatenate : ndarray를 합치는 함수, axis를 기준으로 ndarray를 합치는 함수
a = np.array([[1], [2]])
b = np.array([[3], [4]])
c = np.array([[5], [6]])
d = np.concatenate((a, b, c), axis=1)
print(d)
