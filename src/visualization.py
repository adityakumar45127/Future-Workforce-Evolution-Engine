import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt 

df = pd.read_csv("data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")

plt.hist(df["Age"])

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()

plt.figure(figsize=(6, 4))

df["Attrition"].value_counts().plot(kind ="bar")

plt.title("Employee Attriton")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.show()

plt.figure(figsize=(8, 5))

df["Department"].value_counts().plot(kind = "bar")
plt.title("Employess by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()

plt.figure(figsize=(6,5))

df["Gender"].value_counts().plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")

plt.show()

plt.figure(figsize=(10,6))

df["JobRole"].value_counts().plot(kind="bar")

plt.title("Employees by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)

plt.show()

plt.figure(figsize=(8,5))

plt.hist(df["MonthlyIncome"], bins=20)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.show()

