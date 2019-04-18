import pandas as pd
import numpy as np

"""
groupby 연산
SQL groupby 명령어와 같은 방식
split -> apply -> combine 과정을 거쳐 연산함
"""
df = pd.read_csv('example.csv', sep=',', header=None)
print(df.head())
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV', 'TEST']
print(df.head())

# df.groupby("묶는 기준이 되는 컬럼")["적용받는 컬럼"].연산()
result = df.groupby("TEST")['B'].sum()
print(result)

data = {
    'Points': [876, 789, 863, 673, 741],
    'Rank': [1, 2, 2, 3, 3],
    'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings'],
    'Year': [2014, 2015, 2014, 2015, 2014]
}

df = pd.DataFrame(data)
print(df)
result = df.groupby('Team')["Points"].sum() # dataframe으로 생성
print(result)
# 아래와 같이 groupby 메서드에 리스트로 하나이상의 컬럼을 기준으로 묶을 수 있다.
result = df.groupby(['Team', 'Year'])["Points"].sum()
print(type(result))
print(result)

# groupby의 결과물도 결국은 dataframe이다. 두 개의 column으로 groupby를 한다면 index가 두 개 생성
print(result.index)
print(result['Kings':'Riders'])  # 뒤에 넣은 컬럼 index까지 도출

print(result.unstack(fill_value=0))  # group으로 묶여진 데이터를 matrix 형태로 전환

# grouping된 데이터를 swaplevel을 통해 index level을 변경할 수 있다.
print(result.index)
print(result.swaplevel(0,1))

# index level을 기준으로 기본 연산을 수행할 수 있다. (sum, min, max, ge, le 등)
print(result.sum(level=0))
print(result.sum(level=1))

# grouped - groupby에 의해 split된 상태를 추출하도록 만들어줌
grouped = df.groupby('Team')
for name, group in grouped:
    print(name)
    print(group)
# 특정 key값을 가진 그룹의 정보만 추출
print(grouped.get_group('Kings'))

# 추출된 group 정보에는 세가지 유형의 apply가 가능하다.
# 1. Aggregation : 요약된 통계정보 추출
print(grouped.agg(sum))
mean_group = grouped.agg(np.mean)
print(mean_group)
print(grouped['Points'].agg([np.sum, np.mean, np.std]))

# 2. transformation, 개별 데이터의 변환을 지원
# 3. filter: 특정 조건으로 데이터 검색시 사용
