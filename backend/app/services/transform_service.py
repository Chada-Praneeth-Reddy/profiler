from app.adapters.recruiter_csv import parse_recruiter_csv
from app.adapters.github_adapter import parse_github_profile
from app.adapters.resume_adapter import parse_resume
from app.normalizers.skills import merge_skills
from app.normalizers.candidate_merge import choose_first

def transform_candidate_data(
    csv_file=None,
    resume_file=None,
    github_url=None,
):
    candidate = {}

    csv_data = {}
    github_data = {}
    resume_data = {}

    csv_skills = []
    github_skills = []
    resume_skills = []

    if csv_file:
        csv_data = parse_recruiter_csv(csv_file.file)

        csv_skills = csv_data.get("skills", [])


    if github_url:
        github_data = parse_github_profile(github_url)
        
        candidate["github"] = github_data["github"]
        
        github_skills = github_data.get("skills", [])

    if resume_file:
        resume_data = parse_resume(
            resume_file.file,
            resume_file.filename
        )

        candidate["resume_text"] = resume_data["resume_text"]
        candidate["total_experience_years"] = \
                         resume_data["total_experience_years"]
        resume_skills = resume_data.get("skills", [])
    
    candidate["skills"] = merge_skills(
    csv_skills,
    github_skills,
    resume_skills
     )

    candidate["full_name"] = choose_first(
    csv_data.get("full_name"),
    resume_data.get("full_name"),
    github_data.get("github", {}).get("name")
     )

    candidate["email"] = choose_first(
    csv_data.get("email"),
    resume_data.get("email")
     )

    candidate["phone"] = choose_first(
    csv_data.get("phone"),
    resume_data.get("phone")
     )


    return candidate