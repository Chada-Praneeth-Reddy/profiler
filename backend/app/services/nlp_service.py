import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load("en_core_web_sm")

SKILL_VOCAB = [
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
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Computer Vision",
    "LangChain",
    "OpenAI",
    "Linux"
]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

patterns = [nlp.make_doc(skill) for skill in SKILL_VOCAB]

matcher.add("SKILLS", patterns)


def extract_skills_nlp(text: str):
    doc = nlp(text)

    matches = matcher(doc)

    found = set()

    for _, start, end in matches:
        found.add(doc[start:end].text)

    return [
        {
            "name": skill,
            "confidence": 0.90,
            "source": "resume"
        }
        for skill in sorted(found)
    ]

def extract_entities(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities