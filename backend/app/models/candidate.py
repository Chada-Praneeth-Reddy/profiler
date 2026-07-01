from typing import Optional, List, Dict, Any

from pydantic import BaseModel

from app.models.skill import Skill


class CandidateProfile(BaseModel):

    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    skills: List[Skill] = []

    github: Optional[Dict[str, Any]] = None

    total_experience_years: Optional[int] = None

    resume_text: Optional[str] = None