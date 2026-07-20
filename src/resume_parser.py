import pdfplumber


def extract_text_from_resume(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.lower()

def detect_skills(resume_text, skills_df):

    detected_skills = []

    resume_text = resume_text.lower()

    for skill in skills_df["skill_name"]:

        if skill.lower() in resume_text:
            detected_skills.append(skill)

    return detected_skills

print("resume_parser loaded successfully")