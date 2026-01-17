import requests
from app.schemas.job_schema import Job

REMOTIVE_API = "https://remotive.com/api/remote-jobs"

def fetch_jobs(keyword: str, limit: int = 10):
    response = requests.get(REMOTIVE_API, params={"search": keyword})
    data = response.json()

    jobs = []
    for item in data.get("jobs", [])[:limit]:
        jobs.append(
            Job(
                title=item["title"],
                company=item["company_name"],
                location=item.get("candidate_required_location"),
                description=item["description"],
                source="Remotive",
                url=item["url"]
            )
        )
    return jobs
