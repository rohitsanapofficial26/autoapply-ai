from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    role = Column(String)
    status = Column(String)
    job_url = Column(String)
    cover_letter = Column(Text)
