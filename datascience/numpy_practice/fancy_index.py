import numpy as np, random
"""
boolean index
numpy는 배열을 특정 조건에 따른 값을 배열 형태로 추출하도록 만들어 준다.
이떄 python의 비교연산자 뿐 아니라 Comparison operation 함수들도 사용할 수 있다.
"""
test_array = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1], dtype=np.int32)
print(test_array > 3)  # 단순 비교시
print(test_array[test_array > 3])  # 조건이 True인 index의 element만 추출

arr = [random.randint(1, 100) for _ in range(100)]
test_array2 = np.array(arr)
test_array3 = test_array2 > 50
print(test_array3.astype(np.int))  # boolean으로 표현되는 값을 int형으로 바꾸는 방법

"""
fancy index
array를 index value로 사용하여 값을 추출하는 방법
"""
a = np.array([2, 4, 6, 8])
b = np.arange(0, 10)
print(b[a])  # a의 원소를 index로 b의 값을 추출하는 방법, matrix 형태로도 사용할 수 잇다.

a = a.reshape(2, 2)
b = np.array([random.randint(0, 1) for _ in range(10)])
c = np.array([random.randint(0, 1) for _ in range(10)])
print(b)
print(c)
print(a[b, c])  # 앞에 먼저 사용된 arr를 row의 index, 뒤에 사용된 arr를 col의 index로 사용
