def build_provenance(
    candidate,
    csv_present=False,
    resume_present=False,
    github_present=False
):

    provenance = []

    # ---------- Full Name ----------

    if candidate.get("full_name"):

        field_sources = []

        if csv_present:
            field_sources.append("recruiter_csv")

        if github_present:
            field_sources.append("github")

        if resume_present:
            field_sources.append("resume")

        provenance.append({
            "field": "full_name",
            "source": field_sources,
            "method": "choose_first"
        })

    # ---------- Email ----------

    if candidate.get("email"):

        field_sources = []

        if csv_present:
            field_sources.append("recruiter_csv")

        if github_present:
            field_sources.append("github")

        provenance.append({
            "field": "email",
            "source": field_sources,
            "method": "choose_first"
        })

    # ---------- Phone ----------

    if candidate.get("phone"):

        provenance.append({
            "field": "phone",
            "source": ["recruiter_csv"],
            "method": "normalize_phone"
        })

    # ---------- Skills ----------

    if candidate.get("skills"):

        skill_sources = set()

        for skill in candidate["skills"]:

            skill_sources.update(
                skill.get("sources", [])
            )

        provenance.append({
            "field": "skills",
            "source": sorted(skill_sources),
            "method": "merge_skills"
        })

    # ---------- GitHub ----------

    if github_present:

        provenance.append({
            "field": "github",
            "source": ["github"],
            "method": "github_api_extraction"
        })

    # ---------- Resume ----------

    if resume_present:

        provenance.append({
            "field": "resume_text",
            "source": ["resume"],
            "method": "spacy_nlp_extraction"
        })

        if candidate.get("total_experience_years") is not None:

            provenance.append({
                "field": "total_experience_years",
                "source": ["resume"],
                "method": "experience_parser"
            })

    return provenance