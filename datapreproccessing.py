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

#encoding - Label encoding
            #data fame - 2d both rows and columns  
            #series - 1d only rows

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

#one-hot encoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
a = ColumnTransformer(transformers = [("encoder", OneHotEncoder(), [0])], remainder = "passthrough")
X = a.fit_transform(X)
print(X)

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size = 0.5, random_state = 6)
print(xtrain)

print(xtrain, ytrain)

#Scaling - Standard scaling
#z=(x−μ)/σ
from sklearn.preprocessing import StandardScaler
s = StandardScaler()
xtrain[:, 3: ] = s.fit_transform(xtrain[:, 3:])
xtest[:, 3: ] = s.transform(xtest[:, 3: ])
print(xtrain)
print(xtest)



#fit - providing the achine with info then the machine tries to learn from it
#transform - makes changes to the data
#fit_transform - learns from the information and also changes it