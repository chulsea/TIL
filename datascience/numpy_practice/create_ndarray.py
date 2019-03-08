import numpy as np

# arange : array의 범위를 지정하여 값의 list를 생성하는 명령어
a = np.arange(30)
print(a)
# reshape을 활용하여 1차원 ndarray를 다차원 배열로 변형할 수 있다.
print(a.reshape(6,5))

# arange시 step을 줄 수 있다.
b = np.arange(0, 5, 0.5)  # python의 range와 비슷하게 시작, 끝, step 순으로 numpy ndarray를 만들 수 있다.
print(b)

# zeros : 0으로 가득찬 ndarray 생성
c = np.zeros(shape=(10, ), dtype=np.int8)
print(c)

# ones : 1로 가득찬 ndarray 생성
d = np.ones(shape=(5, 5), dtype=np.float32)
print(d)

# shape만 주어지고 비어있는 ndarray 생성
e = np.empty(shape=(3, 2), dtype=np.int64)
print(e)

# something_like : 기존 ndarray의 shape크기 만큼 1, 0 또는 empty array 반환
f = np.zeros_like(a.reshape(5, 6))  # a.reshape(5, 6)의 공간만큼 0을 채워넣을 경우 zeros_like
print(f)

g = np.ones_like(a.reshape(3, 10))  # a.reshape(3, 10)의 공간만큼 1을 채워넣을 경우 ones_like
print(g)

h = np.empty_like(a)  # a 크기의 공간만큼 빈 element를 가진 ndarray 생성
print(h)

# identity : 단위 행렬 생성 (row와 col의 index가 같은 부분에 1이 채워진 행렬)
i = np.identity(n=5, dtype=np.int8)
j = np.identity(n=5)
print(i)
print(j)

# eye : 대각선이 1인 행렬, N으로 row, M으로 col의 갯수를 설정할 수 있으며 k로 시작 index를 변경할 수 있다.
o = np.eye(3, 5, 1, int)
print(o)

# diag : 대각 행렬의 값을 구함
print(np.diag(j))
print(np.diag(o))
print(np.diag(o, k=1))

# random sampling : 데이터 분포에 따라 array 생성
p = np.random.uniform(0, 1, 10).reshape(2, 5)  # 균등분포
q = np.random.normal(0, 1, 10).reshape(2, 5)  # 정규분포
print(p)
print(q)
