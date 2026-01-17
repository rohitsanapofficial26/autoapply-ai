from openai import OpenAI
from app.core.config import OPENAI_API_KEY
from app.schemas.resume_schema import ResumeData
from app.schemas.job_schema import Job

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_cover_letter(resume: ResumeData, job: Job) -> str:
    prompt = f"""
You are a professional career assistant.

Write a concise, professional cover letter (max 200 words) for the following job.

Candidate Resume Summary:
{resume.summary}

Candidate Skills:
{", ".join(resume.skills)}

Job Title:
{job.title}

Company:
{job.company}

Job Description:
{job.description}

Guidelines:
- Tailor to the role
- Highlight relevant skills
- Confident but not arrogant
- No emojis
- End with a polite closing
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
