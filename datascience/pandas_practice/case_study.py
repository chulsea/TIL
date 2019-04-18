import pandas as pd, dateutil
# Data

df_phone = pd.read_csv('phone_data.csv')
print(df_phone.head())
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)
print(df_phone.head())

df_phone_duration = df_phone.groupby('month')['duration'].sum()
print(type(df_phone_duration))
print(df_phone_duration)

df_phone_call = df_phone[df_phone['item'] == 'call'].groupby('network')['duration'].sum()
print(df_phone_call)