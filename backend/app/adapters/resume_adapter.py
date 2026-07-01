from pypdf import PdfReader
from docx import Document
from pathlib import Path
from app.normalizers.experience import extract_total_experience
from app.services.nlp_service import extract_skills_nlp



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
            "skills": [],
            "total_experience_years": 0
        }

    return {
    "resume_text": text[:1000],
    "skills": extract_skills_nlp(text),
    "total_experience_years":
        extract_total_experience(text)
}