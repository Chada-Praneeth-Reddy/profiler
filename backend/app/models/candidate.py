from pydantic import BaseModel, Field
from typing import List, Optional


class Skill(BaseModel):
    name: str
    confidence: float
    source: str


class Candidate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    github_url: Optional[str] = None
    skills: List[Skill] = Field(default_factory=list)