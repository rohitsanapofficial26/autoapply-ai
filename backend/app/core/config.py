import os
from dotenv import load_dotenv

load_dotenv()  # 👈 THIS loads .env into environment

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
