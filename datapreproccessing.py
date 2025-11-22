import numpy as np
import pandas as pd

#features
data = pd.read_csv("data.csv")
print(data.info())
X = data.iloc[:, 0:3]

#target
y = data.iloc[:, 3]
print(y)

print(X)