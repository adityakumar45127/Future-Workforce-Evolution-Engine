import pandas as pd
import sqlite3
import random

conn = sqlite3.connect("database/workforce.db")

skills = pd.read_sql_query("SELECT * FROM skills", conn)
roles = pd.read_sql_query("SELECT * FROM roles", conn)
skills_roles = pd.read_sql_query("SELECT * FROM skills_roles", conn)

conn.close()

skill_map = dict(zip(skills["skill_id"], skills["skill_name"]))

dataset = []

for _, role in roles.iterrows():

    role_id = role["role_id"]
    role_name = role["role_name"]

    role_skills = skills_roles[
        skills_roles["role_id"] == role_id
    ]

    for _ in range(200):

        sample = {}

        # Initialize every skill to 0
        for _, skill in skills.iterrows():
            sample[skill["skill_name"]] = 0

        # Fill required skills according to importance
        for _, row in role_skills.iterrows():

            skill_name = skill_map[row["skill_id"]]
            importance = row["importance"]

            if importance >= 9:
                probability = 98
            elif importance >= 7:
                probability = 90
            elif importance >= 5:
                probability = 75
            else:
                probability = 50

            sample[skill_name] = random.choices(
                [1, 0],
                weights=[probability, 100 - probability]
            )[0]

        sample["Career"] = role_name

        dataset.append(sample)

career_df = pd.DataFrame(dataset)

career_df.to_csv(
    "data/processed/career_dataset.csv",
    index=False
)

print(career_df.head())
print(career_df.shape)

print("Dataset Generated Successfully")