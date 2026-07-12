import sqlite3
import pandas as pd

df = pd.read_csv("data/processed/roles.csv")

conn = sqlite3.connect("database/workforce.db")

cursor = conn.cursor()
#purana data delete kr rhe hain
cursor.execute("delete from roles")

#khud se banaya hua csv file de rhe hain 

df.to_sql(
    "roles",
    conn,
    if_exists = "append",
    index = False
)
print("roles data loaded successfully.")
conn.commit()
conn.close()