# 🚀 Future Workforce Evolution Engine

> **An AI-powered Career Intelligence System that analyzes user skills, compares them with industry role requirements using a weighted skill matching algorithm, and recommends the most suitable career path with interactive visualizations.**

![Status](https://img.shields.io/badge/Status-Version%201.0-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Plotly](https://img.shields.io/badge/Visualization-Plotly-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 Project Overview

Future Workforce Evolution Engine is an AI-inspired career recommendation system that evaluates a user's technical skills against multiple industry roles and recommends the best career based on a weighted skill matching algorithm.

Unlike simple keyword matching systems, this project assigns importance weights to individual skills required for each role and calculates an overall match percentage, making recommendations more meaningful and realistic.

The system also identifies missing skills, generates a personalized learning roadmap, and visualizes career recommendations through an interactive Streamlit dashboard.

This project has been designed with modular architecture so that Machine Learning based recommendations and AI-driven workforce analytics can be integrated in future versions.

---

# ✨ Features

### Career Recommendation Engine
- ✅ Weighted Skill Matching Algorithm
- ✅ Best Career Recommendation
- ✅ Top 3 Career Recommendations
- ✅ Match Score Calculation

### Skill Intelligence
- ✅ Missing Skills Detection
- ✅ Personalized Learning Roadmap
- ✅ Skill ID Conversion
- ✅ Skill Weight Analysis

### Dashboard
- ✅ Interactive Streamlit Web Application
- ✅ Career Recommendation Dashboard
- ✅ Progress Bar
- ✅ Bar Chart Visualization
- ✅ Pie Chart Skill Analysis
- ✅ Input Validation

### Database
- ✅ SQLite Database Integration
- ✅ Skills Database
- ✅ Career Roles Database
- ✅ Role-Skill Mapping

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| SQLite | Database |
| Pandas | Data Processing |
| Streamlit | Interactive Web Dashboard |
| Plotly | Interactive Data Visualization |

---

# 📂 Project Structure

```text
Future-Workforce-Evolution-Engine
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── workforce.db
│
├── src/
│   ├── app.py
│   ├── skill_match_engine.py
│   ├── load_skills.py
│   ├── load_roles.py
│   ├── load_skills_roles.py
│   └── visualization.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# 🗄 Database Schema

The recommendation engine uses the following database tables.

| Table | Description |
|--------|-------------|
| skills | Stores technical skills |
| roles | Stores career roles |
| skills_roles | Maps skills to career roles with importance weights |
| employees | Employee dataset (Future Analytics Module) |

---

# ⚙️ Recommendation Workflow

```text
              User Skills
                   │
                   ▼
          Skill ID Conversion
                   │
                   ▼
           SQLite Database
                   │
                   ▼
      Required Skills Retrieval
                   │
                   ▼
     Weighted Skill Matching
                   │
                   ▼
        Match Score Calculation
                   │
                   ▼
       Best Career Recommendation
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
 Missing Skills      Top 3 Careers
         │                   │
         └─────────┬─────────┘
                   ▼
      Learning Roadmap Generator
                   │
                   ▼
        Streamlit Interactive Dashboard
```

---

# 🧠 Recommendation Algorithm

The recommendation engine performs the following steps:

1. Accept user skills.
2. Convert skills into Skill IDs.
3. Retrieve required skills for every career.
4. Compare user skills with required skills.
5. Calculate weighted match scores.
6. Recommend the highest matching career.
7. Identify missing skills.
8. Generate a personalized learning roadmap.

### Weighted Match Score

```text
Match Score =
(Matched Skill Weight / Total Required Skill Weight) × 100
```

---

# 📊 Dashboard Features

The Streamlit dashboard provides:

- 🎯 Best Career Recommendation
- 📈 Match Score
- 📊 Top 3 Career Recommendations
- 📉 Career Match Bar Chart
- 🥧 Skill Analysis Pie Chart
- 📚 Missing Skills
- 🛣 Personalized Learning Roadmap

---

# 📈 Current Progress

```text
Overall Progress

██████████████████░░ 90%

✅ Database Layer

✅ Data Loading Modules

✅ Weighted Skill Matching Engine

✅ Career Recommendation Engine

✅ Streamlit Dashboard

✅ Top 3 Recommendations

✅ Missing Skills Detection

✅ Learning Roadmap

✅ Interactive Charts

⏳ Machine Learning Recommendation

⏳ AI Workforce Analytics
```

---

# 🚀 Version Roadmap

## ✅ Version 1.0 (Completed)

- SQLite Database
- Skills Database
- Career Roles Database
- Role-Skill Mapping
- Weighted Skill Matching Algorithm
- Career Recommendation Engine
- Top 3 Career Recommendations
- Missing Skills Detection
- Learning Roadmap Generation
- Interactive Streamlit Dashboard
- Plotly Visualizations
- Progress Indicator
- Input Validation

---

## 🚀 Version 2.0 (Coming Soon)

- Machine Learning Recommendation System
- Resume-Based Skill Analysis
- Future Workforce Prediction
- Salary Prediction
- AI Career Trend Analysis
- Personalized Career Growth Prediction
- Resume Upload Support
- PDF Career Report Generation

---

# 🎯 Future Vision

The final platform aims to answer:

- Which career best matches my skills?
- Which skills should I learn next?
- What are my missing skills?
- Which career has the highest future demand?
- Which career is least affected by AI?
- How can I improve my match score?
- How will my career evolve over the next 5–10 years?

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Future-Workforce-Evolution-Engine.git
```

Move into the project directory

```bash
cd Future-Workforce-Evolution-Engine
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run src/app.py
```

---

# 📸 Sample Output

```text
=========================================
Future Workforce Evolution Engine
=========================================

User Skills

• Python
• SQL
• Git

Best Career

Data Engineer

Match Score

77.78%

Top Career Recommendations

1. Data Engineer
2. Data Analyst
3. Machine Learning Engineer

Missing Skills

• Apache Spark
• Airflow

Learning Roadmap

Week 1 : Apache Spark
Week 2 : Airflow
```

---

# 👨‍💻 Author

**Aditya Kumar**

B.Tech – Electronics & Communication Engineering

Birla Institute of Technology Mesra

GitHub: https://github.com/your-username

---

# ⭐ Project Status

Version **1.0** has been successfully completed.

The project currently includes a complete weighted skill-based recommendation engine with an interactive Streamlit dashboard.

Future releases will integrate Machine Learning, AI-powered workforce analytics, resume parsing, and predictive career intelligence.

If you found this project useful, consider giving it a ⭐ on GitHub.