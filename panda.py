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


#extracting a particular column out of a conditon
an = t.loc[t["Age"]>18, "Name"]
print(an)
iloc = t.iloc[2:5, 5:10]
print(iloc)
t.iloc[0:5, 2] = "Hello"
print(t.head())
#Adding new columns to the new file
t["Discount"] = t["Fare"]/10
t["Total price"] = t["Fare"] - t["Discount"]
t.to_csv("New File.csv")
#renaming the column
t_renamed = t.rename(columns = {"Survived":"Lived", "Sex":"Gender"})
print(t_renamed.info())
#Mean age
ma = t["Age"].mean()
print(ma)
#Min, max, median, mean, and sum all cannot be applied on non-numeric data
m = t[["Age", "Fare"]].mean()
print(m)

a = t.agg({"Age":["min", "median", "max"], "Fare":["sum", "median", "mean"]})
print(a)

print(t["Survived"].value_counts())
print(t["Pclass"].value_counts())

#grouping data categorically
print(t[["Sex", "Age"]].groupby("Sex").max())
print(t[["Age", "Sex"]].groupby("Sex").mean())
print(t[["Fare", "Pclass"]].groupby("Pclass").max())
print(t[["Fare", "Pclass"]].groupby("Pclass").mean())
print(t.groupby("Pclass")["Name"].count())

#sorting the data
t1 = t.sort_values(by = "Age")
print(t1[["Name", "Age"]])

t2 = t.sort_values(by = "Fare", ascending = False)
print(t2[["Name", "Fare"]])

#operations for the text data
t["Name"].str.split(",")
t["Surname"] = t["Name"].str.split(" ").str.get(-1)
print(t["Surname"])

t["Name"].str.lower()
t["Lowercase Name"] = t["Name"].str.lower()
print(t["Lowercase Name"])

t["Gender"] = t["Sex"].replace({"male":"M", "female":"F"})
print(t["Gender"])