from fastapi import APIRouter, Query
from app.services.job_services import fetch_jobs

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/search")
def search_jobs(
    keyword: str = Query(..., example="python"),
    limit: int = 10
):
    return fetch_jobs(keyword, limit)
