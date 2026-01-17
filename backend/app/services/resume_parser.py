from pypdf import PdfReader
from openai import OpenAI
from app.core.config import OPENAI_API_KEY
from app.schemas.resume_schema import ResumeData
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def parse_resume_with_ai(resume_text: str) -> ResumeData:
    prompt = f"""
    You are an expert resume parser.

    Extract the following details from the resume text and return ONLY valid JSON:
    - name
    - email
    - phone
    - skills (list)
    - experience_years (number)
    - roles (list)
    - technologies (list)
    - summary (short professional summary)

    Resume Text:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content
    data = json.loads(content)

    return ResumeData(**data)
