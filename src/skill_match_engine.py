# imports

import pandas as pd 
import sqlite3 

# databse functions 

def connect_database() :
    conn = sqlite3.connect("database/workforce.db")
    return conn 


def get_roles(conn) :
    query = "select * from roles"
    roles_df = pd.read_sql_query(query, conn)
    return roles_df


def get_skills(conn) :
    query = "select *from skills"
    skills_df = pd.read_sql_query(query, conn)
    return skills_df

def get_skills_roles(conn) :
    query = "select * from skills_roles"
    skills_roles_df = pd.read_sql_query(query, conn)
    return skills_roles_df

# Helper Functions 

def get_skill_id(skill_name, skills_df) :
    result = skills_df[skills_df["skill_name"] == skill_name]

    if result.empty:
        return None
    return  int( result.iloc[0]["skill_id"])

def convert_user_skills_to_ids(user_skills, skills_df) :
    skill_ids = []
    for skill in user_skills :
        skill_id = get_skill_id(skill, skills_df)
        if skill_id is not None:
            skill_ids.append(skill_id)
    return skill_ids


def get_required_skills(role_id, skills_roles_df):
    required_skills = skills_roles_df[
        skills_roles_df["role_id"] == role_id]
    return required_skills

# Recommendation Engine 

def calculate_match_score(user_skills_ids, required_skills) :
    total_weight = 0
    matched_weight = 0

    for index , row in required_skills.iterrows():
        skill_id = row["skill_id"]
        importance = row["importance"]
        total_weight =  total_weight + importance

        if skill_id in user_skills_ids :

            matched_weight = matched_weight + importance

    if total_weight == 0 :
        return 0

    match_percentage = (matched_weight / total_weight) * 100
    return match_percentage

def recommend_best_role(user_skills_ids, roles, skills_roles) :
    best_score = 0 
    best_role = None

    for index , row in roles.iterrows() :

        role_id = row["role_id"]
        role_name = row["role_name"]

        required_skills = get_required_skills(role_id, skills_roles) 
        
        match_score = calculate_match_score(user_skills_ids, required_skills)
        
        if match_score > best_score :
            best_score = match_score 
            best_role = role_name

    return best_role, best_score 

# main program 

if __name__ == "__main__" :
    conn = connect_database()
    # print("Database connected Successfully")

    roles =  get_roles(conn)
    # print("Roles Table")
    # print(roles)

    skills = get_skills(conn)
    # print("Skills Table")
    # print(skills)

    skills_roles = get_skills_roles(conn)
    # print("Skills_roles Table")
    # print(skills_roles)

    required_skills = get_required_skills(1, skills_roles)
    # print("Required Skills for Role ID 1")
    # print(required_skills)

    user_skills = [
        "Python",
        "SQL",
        "Git"
    ]

    user_skills_ids = convert_user_skills_to_ids(user_skills, skills)
    # print("User skills_ids")
    # print(user_skills_ids)

    best_role , best_score = recommend_best_role(
        user_skills_ids,
        roles,
        skills_roles
    )
    print("\n  ===================  ")
    print("\n  Future Workforce Evolution Engine  ")

    print("\n User Skills  ")
    for skill in user_skills :
        print("-", skill)

    print("\n Career Recommendation")
    print("Best Role :" , best_role)
    print("Match Score :", round(best_score,2), "%")


    conn.close()