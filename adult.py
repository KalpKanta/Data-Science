import pandas as pd

cols = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", 
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", 
        "hours-per-week", "native-country", "income"]

df = pd.read_csv('adult.csv', names=cols, skipinitialspace=True)

low_income = df[df['income'] == '<=50K']

job_counts = low_income['occupation'].value_counts()
print("Number of people earning <=50K by job:")
print(job_counts)

print(df.info())
print(len(df.columns))
print(df["occupation"].count())

low_income = df.loc[df['income'] == '<=50K', "income"].count()
print("LI: ", low_income)
#low_income_p = low_income 

high_income = df.loc[df["income"] == ">50K", "income"].count()
print("HI: ", high_income)

total = low_income + high_income
low_income_p = low_income/total * 100
high_income_p = high_income/total * 100
print(low_income_p)
print(high_income_p)

average_age = df.loc[df["income"] == ">50K", "age"].mean()
print(average_age)

gender = df.groupby(["sex", "income"])["age"].count()
print(gender)