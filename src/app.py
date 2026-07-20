import streamlit as st
import joblib 
import numpy as np
import pandas as pd 
import plotly.express as px
from skill_match_engine import *
from resume_parser import extract_text_from_resume
from resume_parser import detect_skills
from pdf_report import generate_report



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

model = joblib.load("models/career_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")

skills = get_skills(conn)
roles = get_roles(conn)
skills_roles = get_skills_roles(conn)

uploaded_resume = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"]
)


selected_skills = st.multiselect(
    "Select Your Skills",
    skills["skill_name"].tolist()
)

if uploaded_resume is not None :

    resume_text = extract_text_from_resume(uploaded_resume)

    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text[:20000],
        height = 500
    )

    detected_skills = detect_skills(
    resume_text,
    skills
)
    
    st.success("✅ Resume uploaded successfully!")

    if len(detected_skills) == 0:
        st.warning(
        "No matching skills found in the database. You can select skills manually."
        )
        st.metric(
            "Detected Skills",
            len(detected_skills)
            )


    st.subheader("✅ Detected Skills")

    st.write(detected_skills)


if uploaded_resume is not None:
    user_skills = detected_skills
else:
    user_skills = selected_skills


if st.button("Predict Career"):
    with st.spinner("Analyzying your skills.... ") :
        if len(user_skills) == 0:
            st.error("⚠ No skills found. Please upload a valid resume or select skills manually.")
            st.stop()

        clean_skills = user_skills
    
    user_skills_ids = convert_user_skills_to_ids(
        clean_skills,
        skills)
    
    feature_vector = []

    for _, skill in skills.iterrows():

         if skill["skill_id"] in user_skills_ids:
             feature_vector.append(1)
    
         else:
             feature_vector.append(0)

    feature_vector = np.array(feature_vector).reshape(1, -1)
    
    if len(user_skills_ids) == 0 :
        st.error("None of the entered skills were found in the database .")
        st.stop()
    
    best_role_id, best_role, best_score = recommend_best_role(
        user_skills_ids, 
        roles, 
        skills_roles)
    
    career_details = roles[roles["role_name"] == best_role].iloc[0]
    
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

        st.progress(best_score / 100)

    import plotly.graph_objects as go

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=best_score,
            title={"text": "Career Match Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 40], "color": "#ffcccc"},
                    {"range": [40, 70], "color": "#fff4cc"},
                    {"range": [70, 100], "color": "#d4f8d4"},
                ],
            },
        )
    )

    st.plotly_chart(gauge, use_container_width=True)

    st.subheader("Top 3 Career Recommendations")

    rank = 1
    for role_id, role, score in top_three_roles:
        st.write(f"{rank}. {role} : {round(score, 2)} %")
        rank += 1

    chart_data = pd.DataFrame(
        {
            "Career": [role for _, role, _ in top_three_roles],
            "Match Score": [score for _, _, score in top_three_roles],
        }
    )

    fig = px.bar(
        chart_data,
        x="Career",
        y="Match Score",
        text="Match Score",
        title="Top Career Match Scores",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.write(f"- {skill}")

    matched_skills = len(user_skills_ids)
    missing_count = len(missing_skills)

    pie_data = pd.DataFrame(
        {
            "Category": ["Matched Skills", "Missing Skills"],
            "Count": [matched_skills, missing_count],
        }
    )

    pie_fig = px.pie(
        pie_data,
        names="Category",
        values="Count",
        title="Skill Analysis",
    )

    prediction = model.predict(feature_vector)

    ml_prediction = encoder.inverse_transform(prediction)[0]

    probabilities = model.predict_proba(feature_vector)

    confidence = max(probabilities[0]) * 100

    col3, col4 = st.columns(2)

    with col3:
        st.success(f"🤖 AI Prediction\n\n{ml_prediction}")

    with col4:
        st.metric(
            label="AI Confidence",
            value=f"{confidence:.2f}%",
        )

    if best_role == ml_prediction:
        st.success("✅ Rule-Based and AI Prediction matched.")
    else:
        st.warning("⚠ Rule-Based and AI Prediction are different.")

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric(
            "💰 Average Salary",
            f"₹{career_details['base_salary']} LPA",
        )

    with col6:
        st.metric(
            "📈 Growth Score",
            career_details["growth_score"],
        )

    with col7:
        st.metric(
            "🤖 Automation Risk",
            career_details["automation_risk"],
        )

    st.subheader("Learning Roadmap")

    week = 1
    for skill in missing_skills:
        st.write(f"Week {week} : {skill}")
        week += 1

    st.plotly_chart(
        pie_fig,
        use_container_width=True,
    )

    report_filename = "Career_Report.pdf"

    generate_report(
        report_filename,
        best_role,
        best_score,
        ml_prediction,
        detected_skills if uploaded_resume is not None else selected_skills,
        missing_skills,
        career_details["base_salary"],
        career_details["growth_score"]
)
    
    with open(report_filename, "rb") as pdf_file:
        st.download_button(
        label="📄 Download Career Report",
        data=pdf_file,
        file_name="Career_Report.pdf",
        mime="application/pdf"
    )
        
    st.success("Career Analysis completed successfully!")