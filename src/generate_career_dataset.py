import pandas as pd
import numpy as np


# ============================================================
# Configuration
# ============================================================

SKILLS_PATH = "data/processed/skills.csv"
ROLES_PATH = "data/processed/roles.csv"
MAPPINGS_PATH = "data/processed/skills_roles.csv"
OUTPUT_PATH = "data/processed/career_dataset.csv"

SAMPLES_PER_ROLE = 200
RANDOM_STATE = 42


# ============================================================
# Load Data
# ============================================================

skills = pd.read_csv(SKILLS_PATH)
roles = pd.read_csv(ROLES_PATH)
mappings = pd.read_csv(MAPPINGS_PATH)

rng = np.random.default_rng(RANDOM_STATE)

skill_columns = skills["skill_name"].tolist()


# ============================================================
# Generate Skill Profiles
# ============================================================

records = []

for _, role in roles.iterrows():

    role_id = role["role_id"]
    role_name = role["role_name"]

    role_mappings = mappings[
        mappings["role_id"] == role_id
    ]

    importance_map = dict(
        zip(
            role_mappings["skill_id"],
            role_mappings["importance"]
        )
    )

    for _ in range(SAMPLES_PER_ROLE):

        profile = {}

        for _, skill in skills.iterrows():

            skill_id = skill["skill_id"]
            skill_name = skill["skill_name"]

            if skill_id in importance_map:

                importance = importance_map[skill_id]

                # Higher importance → higher probability
                probability = 0.45 + (importance / 10) * 0.45

                profile[skill_name] = int(
                    rng.random() < probability
                )

            else:

                # Non-required skills occasionally appear
                profile[skill_name] = int(
                    rng.random() < 0.05
                )

        profile["Career"] = role_name

        records.append(profile)


# ============================================================
# Create DataFrame
# ============================================================

df = pd.DataFrame(records)

# Ensure column order
df = df[skill_columns + ["Career"]]


# ============================================================
# Remove Exact Duplicates
# ============================================================

before = len(df)

df = df.drop_duplicates().reset_index(drop=True)

after = len(df)

print("Rows before duplicate removal:", before)
print("Rows after duplicate removal :", after)
print("Duplicates removed            :", before - after)


# ============================================================
# Save Dataset
# ============================================================

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nDataset generated successfully.")
print("Dataset Shape:", df.shape)
print("\nCareer Distribution:")
print(df["Career"].value_counts())

print("\nSaved to:")
print(OUTPUT_PATH)