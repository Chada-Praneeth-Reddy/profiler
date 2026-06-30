from app.adapters.recruiter_csv import parse_recruiter_csv
from app.adapters.github_adapter import parse_github_profile


def transform_candidate_data(
    csv_file=None,
    resume_file=None,
    github_url=None,
):
    candidate = {}

    # CSV
    if csv_file:
        candidate.update(parse_recruiter_csv(csv_file))

    # GitHub
    if github_url:
        github_data = parse_github_profile(github_url)

        candidate["github"] = github_data["github"]

        existing_skills = candidate.get("skills", [])

        candidate["skills"] = (
              existing_skills +
              github_data["skills"]
                              )

    return candidate