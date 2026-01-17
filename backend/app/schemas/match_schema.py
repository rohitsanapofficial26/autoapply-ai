from pydantic import BaseModel
from typing import List

class JobMatchResult(BaseModel):
    title: str
    company: str
    match_score: float
    missing_skills: List[str]
    url: str
