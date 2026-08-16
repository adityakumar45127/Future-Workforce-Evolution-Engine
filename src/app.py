import streamlit as st
import joblib
import numpy as np
import pandas as pd

from skill_match_engine import *
from resume_parser import extract_text_from_resume, detect_skills
from pdf_report import generate_report


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Future Workforce Evolution Engine",
    page_icon="🚀",
    layout="wide",
)


# ============================================================
# HEADER
# ============================================================

st.title("🚀 Future Workforce Evolution Engine")
st.subheader("AI-Powered Career Recommendation System")
st.caption(
    "Resume intelligence • Skill-gap analysis • ML career prediction • "
    "Personalized learning roadmap"
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📌 Project Information")

st.sidebar.info(
    """
**Future Workforce Evolution Engine**

**Version:** 2.0

**Developer:** Aditya Kumar

**Tech Stack**
- Python
- SQLite
- Pandas
- Scikit-learn
- Random Forest
- Streamlit
"""
)

st.sidebar.success("🟢 Model loaded")
st.sidebar.success("🟢 Database connected")
st.sidebar.info("30 ML features")


# ============================================================
# DATABASE & MODEL
# ============================================================

conn = connect_database()

model = joblib.load("models/career_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")

skills = get_skills(conn)
roles = get_roles(conn)
skills_roles = get_skills_roles(conn)


# ============================================================
# INPUT SECTION
# ============================================================

st.header("1️⃣ Candidate Input")

# ------------------------------------------------------------
# Session-state controls
# ------------------------------------------------------------

if "resume_widget_version" not in st.session_state:
    st.session_state["resume_widget_version"] = 0

if "selected_skills" not in st.session_state:
    st.session_state["selected_skills"] = []

if "processed_file_id" not in st.session_state:
    st.session_state["processed_file_id"] = None


# ------------------------------------------------------------
# Callback:
# If the user starts selecting a manual skill, clear the PDF.
# ------------------------------------------------------------

def clear_resume_when_manual_skill_selected():
    if st.session_state.get("selected_skills"):
        st.session_state["resume_widget_version"] += 1
        st.session_state["processed_file_id"] = None


upload_col, manual_col = st.columns(2)


with upload_col:

    st.subheader("📄 Resume Upload")

    uploaded_resume = st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        key=f"resume_uploader_{st.session_state['resume_widget_version']}",
        help="Upload a PDF resume for automatic skill detection.",
    )


with manual_col:

    st.subheader("🧩 Manual Skills")

    # If a new PDF is uploaded, clear all previous manual selections.
    current_file_id = (
        f"{uploaded_resume.name}-{getattr(uploaded_resume, 'size', 0)}"
        if uploaded_resume is not None
        else None
    )

    previous_file_id = st.session_state.get("processed_file_id")

    if (
        uploaded_resume is not None
        and current_file_id != previous_file_id
    ):
        st.session_state["selected_skills"] = []
        st.session_state["processed_file_id"] = current_file_id

    selected_skills = st.multiselect(
        "Select your skills",
        skills["skill_name"].tolist(),
        key="selected_skills",
        placeholder="Choose skills...",
        on_change=clear_resume_when_manual_skill_selected,
    )

    if uploaded_resume is not None:
        st.caption(
            "📄 Resume mode is active. Selecting a manual skill "
            "will automatically remove the uploaded PDF."
        )


# ============================================================
# RESUME PROCESSING
# ============================================================

detected_skills = []
resume_text = ""

if uploaded_resume is not None:

    resume_text = extract_text_from_resume(uploaded_resume)

    detected_skills = detect_skills(
        resume_text,
        skills
    )

    st.success("✅ Resume uploaded and processed successfully.")

    resume_col1, resume_col2 = st.columns([2, 1])

    with resume_col1:
        with st.expander("🔍 View Extracted Resume Text"):
            st.text_area(
                "Extracted Text",
                resume_text[:20000],
                height=350,
                label_visibility="collapsed",
            )

    with resume_col2:
        st.metric(
            "Detected Skills",
            len(detected_skills)
        )

        st.write("**Detected Skills:**")

        if detected_skills:
            st.write(detected_skills)
        else:
            st.warning(
                "No matching skills detected. "
                "Remove the PDF if you want to use manual skills."
            )


