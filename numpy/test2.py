import pandas as pd
import numpy as np
# df = pd.DataFrame([[1,2], [3,4], [5,6]], columns=["first", "second"])
# df.to_csv("numpy/test.csv", index=False)

df = pd.read_csv("numpy/test.csv")
print(df)

row0 = df.ix[0]
row0_loc = df.loc[0]
print(row0)
print(row0_loc)

# df["third"] = pd.Series([7,8,9])
df.loc[:, "third"] = [7,8,9]
print(df)

df2 = pd.DataFrame([[10],[11],[12]], index=[4,5,6], dtype=np.int)
df = df.append()
print(df)