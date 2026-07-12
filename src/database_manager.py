import sqlite3
import pandas as pd

df = pd.read_csv("data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# connecting database 
conn = sqlite3.connect("database/workforce.db")

#storing dataframe into SQL table 

df.to_sql(
    "employees",
    conn,
    if_exists = "replace",
    index = False
)

print("Database Created Successfully !")
print("Table Name :" "employees")
print("Total Records :", len(df))


cursor = conn.cursor()

#skillss table 

cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
               skill_id integer primary key autoincrement,
               skill_name text not null,
               category text not null ,
               demand_score integer not null,
               salary_impact integer not null,
               difficulty integer not null,
               future_score integer not null ,
               ai_resistance integer not null)
""")

print("Skills table created successfully")
conn.commit()

cursor = conn.cursor()

# creating roles table 
cursor.execute("""
create table if not exists roles (
               role_id integer primary key not null,
               role_name text not null,
               category text not null,
               base_salary real not null,
               growth_score integer not null,
               automation_risk integer not null)
               
""")
print("Roles table created successfully")

conn.commit()

cursor = conn.cursor()

cursor.execute("""
create table if not exists skills_roles(
              role_skill_id integer primary key autoincrement,
               role_id   integer ,
               skill_id   integer,
               importance  integer
                )
               
""")
print("role_skills table created successfully")
conn.commit()
conn.close()