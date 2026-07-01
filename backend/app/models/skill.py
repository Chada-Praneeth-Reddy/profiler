from pydantic import BaseModel
from typing import List


class Skill(BaseModel):
    name: str
    confidence: float
    sources: List[str]