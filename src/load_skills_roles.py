import sqlite3
import pandas as pd 
  
df = pd.read_csv("data/processed/skills_roles.csv")

conn = sqlite3.connect("database/workforce.db")

cursor = conn.cursor()

cursor.execute("delete from skills_roles")

# apni chije insert kr rhe hain table me 
df.to_sql(
    "skills_roles",
    conn,
    if_exists="append",
    index = False
)
print("skills_roles data is loaded successfully.")

conn.commit()
conn.close()