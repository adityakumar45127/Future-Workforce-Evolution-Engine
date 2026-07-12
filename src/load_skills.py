import sqlite3 
import pandas as pd 

df = pd.read_csv("data/processed/skills.csv")

conn = sqlite3.connect("database/workforce.db")

cursor = conn.cursor()

#delete kr rhe old data ko
cursor.execute("delete from skills")

#storing khud ka data banaya hua into skills table
df.to_sql(
    "skills",
    conn,
    if_exists="append",
    index=False
)
print("Skills data loaded successfully.")
conn.commit()
conn.close()



