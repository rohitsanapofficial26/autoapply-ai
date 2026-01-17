from pydantic import BaseModel

class CoverLetterResponse(BaseModel):
    company: str
    role: str
    cover_letter: str
