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

                merged[name]["confidence"] = max(
                    merged[name]["confidence"],
                    skill["confidence"]
                )

                if skill["source"] not in merged[name]["sources"]:
                    merged[name]["sources"].append(
                        skill["source"]
                    )

    return list(merged.values())