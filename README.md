# Profiler - AI-Powered Candidate Data Transformation Engine

> Transform candidate information from resumes, recruiter exports, and GitHub profiles into a unified, confidence-aware, and explainable candidate profile.

🌐 **Live Demo:** https://profiler-chada2.vercel.app/

---

## Table of Contents

* [Features](#features)
* [Multi-Source Candidate Ingestion](#multi-source-candidate-ingestion)
* [Canonical Data Transformation](#canonical-data-transformation)
* [Conflict Resolution & Confidence Scoring](#conflict-resolution--confidence-scoring)
* [Runtime Schema Projection](#runtime-schema-projection)
* [GitHub Intelligence Layer](#github-intelligence-layer)
* [System Architecture Overview](#system-architecture-overview)
* [High-Level Architecture](#high-level-architecture)
* [Data Processing Pipeline](#data-processing-pipeline)
* [Design Decisions & Reasoning](#design-decisions--reasoning)
* [Edge Cases & Robustness](#edge-cases--robustness)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
* [API Endpoints](#api-endpoints)
* [Canonical Output Schema](#canonical-output-schema)
* [Future Improvements](#future-improvements)
* [License](#license)
* [Contact](#contact)

---

# Features

## Multi-Source Candidate Ingestion

Profiler consolidates candidate information from multiple heterogeneous sources:

* Recruiter CSV exports
* Resume files (PDF/DOCX)
* Public GitHub profiles

The platform automatically extracts, normalizes, and merges data into a unified representation.

---

## Canonical Data Transformation

All incoming data is standardized into canonical formats:

* Phone numbers → E.164 international format
* Dates → ISO-8601 format
* Skills → Canonical normalized taxonomy
* Experience → Unified numeric representation
* Resume text → Cleaned and normalized content

This ensures compatibility with ATS systems and downstream workflows.

---

## Conflict Resolution & Confidence Scoring

Profiler resolves conflicting information using deterministic priority rules:

| Priority | Source         |
| -------- | -------------- |
| 1        | Recruiter CSV  |
| 2        | Resume         |
| 3        | GitHub Profile |

Collection-based fields such as skills use union-based merging.

Every field includes:

* Confidence scores
* Source attribution
* Resolution methodology
* Provenance metadata

Example:

```json
{
  "name": "Python",
  "confidence": 0.95,
  "sources": [
    "resume",
    "github"
  ]
}
```

---

## Runtime Schema Projection

Recruiters can customize output schemas without modifying backend code.

Supported capabilities include:

### Field Selection

```json
{
  "path": "full_name"
}
```

### Field Remapping

```json
{
  "path": "candidate_name",
  "from": "full_name"
}
```

### Type Validation

```json
{
  "type": "string"
}
```

Supported types:

* string
* number
* array
* object

### Missing Value Policies

* null
* omit
* error

---

## GitHub Intelligence Layer

Beyond simple profile extraction, Profiler derives recruiter-focused insights:

* Account age
* Total stars earned
* Most starred repository
* Top programming languages
* Repository topics
* Activity score
* Estimated seniority level
* Open-source contribution metrics

This transforms developer activity into actionable hiring intelligence.

---

# System Architecture Overview

Profiler follows a layered transformation architecture:

```text
User Upload
      ↓
Input Adapters
(CSV / Resume / GitHub)
      ↓
Extraction Layer
      ↓
Normalization Engine
      ↓
Conflict Resolution Engine
      ↓
Canonical Candidate Model
      ↓
Projection Layer
      ↓
Custom Recruiter Output
```

---

# High-Level Architecture

```text
Frontend (React + Vite)
        ↓
FastAPI Backend
        ↓
────────────────────────
Input Processing Layer
────────────────────────
    ↓       ↓       ↓
 CSV     Resume   GitHub API
Adapter  Parser    Adapter
    ↓       ↓       ↓

Normalization Engine
        ↓

Merge & Conflict Resolver
        ↓

Confidence Calculator
        ↓

Provenance Tracker
        ↓

Projection Engine
        ↓

Final Candidate Profile
```

---

# Data Processing Pipeline

```text
Recruiter CSV
       ↓
Resume Upload
       ↓
GitHub Username
       ↓

Extraction Stage
       ↓

Field Normalization
       ↓

Conflict Resolution
       ↓

Confidence Assignment
       ↓

Canonical Profile Creation
       ↓

Runtime Projection Rules
       ↓

Custom JSON Output
```

---

# Design Decisions & Reasoning

### Canonical Layer Separation

Transformation logic remains completely independent from output representation.

Benefits:

* Easier maintenance
* Runtime customization
* Future source integrations
* Improved testability

---

### Deterministic Conflict Resolution

Instead of probabilistic matching, the system prioritizes:

```text
Recruiter CSV
   >
Resume
   >
GitHub
```

This guarantees reproducibility and explainability.

---

### Confidence-Driven Candidate Profiles

Confidence scores are dynamically computed using:

* Source reliability
* Field completeness
* Multi-source agreement
* Data consistency

Conceptually:

```python
overall_confidence = weighted(
    source_count,
    completeness,
    agreement
)
```

---

### Independent Source Processing

Failures in individual sources do not affect the entire transformation pipeline.

Examples:

* Missing GitHub profiles
* Corrupted resumes
* Invalid CSV rows

The system continues execution gracefully.

---

# Edge Cases & Robustness

## Missing Sources

**Input:**

```text
GitHub only
```

**Behavior:**

* Missing fields become `null`
* Processing continues normally

---

## Conflicting Candidate Information

**Input:**

Different emails across multiple sources.

**Resolution:**

Deterministic source prioritization resolves conflicts consistently.

---

## Large Recruiter Batches

The system processes candidates independently.

Benefits:

* Partial failures do not stop execution
* Improved scalability
* Better fault tolerance

---

## Invalid Projection Configurations

Example:

```json
{
  "type": "number",
  "path": "full_name"
}
```

Explicit validation errors are raised instead of producing inconsistent outputs.

---

# Tech Stack

| Layer           | Technology                          |
| --------------- | ----------------------------------- |
| Frontend        | React (Vite), TailwindCSS           |
| Backend         | FastAPI                             |
| Language        | Python                              |
| NLP             | spaCy                               |
| Data Processing | Pandas                              |
| Resume Parsing  | PyPDF2, python-docx                 |
| External APIs   | GitHub REST API                     |
| Deployment      | Render (Backend), Vercel (Frontend) |
| Version Control | Git & GitHub                        |

---

# Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/Chada-Praneeth-Reddy/profiler.git

cd profiler
```

---

## 2. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install Frontend Dependencies

```bash
cd frontend

npm install
```

---

## 4. Environment Variables

Create:

```bash
backend/.env
```

Add:

```env
GITHUB_TOKEN=your_github_token
```

Frontend:

```env
VITE_API_BASE_URL=http://localhost:8000
```

---

## 5. Run Backend

```bash
uvicorn app.main:app --reload
```

---

## 6. Run Frontend

```bash
npm run dev
```

---

## 7. Open Browser

```text
Frontend:
http://localhost:5173

Backend API Docs:
http://localhost:8000/docs
```

---

# API Endpoints

## Transform Candidate Data

```http
POST /api/transform
```

Uploads:

* Recruiter CSV
* Resume file
* GitHub username

Returns:

* Canonical candidate profile

---

## Runtime Projection

```http
POST /api/project
```

Example request:

```json
{
  "fields": [
    {
      "path": "candidate_name",
      "from": "full_name"
    }
  ],
  "include_confidence": true,
  "include_provenance": false,
  "on_missing": "null"
}
```

---

# Canonical Output Schema

```json
{
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+919876543210",
  "skills": [
    {
      "name": "Python",
      "confidence": 0.95,
      "sources": [
        "resume",
        "github"
      ]
    }
  ],
  "total_experience_years": 3.5,
  "github": {
    "username": "johndoe",
    "activity_score": 91,
    "estimated_seniority": "Mid-Level"
  },
  "overall_confidence": 0.92,
  "provenance": []
}
```

---

# Future Improvements

The following enhancements were intentionally deferred due to time constraints:

* LinkedIn adapter integration
* Probabilistic conflict resolution
* Explainable confidence visualization
* Graph-based provenance tracking
* Asynchronous batch processing
* Persistent candidate storage
* Vector-based candidate similarity search

---

# Why Profiler Is Unique

✅ GitHub activity becomes recruiter intelligence rather than raw metadata.

✅ Recruiters can define custom output schemas without changing backend code.

✅ Every field includes confidence scores and provenance information.

✅ Independent source processing eliminates single points of failure.

✅ Canonical transformation remains completely separated from presentation logic.

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# Contact

### Chada Praneeth Reddy

📧 Email: [chadapraneethreddy0@gmail.com](mailto:chadapraneethreddy0@gmail.com)

🐙 GitHub: https://github.com/Chada-Praneeth-Reddy

💼 LinkedIn: https://www.linkedin.com/in/chada-praneeth-b1144a2b6/
