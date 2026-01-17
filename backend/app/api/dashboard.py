from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.application_db_service import list_applications
from app.core.database import SessionLocal

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/applications")
def get_applications(db: Session = Depends(get_db)):
    return list_applications(db)
