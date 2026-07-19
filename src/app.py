import streamlit as st
import pandas as pd 
import plotly.express as px
from skill_match_engine import *


st.set_page_config(
    page_title = "Future Workforce Evolution Engine",
    page_icon = "🚀",
    layout = "wide"
)

st.title (" 🚀 Future Workforce Evolution Engine")

st.markdown(
    "AI - Powered Recommendation System"
)
st.divider()

st.sidebar.title("📌 Project Information")
st.sidebar.info("""
**Future Workforce Evolution Engine**
                
Version : 1.0 
                
Developer : Aditya Kumar
                
Tech Stack  
                
. \nPython
. \nSQLite
. \nPandas
. \nStreamlit 
                    
""")

conn = connect_database()

skills = get_skills(conn)
roles = get_roles(conn)
skills_roles = get_skills_roles(conn)


user_input = st.text_input(
    "Enter your Skills"
)

if st.button("Predict Career"):
    with st.spinner("Analyzying your skills.... ") :
        if user_input.strip() == "" :
            st.error("⚠ Please enter at least one skill.")
            st.stop()

            user_skills =  user_input.split(",")

    clean_skills = []
    
    for skill in user_skills :
        clean_skill = skill.strip()
        clean_skills.append(clean_skill)
    
    user_skills_ids = convert_user_skills_to_ids(
        clean_skills,
        skills)
    
    if len(user_skills_ids) == 0 :
        st.error("None of the entered skills were found in the database .")
        st.stop()
    
    best_role_id, best_role, best_score = recommend_best_role(
        user_skills_ids, 
        roles, 
        skills_roles)
    
    top_three_roles = get_top_three_roles(
        user_skills_ids,
        roles,
        skills_roles
    )
    
    required_skills = get_required_skills (
        best_role_id,
        skills_roles
    )

    missing_skills = get_missing_skills (
        user_skills_ids,
        required_skills,
        skills
    )
    
    # st.write("Best Role ", best_role)
    # st.write("Match Score ", round(best_score, 2), "%")

    col1, col2 = st.columns(2)

    with col1 :
        st.success(f"Best Career : \n {best_role}")
    
    with col2 :
        st.metric(
            label = "Match Score",
            value = f"{round(best_score, 2)}%"
        )

    st.progress(best_score/100)
        

    st.subheader("Top 3 Career Recommendations ")
    
    rank = 1
    for role_id, role, score in top_three_roles :
        st.write(f"{rank}. {role} : {round(score, 2)} %")
        rank = rank+1
    
    chart_data = pd.DataFrame(
    {
        "Career" : [role for _, role, _ in top_three_roles ],
        "Match Score" : [ score for _, _, score in top_three_roles ]
    }
)
    
    fig = px.bar(
        chart_data,
        x="Career",
        y="Match Score",
        text="Match Score",
        title="Top Career Match Scores"
    )
    st.plotly_chart(
        fig,
        use_container_width = True
    )

    st.subheader("Missing Skills ")

    for skill in missing_skills :
        st.write(f" - {skill}")

    matched_skills = len(user_skills_ids)
    missing_count = len(missing_skills)

    pie_data = pd.DataFrame(
        {
        "Category" : ["Matched Skills", "Missing Skills"],
        "Count" : [matched_skills, missing_count ]
        }
    )

    pie_fig = px.pie(
        pie_data,
        names= "Category",
        values="Count",
        title = "Skill Analysis"
    )
    

    st.subheader("Learning Roadmap")

    week = 1
    for skill in missing_skills :
        st.write(f"Week {week} : {skill}")
        week = week + 1
    
    st.plotly_chart(
        pie_fig,
        use_container_width = True
    )

    

    st.success("Career Analysis completed successfully !")


st.divider()
st.caption (
    "© 2026 Aditya Kumar | Built using Python . SQLite . Pandas . Streamlit"
    )