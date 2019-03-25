import pandas as pd, numpy as np

df_data = pd.read_csv('example.csv', sep=',', header=None)
print(df_data.head())

# Pandas에서 하나의 열(column)을 Series, Data Table 전체를 Data Frame이라 부른다.

data = [1, 2, 3, 4, 5]
series = pd.Series(data=data)
print(series)
# series를 만들때 위와 같이 list 데이터를 넣어 만들 수 있다.
# series는 numpy의 ndarray를 띈다.

series2 = pd.Series(data=data, index=('one', 'two', 'three', 'four', 'five'))
# 위와 같이 index를 설정하여 데이터에 이름을 지정할 수 있다. 단, data와 index의 갯수가 같아야한다.
print(series2)

dict_data = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
series3 = pd.Series(dict_data, dtype=np.float32, name='test')
print(series3)
# 위와 같이 dictionary로 series 데이터를 만들 수도 있다.

# indexing
print(series[0])  # series에는 'index' 설정이 되어있지않다. 하지만 순서 번호로 해당 series의 값에 접근할 수 있다.
print(series2['one'])  # series2는 'index' 설정이 되어있다. 해당 값을 해당 index로 접근할 수 있다.
print(series2[0])  # 또한 index 말고도 순서번호로도 접근할 수 있다.

print(series2.index)  # 해당 series의 index 리스트 반환
print(series2.values)  # 해당 series의 값 리스트 반환

series2.name = 'numbers'  # 해당 data(series)에 대한 이름
series2.index.name = 'alphabet'  # index의 이름
print(series2)

indexes = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
series4 = pd.Series(data=dict_data, index=indexes)
print(series4)
# index를 기준으로 series를 생성하는 방법, dict_data에는 five까지 밖에 값이 없으므로 six부터는 NaN 값이 할당된다.

