import pandas as pd

# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
df_data = pd.read_csv('example.csv', sep=',', header=None)
# data_url에 있는 데이터를 sep에 해당하는 구분자로 가져옴
print(df_data)
print(df_data.head())  # 상위 5개를 가져옴

df_data.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV', 'TEST']
# df_data의 header 설정

df_data['weight_0'] = 1
# weight_0 컬럼 추가, 1로 값 setting
print(df_data.head())
df_data = df_data.drop('MEDV', axis=1)  # 'MEDV' Y축 값 제거
print(df_data.head())

df_matrix = df_data.values
# Matrix Data로 변환 !as_matrix()는 deprecated 되었다.
# as_matrix와 같이 쓰려면 values property를 사용한다.
print(df_matrix)