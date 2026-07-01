from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional

from app.services.transform_service import transform_candidate_data
from app.services.projection_service import (
    apply_projection,
    load_builtin_projection,
    load_uploaded_projection
)

from app.adapters.recruiter_csv import (
    parse_recruiter_csv_batch
)

from app.services.batch_service import (
    process_batch_candidates
)

import pandas as pd

router = APIRouter()


@router.post("/transform")
async def transform_candidate(
    csv_file: Optional[UploadFile] = File(None),
    resume_file: Optional[UploadFile] = File(None),
    projection_file: Optional[UploadFile] = File(None),

    github_url: Optional[str] = Form(None),
    projection: str = Form("default")
):

    # -------- AUTO BATCH DETECTION --------

    if csv_file:

        df = pd.read_csv(csv_file.file, dtype=str)

        csv_file.file.seek(0)

        if len(df) > 1:

            candidates = parse_recruiter_csv_batch(
                csv_file.file
            )

            transformed = process_batch_candidates(
                candidates
            )

            return {
                "mode": "batch",
                "count": len(transformed),
                "candidates": transformed
            }

        csv_file.file.seek(0)

    # -------- SINGLE CANDIDATE --------

    candidate = transform_candidate_data(
        csv_file,
        resume_file,
        github_url
    )

    if projection == "custom" and projection_file:

        config = load_uploaded_projection(
            projection_file
        )

    else:

        config = load_builtin_projection(
            projection
        )

    return apply_projection(
        candidate,
        config
    )


@router.post("/transform/batch")
async def transform_batch(
    csv_file: UploadFile = File(...)
):

    candidates = parse_recruiter_csv_batch(
        csv_file.file
    )

    transformed = process_batch_candidates(
        candidates
    )

    return {
        "mode": "batch",
        "count": len(transformed),
        "candidates": transformed
    }