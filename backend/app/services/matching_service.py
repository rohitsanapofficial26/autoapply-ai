from openai import OpenAI
from app.core.config import OPENAI_API_KEY
from app.schemas.match_schema import JobMatchResult
from app.schemas.job_schema import Job
from app.schemas.resume_schema import ResumeData
import math

client = OpenAI(api_key=OPENAI_API_KEY)

def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    return dot / (norm1 * norm2)

def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def match_resume_to_jobs(resume: ResumeData, jobs: list[Job]):
    resume_text = (
        resume.summary + " " +
        " ".join(resume.skills) + " " +
        " ".join(resume.technologies)
    )

    resume_embedding = get_embedding(resume_text)
    results = []

    for job in jobs:
        job_text = job.title + " " + job.description
        job_embedding = get_embedding(job_text)

        score = cosine_similarity(resume_embedding, job_embedding)
        match_percentage = round(score * 100, 2)

        missing_skills = [
            skill for skill in job_text.lower().split()
            if skill not in " ".join(resume.skills).lower()
        ][:5]

        results.append(
            JobMatchResult(
                title=job.title,
                company=job.company,
                match_score=match_percentage,
                missing_skills=missing_skills,
                url=job.url
            )
        )

    return sorted(results, key=lambda x: x.match_score, reverse=True)
