from app.services.confidence_service import (
    calculate_skill_confidence
)


def merge_skills(*skill_lists):

    merged = {}

    for skills in skill_lists:

        if not skills:
            continue

        for skill in skills:

            name = skill["name"].strip().lower()

            if name not in merged:

                merged[name] = {
                    "name": skill["name"],
                    "confidence": skill["confidence"],
                    "sources": [skill["source"]]
                }

            else:

                if skill["source"] not in merged[name]["sources"]:

                    merged[name]["sources"].append(
                        skill["source"]
                    )

    # Dynamic confidence calculation
    for skill in merged.values():

        skill["confidence"] = (
            calculate_skill_confidence(
                skill["sources"]
            )
        )

    return list(merged.values())