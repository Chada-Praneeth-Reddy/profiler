# profiler

Profiler is a production-ready candidate data unification platform that transforms recruiter CSVs, resumes, and GitHub profiles into a canonical candidate schema.

## Features

### Multi-Source Ingestion
- Recruiter CSV uploads
- Resume parsing (PDF, DOCX, TXT)
- GitHub profile intelligence

### NLP & Normalization
- Skill extraction
- Phone normalization
- Date normalization
- Canonical field merging
- Experience estimation

### GitHub Intelligence
- Top languages
- Repository statistics
- Account age
- Activity score
- Estimated seniority
- Most starred repository
- Topics and technologies

### Confidence Engine
Dynamic confidence calculation based on:
- Number of sources
- Skill provenance
- Data completeness

### Provenance Tracking
Every transformed field includes:
- Original source(s)
- Transformation method used

### Projection Engine
Supports:
- Default projection
- Compact projection
- Recruiter projection
- Engineering projection
- Custom JSON projection configs

Example:

```json
{
  "fields": [
    {
      "path": "candidate_name",
      "from": "full_name",
      "type": "string"
    },
    {
      "path": "tech_stack",
      "from": "skills",
      "type": "array"
    }
  ],
  "include_confidence": true,
  "include_provenance": false,
  "on_missing": "null"
}
```

### Batch Processing
- Automatically detects multi-row CSV uploads.
- Processes entire candidate batches without changing endpoints.

---

# Architecture

```text
Frontend (React + Vite)
        |
        v
FastAPI API Layer
        |
        v
Transform Service
        |
        +------------------+
        |                  |
        v                  v
Resume Adapter      GitHub Adapter
        |                  |
        +------------------+
                |
                v
Normalization Layer
(phone, dates, skills)
                |
                v
Confidence Engine
                |
                v
Provenance Engine
                |
                v
Projection Engine
                |
                v
Final Candidate Schema
```

---

# Project Structure

```text
backend/

app/
├── adapters/
├── api/
├── config/
├── models/
├── normalizers/
├── services/
└── main.py

tests/
```

---

# Local Setup

## Backend

```bash
cd backend

python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```
