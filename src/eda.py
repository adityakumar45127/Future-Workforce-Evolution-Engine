#isme data analysis kr rhe hain bs 

import pandas as pd 
df = pd.read_csv("data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("\n Attrition Count")
print(df["Attrition"].value_counts())

print("\nDepartment Counts")
print(df["Department"].value_counts())

print("\nMonthly Salary")
print(df["MonthlyIncome"].value_counts)

print("\nJobRole")
print(df["JobRole"].value_counts())

print("\nGender")
print(df["Gender"].value_counts())

