import pandas as pd, numpy as np
# pandas data frame selection
raw_data = {
    'first_name': ['gyeongcheol', 'wooje', 'hohyun'],
    'last_name': ['park', 'noh', 'kim'],
    'age': [27, 27, 28]
}

df = pd.DataFrame(raw_data)
print(df)

# 한개의 column 선택
print(df['first_name'])
# print(df['first']) 만약 없는 값인 경우 오류

# 한개 이상의 column 선택
print(df[['first_name', 'last_name']])

# column의 이름 없이 index number를 사용하는 경우 row를 기준으로 표시한다.
print(df[:2])
# column이름과 함께 row index를 사용하면 해당 column만 indexing할 수 있다.
print(df['last_name'][:2])

# 1개 이상의 index를 가져올때 list에 가져오고자 하는 index를 담아서 가져올 수 있다. (Series)
print(df['first_name'][[0, 2]])

# numpy의 boolean index도 활용가능하다.
print(df['age'][df['age'] == 27])
