import numpy as np
import pandas as pd

#features - 2d data set
data = pd.read_csv("data.csv")
print(data.info())
print(data.isnull().sum())

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer.fit(data.iloc[:, 1:3])
data.iloc[:, 1:3] = imputer.transform(data.iloc[:, 1:3])
print(data)

#sperating the datset into features and tagets
X = data.iloc[:, 0:3]

#target- single columm
y = data.iloc[:, 3]
print(y)
print(X)

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size = 0.5, random_state = 6)
print(xtrain)