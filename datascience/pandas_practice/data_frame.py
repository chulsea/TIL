import pandas as pd, numpy as np
"""
pandas에서 dataframe은 데이터 테이블 전체를 구성하는 객체이다.
dataframe은 numpy의 array와 비슷하다. 단, 각각의 column의 data type은 다를 수 있다.
또한 row와 column의 index를 가질 수 있으며 size가 고정된 것이 아닌 유동적이다.

dataframe은 series를 모아서 만든 Data Table이라 생각해도 무방! (기본적으로 2차원)
"""

raw_data = {
    'last_name': ['park', 'kim', 'yoo', 'jung', 'cho', 'sung'],
    'first_name': ['gyeongcheol', 'yeonjoo', 'seungjoo', 'semin', 'sungwon', 'hongjoon'],
    'age': [27, 26, 25, 29, 29, 26]
}

mft = pd.DataFrame(raw_data, columns=raw_data.keys())
# 첫번째 인자로 dataframe으로 만들고자하는 data를 넣는다. columns는 해당 column의 header를 넣어준다.
print(mft)

mft2 = pd.DataFrame(raw_data, columns=('first_name', 'last_name'))
# column을 일부만 설정해서 해당하는 raw_data에서 column만 가져올 수도 있다.
print(mft2)

mft3 = pd.DataFrame(raw_data, columns=list(raw_data.keys()) + ['young'])
print(mft3)
# 위와 같이 해당 data에 없는 column이 있다면 NaN 값으로 초기화 한 후 컬럼을 추가한다.

print(mft3.first_name)
print(mft3['first_name'])
# dataframe indexing

test = pd.Series(np.NaN, index=[5, 4, 3, 2, 1])
print(test.loc[2:])
# loc은 해당 index의 이름을 통해서 판단하는 방법
print(test.iloc[2:])
# iloc은 index의 순서를 통해서 판단하는 방법

mft3.young = mft3.age <= 27
print(mft3)
# 단, 새로운 컬럼을 만들지는 못하고 기존에 있는 컬럼에서 값을 바꿀 수 있다.

print(mft3.T)  # 이렇게 transpose도 가능