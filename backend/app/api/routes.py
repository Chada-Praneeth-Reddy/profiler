from fastapi import APIRouter, UploadFile, File, Form
from app.adapters.recruiter_csv import parse_recruiter_csv
from typing import Optional
from app.services.transform_service import transform_candidate_data

router = APIRouter()

@router.post("/transform")

async def transform_candidate(
    csv_file: Optional[UploadFile] = File(None),
    resume_file: Optional[UploadFile] = File(None),
    github_url: Optional[str] = Form(None),
):

    result = transform_candidate_data(
        csv_file.file if csv_file else None,
        resume_file.file if resume_file else None,
        github_url,
    )

    return result