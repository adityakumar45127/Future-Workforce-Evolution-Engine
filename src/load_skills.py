import pandas as pd
import sqlite3


# ============================================================
# Load Skills CSV
# ============================================================

df = pd.read_csv("data/processed/skills.csv")


# ============================================================
# Add Required Database Columns
# ============================================================

required_columns = [
    "demand_score",
    "salary_impact",
    "difficulty",
    "future_score",
    "ai_resistance"
]

for column in required_columns:
    if column not in df.columns:
        df[column] = 0


# ============================================================
# Keep Database Column Order
# ============================================================

df = df[
    [
        "skill_id",
        "skill_name",
        "category",
        "demand_score",
        "salary_impact",
        "difficulty",
        "future_score",
        "ai_resistance"
    ]
]


# ============================================================
# Connect Database
# ============================================================

conn = sqlite3.connect("database/workforce.db")


# ============================================================
# Remove Existing Skills
# ============================================================

conn.execute("DELETE FROM skills")
conn.commit()


# ============================================================
# Insert Updated Skills
# ============================================================

df.to_sql(
    "skills",
    conn,
    if_exists="append",
    index=False
)


# ============================================================
# Verify
# ============================================================

count = conn.execute(
    "SELECT COUNT(*) FROM skills"
).fetchone()[0]

print(f"Successfully loaded {count} skills into database.")


conn.close()