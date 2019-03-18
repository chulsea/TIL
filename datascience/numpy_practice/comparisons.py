import numpy as np
"""
numpy 비교 연산
"""
# All & Any : Array의 데이터 전부 또는 일부가 조건에 만족하는지 여부를 반환
a = np.arange(1, 11)

# all(condition) : 해당 조건에 모두 만족해야 True
print(np.all(a > 5))
# any(condition) : 해당 조건에 하나라도 만족하면 True
print(np.any(a > 5))

# Comparison operation : 배열의 크기가 동일할 때 element간 비교의 결과를 boolean type으로 반환
# 기존의 비교 연산자로 배열의 각 element에 대해 논리값 계산이 가능하다.
b = np.arange(1, 20, 2)
print(b > a)
print(b == a)

# numpy의 Comparison operation

# 1. logical_and(*condition)
print(np.logical_and(a > 0, a < 3))

# 2. logical_not(*condition)
print(np.logical_not(a))

# 3. logical_or(*condition)
print(np.logical_or(a < 5, a > 5))

# numpy where(condition, true 시 값, false 시 값)
c = np.where(a > 5, 10, 0)
print(c)

# 만약 where에 2번째, 3번째 인자가 없다면 index 값을 반환한다. (false는 추가 x)
d = np.where(a > 5)
print(d)

# np.isnan(ndarray): number가 아닌 경우 체크, np.isfinite(a): 유한한 정수 값인 경우 체크
e = np.array([np.NaN, np.Inf, 1, 2, 3])
print(np.isnan(e))
print(np.isfinite(e))

# argmax & argmin : array내의 최대값과 최소값의 "index"를 반환
f = np.arange(1, 101)
print(f)
print(np.argmax(f))
print(np.argmin(f))
f = f.reshape(2, 50)
print(np.argmax(f, axis=1))  # 다음과 같이 축을 기준으로 최대 / 최소값을 판별할 수 있다.
