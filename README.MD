# 🚀 Future Workforce Evolution Engine

> **An AI-inspired career intelligence system that analyzes user skills, compares them with industry role requirements, and recommends the most suitable career path using a weighted skill matching algorithm.**

![Status](https://img.shields.io/badge/Status-Version%201.0-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 Project Overview

Future Workforce Evolution Engine is a career recommendation system that evaluates a user's technical skills against multiple industry roles and recommends the best career based on a weighted skill matching algorithm.

Instead of simply matching keywords, the system assigns importance weights to skills required for each role and calculates a percentage match score, making recommendations more meaningful and realistic.

This project is being developed as a modular AI-inspired career intelligence platform with future plans for skill gap analysis, learning roadmap generation, workforce trend analysis, and machine learning integration.

---

# ✨ Current Features

✅ SQLite Database Integration

✅ Skills Database

✅ Roles Database

✅ Role-Skill Mapping

✅ User Skill to Skill-ID Conversion

✅ Weighted Skill Match Algorithm

✅ Career Recommendation Engine

✅ Modular Python Architecture

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| SQLite | Database |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Matplotlib | Visualization *(Upcoming)* |
| Streamlit | Interactive Dashboard *(Upcoming)* |

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
│   ├── load_skills.py
│   ├── load_roles.py
│   ├── load_skills_roles.py
│   ├── skill_match_engine.py
│   └── visualization.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🗄 Database Schema

The project currently uses four database tables.

| Table | Description |
|--------|-------------|
| employees | Employee dataset |
| skills | Stores all technical skills |
| roles | Stores available career roles |
| skills_roles | Maps skills to career roles with importance weights |

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
Weighted Skill Match Algorithm
      │
      ▼
Career Recommendation Engine
      │
      ▼
Best Career Recommendation
```

---

# 🧠 Recommendation Algorithm

The recommendation engine follows these steps:

1. Accept user skills.
2. Convert skill names into skill IDs.
3. Retrieve required skills for every career role.
4. Compare user skills with required skills.
5. Calculate a weighted match percentage.
6. Recommend the role with the highest score.

The weighted score is calculated as:

```
Match Score = (Matched Skill Weight / Total Required Skill Weight) × 100
```

---

# 📊 Current Progress

```text
Overall Progress

████████████░░░░░░░░ 60%

✅ Database Layer

✅ Data Loading Modules

✅ Weighted Skill Matching Engine

✅ Career Recommendation Engine

⏳ Skill Gap Analysis

⏳ Learning Roadmap

⏳ Streamlit Dashboard

⏳ Machine Learning Module
```

---

# 🚀 Version Roadmap

## ✅ Version 1.0 (Completed)

- SQLite Database
- Skills Management
- Roles Management
- Role-Skill Mapping
- Weighted Skill Match Algorithm
- Career Recommendation Engine

---

## 🚧 Version 1.1 (Planned)

- Top 3 Career Recommendations
- Skill Gap Analysis
- Missing Skills Detection
- Learning Roadmap Generator

---

## 🚀 Version 2.0 (Future)

- Interactive Streamlit Dashboard
- Machine Learning Recommendation System
- AI Workforce Trend Analysis
- Future Career Evolution Prediction
- Salary Growth Estimation
- Resume-Based Skill Analysis

---

# 🎯 End Goal

The final platform will answer questions like:

- Which career best matches my current skills?
- Which skills should I learn next?
- What are my missing skills?
- Which career has the highest future demand?
- Which career is least affected by AI automation?
- How can I improve my career match score?
- How will my career evolve over time?

---

# ▶️ How to Run

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

Run the recommendation engine

```bash
python src/skill_match_engine.py
```

---

# 📌 Sample Output

```text
==========================================
 Future Workforce Evolution Engine
==========================================

User Skills

- Python
- SQL
- Git

Career Recommendation

Best Role   : Data Engineer

Match Score : 77.78 %
```

---

# 👨‍💻 Author

**Aditya Kumar**

B.Tech – Electronics & Communication Engineering

Birla Institute of Technology Mesra

---

# ⭐ Project Status

This project is under active development.

Version **1.0** of the core recommendation engine has been completed successfully.

Future versions will introduce skill gap analysis, learning roadmap generation, Streamlit dashboards, and AI-powered career intelligence features.

If you found this project useful, consider giving it a ⭐ on GitHub.