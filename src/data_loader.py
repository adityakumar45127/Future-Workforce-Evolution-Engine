"""
Future Workforce Evolution Engine v1
Author : Aditya Kumar
Module : Data Loader
"""
import pandas as pd 
df = pd.read_csv("data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("=" * 60)
print("Future Workforce Evolution Engine")
print("=" * 60)

print("\n fisrt 5 rows")
print(df.head())

print("\n shape of dataset")
print(df.shape)

print("\ncolumns names")
print(df.columns.tolist())

print("\n dataset information")
print(df.info())

print("\n describe datasets")
print(df.describe())

print(df["MonthlyIncome"].max())
print(df["Age"].min())