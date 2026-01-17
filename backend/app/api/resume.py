from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/resume", tags=["Resume"])

@router.post("/parse")
async def parse_resume(file: UploadFile = File(...)):
    return {"message": "Resume endpoint working"}
