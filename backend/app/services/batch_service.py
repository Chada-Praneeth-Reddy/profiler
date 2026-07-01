from app.normalizers.phone import normalize_phone
from app.services.provenance_service import build_provenance
from app.services.confidence_service import (
    calculate_overall_confidence
)


def process_batch_candidates(candidates):

    results = []

    for candidate in candidates:

        if candidate.get("phone"):

            candidate["phone"] = normalize_phone(
                candidate["phone"]
            )

        # Dynamic confidence calculation
        candidate["overall_confidence"] = (
            calculate_overall_confidence(candidate)
        )

        candidate["provenance"] = build_provenance(
            candidate,
            csv_present=True
        )

        results.append(candidate)

    return results