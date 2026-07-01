def calculate_skill_confidence(sources):

    weights = {
        "recruiter_csv": 0.95,
        "resume": 0.90,
        "github": 0.85
    }

    total = 0

    for source in sources:
        total += weights.get(source, 0.5)

    confidence = min(total, 1.0)

    return round(confidence, 2)


def calculate_overall_confidence(candidate):

    skills = candidate.get("skills", [])

    if skills:

        total = sum(
            skill.get("confidence", 0.5)
            for skill in skills
        )

        return round(
            total / len(skills),
            2
        )

    score = 0.0
    count = 0

    if candidate.get("full_name"):
        score += 0.95
        count += 1

    if candidate.get("email"):
        score += 0.95
        count += 1

    if candidate.get("phone"):
        score += 0.90
        count += 1

    if candidate.get("github"):
        score += 0.85
        count += 1

    if candidate.get("resume_text"):
        score += 0.90
        count += 1

    if count == 0:
        return 0.0

    return round(score / count, 2)