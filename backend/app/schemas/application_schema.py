from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str
    job_url: str
    cover_letter: str
