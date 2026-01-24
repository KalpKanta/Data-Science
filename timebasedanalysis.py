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
#print(In)
print("..................................................................................................")


#Ind = I.loc[(I["DateReported"].dt.year == 2021) & (I["DateReported"].dt.month == 4) & (I["New_cases"] > 0), :]
Ind = In.loc[(In["New_cases"] > 0), "New_cases"].sum()
#print(Ind)

Indi = I.loc[(I["DateReported"].dt.year == 2020), :]
#print(Indi)

m = I.groupby(I["DateReported"].dt.year)["New_deaths"].mean().nlargest(2)
print(m)

m = I.groupby([I["DateReported"].dt.year, I["DateReported"].dt.month])["New_deaths"].sum()
print(m)