from sqlalchemy.orm import Session
from app.models.application import Application

def create_application(db: Session, data):
    app = Application(**data)
    db.add(app)
    db.commit()
    db.refresh(app)
    return app

def list_applications(db: Session):
    return db.query(Application).all()
