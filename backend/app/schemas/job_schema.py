from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    title: str
    company: str
    location: Optional[str]
    description: str
    source: str
    url: str
