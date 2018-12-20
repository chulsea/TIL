import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/HighLvRiver/PythonLearning/master/Study/Ecommerce%20Purchases"
df = pd.read_csv(url)
print(df.columns)
print(df[["Address", "Lot"]].head())
df["num AP"] = np.where(df["AM or PM"] == "AM", 0, 1)
print(df["AM or PM"].tail())
print(df["num AP"].tail())
print(df.columns)

i = df.index
mask = i.map(lambda t: t if["num AP"][t] == 1 else 0)
print(mask)
