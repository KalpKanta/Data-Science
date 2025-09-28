import pandas as pd

t = pd.read_csv("titanic.csv")
print(t.info())
print(t.describe())
print(t.head(880))
print(t.tail(10))
print(t.shape)
print(t["Survived"])
print(t["Name"].head(6))
print(t["Age"].max())
print(t["Age"].min())
print(t["Age"].count())
print(t["Age"].sum())
print(t[["Age", "Name"]])
thirty = t[t["Age"]>30]
survived = t[t["Survived"] == 1]
print(thirty)
print(survived)