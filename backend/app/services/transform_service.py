from app.adapters.recruiter_csv import parse_recruiter_csv


def transform_candidate_data(
    csv_file=None,
    resume_file=None,
    github_url=None,
):
    candidate = {}

    if csv_file:
        candidate.update(parse_recruiter_csv(csv_file))

    if github_url:
        candidate["github_url"] = github_url

    # Resume processing comes later
    # GitHub API enrichment comes later

    return candidate