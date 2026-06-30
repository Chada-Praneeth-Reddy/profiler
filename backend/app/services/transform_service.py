from app.adapters.recruiter_csv import parse_recruiter_csv
from app.adapters.github_adapter import parse_github_profile
from app.adapters.resume_adapter import parse_resume

def transform_candidate_data(
    csv_file=None,
    resume_file=None,
    github_url=None,
):
    candidate = {}

    if csv_file:
        candidate.update(
            parse_recruiter_csv(csv_file.file)
        )

    if github_url:
        github_data = parse_github_profile(github_url)

        candidate["github"] = github_data["github"]

        candidate["skills"] = (
            candidate.get("skills", [])
            + github_data["skills"]
        )

    if resume_file:
        resume_data = parse_resume(
            resume_file.file,
            resume_file.filename
        )

        candidate["resume_text"] = (
            resume_data["resume_text"]
        )

        candidate["skills"] = (
            candidate.get("skills", [])
            + resume_data["skills"]
        )

    return candidate