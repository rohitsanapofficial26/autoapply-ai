from pydantic import BaseModel
from typing import List

class ResumeData(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]
    experience_years: float
    roles: List[str]
    technologies: List[str]
    summary: str
