from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import apply, dashboard

app = FastAPI(title="AutoApply AI")

# ✅ CORS (for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apply.router)
app.include_router(dashboard.router)

@app.get("/")
def root():
    return {"status": "running"}
