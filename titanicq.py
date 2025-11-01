import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t = pd.read_csv("titanic.csv")
print(t.info())
print(t.describe())
age = t.loc[t["Age"] > 30, "Name"].count()
print(age)


age = t["Age"]
bins = [0,10,20,30,40,50,60,70,80,90]
plt.hist(age, bins, rwidth = 0.8)
plt.xlabel("Age interval")
plt.ylabel("Number of people")
plt.title("Age groups (Titanic)")
plt.show()


survived = t.loc[t["Survived"] == 1, "Survived"].count()
nsurvived = t.loc[t["Survived"] == 0, "Survived"].count()
colours = ["green", "red"]
print(survived)
print(nsurvived)
plt.pie([survived, nsurvived], labels = [survived, nsurvived], colors = colours, autopct = "%1.1f%%")
plt.show()