import pandas as pd

data = pd.read_csv("covid.csv")
print(data.info())
print(data.describe())
data["DateReported"] = pd.to_datetime(data["DateReported"])
print(data.info())
print(data.loc[data["Country"] == "India", :])
print(data[["New_cases", "DateReported"]].groupby("DateReported").sum())
print(data[["New_deaths", "DateReported"]].groupby("DateReported").sum())
I = data.loc[data["Country"] == "India", :]
In = I.loc[(I["DateReported"].dt.year == 2021) & (I["DateReported"].dt.month == 4), :]
print(In)