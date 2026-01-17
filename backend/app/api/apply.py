from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.application_schema import ApplicationCreate
from app.services.application_db_service import create_application
from app.core.database import SessionLocal

router = APIRouter(prefix="/apply", tags=["Apply"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/execute")
def apply_job(data: ApplicationCreate, db: Session = Depends(get_db)):
    create_application(db, data.dict())
    return {"status": "saved"}
