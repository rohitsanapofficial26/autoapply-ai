from app.core.database import engine
from app.models.application import Application

def init_db():
    Application.metadata.create_all(bind=engine)
