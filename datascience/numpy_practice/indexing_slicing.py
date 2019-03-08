import numpy as np

a = np.array([[1, 2, 3], [4.5, 5, 6]], int)
# indexing
print(a)  # 전체 ndarray 출력
print(a[0, 0])  # 리스트와는 달리 이차원 배열에서 [0, 0] 같은 표기법 제공
print(a[0][0])  # a[0, 0]과 같다.

# 할당도 가능
a[0, 0] = 10
print(a)

# slicing : list와는 달리 행과 열을 나눠서 slicing 가능하다.
print(a[:, 2:])  # 전체 row에서 index 2부터 가져옴
print(a[1, 1:3])  # 1번 row에서 1~2번 column
print(a[1:3])  # 1~2번 row에서 전체 column


# 파이썬에서처럼 slicing시 세번째 숫자를 주어 step 설정도 가능하다.
print(a[:, ::2])