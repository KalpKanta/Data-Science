import pandas as pd


data = pd.read_csv("covid_data.csv")
print(data.info())
print(data.isnull().sum())
print(data.head)
data = data[["Province_State", "Country_Region", "Confirmed", "Recovered", "Deaths", "Active"]]
data.columns = ("State", "Country", "Confirmed", "Rec", "Deaths", "Active")
print(data.info())
print(data.head())
print(data.loc[data["Country"]== "US", :])
print(data.groupby("Country").get_group("US").count())

import plotly
import plotly.express as px
import plotly.graph_objects as go

Top10ConfirmedCases = data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values()

print(Top10ConfirmedCases)

#highest number of recovered cases and the highest number of deaths and highest number of active cases and then also do all those <--- for 5 states of one of the countries

Top10Recovered = data.groupby("Country")["Rec"].sum().nlargest(10).sort_values()
print(Top10Recovered)

Top10Deaths = data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values()
print(Top10Deaths)

Top10Active = data.groupby("Country")["Active"].sum().nlargest(10).sort_values()
print(Top10Active)

us_data = data.groupby("Country").get_group("US")

Top5USRecovered = us_data.nlargest(5, "Rec")

Top5USDeaths = us_data.nlargest(5, "Deaths")

Top5USActive = us_data["Active"].nlargest(5)

figure1 = px.scatter(Top5USDeaths, x = Top5USDeaths["State"], y = Top5USDeaths ["Deaths"], color = "Deaths", size_max = 100, size = "Deaths", color_continuous_scale = ["Lime", "Red"])
figure1.write_html("figure1.html", auto_open = True)