from pypdf import PdfReader
from docx import Document
from pathlib import Path
from app.normalizers.experience import extract_total_experience

SKILL_KEYWORDS = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "TypeScript",
    "React",
    "Next.js",
    "Node.js",
    "FastAPI",
    "Django",
    "Flask",
    "Docker",
    "Kubernetes",
    "AWS",
    "PostgreSQL",
    "MongoDB",
    "Redis",
    "Git",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
]


def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def extract_docx_text(file):
    doc = Document(file)

    return "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )


def extract_txt_text(file):
    return file.read().decode("utf-8")


def detect_skills(text):
    text_lower = text.lower()

    skills = []

    for skill in SKILL_KEYWORDS:
        if skill.lower() in text_lower:
            skills.append({
                "name": skill,
                "confidence": 0.85,
                "source": "resume"
            })

    return skills


def parse_resume(file, filename):
    extension = Path(filename).suffix.lower()

    if extension == ".pdf":
        text = extract_pdf_text(file)

    elif extension == ".docx":
        text = extract_docx_text(file)

    elif extension == ".txt":
        text = extract_txt_text(file)

    else:
        return {
            "resume_text": "",
            "skills": []
        }

    return {
    "resume_text": text[:1000],
    "skills": detect_skills(text),
    "total_experience_years":
        extract_total_experience(text)
}