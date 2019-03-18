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

"""
numpy에서는 array간에 기본적인 사칙연산을 지원해준다.
+ : ndarray의 index와 일치하는 원소들을 합함
- : ndarray의 index와 일치하는 원소들을 뻄
* : ndarray의 index와 일치하는 원소들을 곱함
/ : ndarray의 index와 일치하는 원소들을 나눔
// : ndarray의 index와 일치하는 원소들을 나눔 (나머지 버림)
% : 모듈러 연산

위 사칙연산은 element-wise operation이다.
element-wise operation : array간의 shape이 같은 경우 일어나는 연산
"""

e = np.array([[1, 2, 3], [2, 3, 4]])
f = np.array([[5, 6, 7], [8, 9, 10]])
print(e+f)
print(f-e)
print(e*f)
print(e/f)
print(e % f)

"""
dot-product : 기존의 행렬 연산을 수행하는 방법
dot 함수를 사용하여 구현할 수 있다.
"""
g = np.arange(1, 7).reshape(2, 3)
h = np.arange(7, 13).reshape(3, 2)
print(g.dot(h))

"""
transpose : ndarray 행 / 열을 뒤바꾸는 함수
transpose 메서드나 T attribute를 사용.
"""
print(g)
print(g.T)
print(h)
print(h.transpose())

"""
broadcasting : shape이 다른 ndarray 간 연산을 지원
"""

test_matrix = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 3
print(test_matrix * scalar)  # matrix - scalar 간 연산 지원 (모든 element에 scalar 연산)
test_vector = np.arange(1, 4)
print(test_vector * scalar)  # matrix - scalar뿐 아니라 vector - scalar 간 연산도 지원해준다.

# 그 외에도 matrix - vector 간 broadcasting을 지원해준다. 단, column의 길이가 같아야함
print(test_matrix + test_vector)
