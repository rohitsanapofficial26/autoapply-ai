from fastapi import APIRouter
from app.schemas.resume_schema import ResumeData
from app.services.job_services import fetch_jobs
from app.services.matching_service import match_resume_to_jobs

router = APIRouter(prefix="/match", tags=["Matching"])

@router.post("/jobs")
def match_jobs(resume: ResumeData, keyword: str):
    jobs = fetch_jobs(keyword=keyword, limit=10)
    return match_resume_to_jobs(resume, jobs)
