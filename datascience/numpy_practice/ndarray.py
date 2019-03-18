import numpy as np
# array create
"""
numpy는 파이썬의 array와는 다르게 하나의 데이터 type만 배열에 넣을 수 있다.
c를 사용하여 배열을 만들기 때문에 파이썬의 배열보다 훨씬 빠르다.
"""

test_array = np.array([1, 2, 3, 4], dtype=np.float)
print(test_array)
# numpy array는 numpy 모듈 내의 array 함수로 만들 수 있다.
# 첫번째 인자로는 ndarray로 만들 배열(matrix)
# 두번째 인자로는 해당 ndarray의 type을 넣어준다.

# np.array의 변수들
print(test_array.dtype)  # numpy array의 데이터 type
print(test_array.shape)  # numpy array의 dimension 구성을 return (tuple 형태)
# 고차원일 수록 앞선 index에 저장된다.
# ex) 2x3 matrix의 경우 (2차원) shape은 (2,3)이 된다.
print(test_array.dtype)
print(type(test_array[0]))

# numpy에서 String 데이터를 입력해도 dtype에 맞춰 type이 변형된다.
test_array2 = np.array([1, 3, 5, '7'], dtype=np.int)
print(test_array2.ndim)  # ndim은 number of dimension으로 몇 차원인지 알려주는 변수
print(test_array2.size)  # size는 해당 ndarray에 있는 데이터의 갯수
print(test_array2.dtype)  # dtype은 해당 ndarray에 설정된 data type, 각 element가 차지하는 memory의 크기가 결정
print(test_array2.nbytes)
"""
basic type / numpy types
boolean / bool
integer / int8, int16, int32, int64, int128, int(=int32)
unsigned integer / uint8, uint16, uint32, uint64, uint128, uint(=int32)
Float / float32, float64, float(=float64), longfloat
Complex / complex64, complex128, complex
Strings / str, unicode
Object / object
Records / void
"""
print(test_array2)