# ============================================================
# ACTIVE INPUT
# ============================================================

if uploaded_resume is not None:
    user_skills = detected_skills
    input_mode = "Resume"
else:
    user_skills = selected_skills
    input_mode = "Manual"


if user_skills:

    st.divider()
    st.subheader("📋 Input Summary")

    summary1, summary2, summary3 = st.columns(3)

    with summary1:
        st.metric("Input Mode", input_mode)

    with summary2:
        st.metric("Skills Provided", len(user_skills))

    with summary3:
        st.metric("ML Features", 30)

    if uploaded_resume is not None:
        st.caption(
            "PDF mode is active: manual selections were cleared. "
            "The prediction uses skills detected from the resume."
        )


# ============================================================
# PREDICTION
# ============================================================

if st.button(
    "🚀 Analyze Career Profile",
    type="primary",
    use_container_width=True,
):

    with st.spinner("Analyzing your career profile..."):

        # ----------------------------------------------------
        # Validate input
        # ----------------------------------------------------

        if len(user_skills) == 0:
            st.error(
                "⚠ No skills found. Please upload a valid resume "
                "or select skills manually."
            )
            st.stop()

        clean_skills = user_skills

        # ----------------------------------------------------
        # Skill IDs
        # ----------------------------------------------------

        user_skills_ids = convert_user_skills_to_ids(
            clean_skills,
            skills
        )

        if len(user_skills_ids) == 0:
            st.error(
                "None of the entered skills were found in the database."
            )
            st.stop()

        # ----------------------------------------------------
        # 30 ML features
        # ----------------------------------------------------

        model_features = [
            "Python",
            "SQL",
            "NumPy",
            "Pandas",
            "Excel",
            "Power BI",
            "Statistics",
            "Git",
            "GitHub",
            "Machine Learning",
            "Scikit-learn",
            "XGBoost",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "NLP",
            "Computer Vision",
            "Matplotlib",
            "Seaborn",
            "Tableau",
            "Data Visualization",
            "AWS",
            "Docker",
            "Apache Spark",
            "Apache Airflow",
            "ETL",
            "Data Warehousing",
            "Flask",
            "FastAPI",
            "REST API",
        ]

        feature_vector = np.array(
            [
                1 if feature in clean_skills else 0
                for feature in model_features
            ]
        ).reshape(1, -1)

        if feature_vector.shape[1] != 30:
            st.error(
                f"Feature vector has {feature_vector.shape[1]} features, "
                "but the model expects 30."
            )
            st.stop()

        # ----------------------------------------------------
        # Rule-based recommendation
        # ----------------------------------------------------

        best_role_id, best_role, best_score = recommend_best_role(
            user_skills_ids,
            roles,
            skills_roles
        )

        career_details = roles[
            roles["role_name"] == best_role
        ].iloc[0]

        top_three_roles = get_top_three_roles(
            user_skills_ids,
            roles,
            skills_roles
        )

        required_skills = get_required_skills(
            best_role_id,
            skills_roles
        )

        missing_skills = get_missing_skills(
            user_skills_ids,
            required_skills,
            skills
        )

        # ----------------------------------------------------
        # ML prediction
        # ----------------------------------------------------

        prediction = model.predict(feature_vector)

        ml_prediction = encoder.inverse_transform(
            prediction
        )[0]

        probabilities = model.predict_proba(
            feature_vector
        )

        confidence = float(
            max(probabilities[0]) * 100
        )


        # ====================================================
        # DASHBOARD
        # ====================================================

        st.divider()
        st.header("2️⃣ Career Intelligence Dashboard")

        # Main career results
        result1, result2 = st.columns(2)

        with result1:
            st.success(
                f"🎯 Recommended Career\n\n"
                f"## {best_role}"
            )

        with result2:
            st.info(
                f"🤖 ML Prediction\n\n"
                f"## {ml_prediction}"
            )

        # KPI row
        k1, k2, k3, k4 = st.columns(4)

        with k1:
            st.metric(
                "🎯 Match Score",
                f"{best_score:.1f}%"
            )

        with k2:
            st.metric(
                "🧠 Prediction Confidence",
                f"{confidence:.1f}%"
            )

        with k3:
            st.metric(
                "💰 Average Salary",
                f"₹{career_details['base_salary']} LPA"
            )

        with k4:
            st.metric(
                "📈 Growth Score",
                career_details["growth_score"]
            )

        # Match progress
        st.subheader("Career Match")

        st.progress(
            min(max(best_score / 100, 0), 1)
        )

        st.caption(
            f"Career match score: {best_score:.2f}%"
        )


        # ====================================================
        # TOP 3 CAREERS
        # ====================================================

        st.subheader("🏆 Top 3 Career Recommendations")

        for rank, (_, role, score) in enumerate(
            top_three_roles,
            start=1
        ):

            role_col1, role_col2 = st.columns([2, 1])

            with role_col1:
                st.write(
                    f"**{rank}. {role}**"
                )

            with role_col2:
                st.write(
                    f"**{score:.2f}%**"
                )

            st.progress(
                min(max(score / 100, 0), 1)
            )


        # ====================================================
        # PREDICTION AGREEMENT
        # ====================================================

        if best_role == ml_prediction:
            st.success(
                "✅ Rule-based matching and ML prediction agree."
            )
        else:
            st.warning(
                f"⚠ Rule-based recommendation: **{best_role}**  \n"
                f"ML prediction: **{ml_prediction}**"
            )


        # ====================================================
        # CAREER PROFILE
        # ====================================================

        st.header("3️⃣ Career Profile")

        p1, p2, p3 = st.columns(3)

        with p1:
            st.metric(
                "💰 Average Salary",
                f"₹{career_details['base_salary']} LPA"
            )

        with p2:
            st.metric(
                "📈 Growth Score",
                career_details["growth_score"]
            )

        with p3:
            st.metric(
                "🤖 Automation Risk",
                career_details["automation_risk"]
            )


        # ====================================================
        # SKILL GAP
        # ====================================================

        st.header("4️⃣ Skill Gap Analysis")

        gap1, gap2 = st.columns(2)

        with gap1:

            st.subheader("✅ Matched Skills")

            matched_names = [
                skill
                for skill in clean_skills
                if skill in model_features
            ]

            st.metric(
                "Matched Skills",
                len(matched_names)
            )

            if matched_names:
                for skill in matched_names:
                    st.write(f"• {skill}")

        with gap2:

            st.subheader("📚 Missing Skills")

            st.metric(
                "Skills to Develop",
                len(missing_skills)
            )

            if missing_skills:
                for skill in missing_skills:
                    st.write(f"• {skill}")
            else:
                st.success(
                    "🎉 No major missing skills identified."
                )


        # ====================================================
        # LEARNING ROADMAP
        # ====================================================

        st.header("5️⃣ Recommended Skill Development Roadmap")

        if missing_skills:

            for week, skill in enumerate(
                missing_skills,
                start=1
            ):

                st.info(
                    f"**Week {week}**  \n"
                    f"🎓 {skill}"
                )

        else:

            st.success(
                "You already have the required skills "
                "for this career path."
            )


        # ====================================================
        # PDF REPORT
        # ====================================================

        st.header("6️⃣ Career Report")

        report_filename = "Career_Report.pdf"

        report_skills = (
            detected_skills
            if uploaded_resume is not None
            else selected_skills
        )

        generate_report(
            report_filename,
            best_role,
            best_score,
            ml_prediction,
            report_skills,
            missing_skills,
            career_details["base_salary"],
            career_details["growth_score"]
        )

        with open(
            report_filename,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="📄 Download Career Report",
                data=pdf_file,
                file_name="Career_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        st.success(
            "✅ Career analysis completed successfully!"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Future Workforce Evolution Engine • "
    "Resume-to-Career Intelligence Platform"
)