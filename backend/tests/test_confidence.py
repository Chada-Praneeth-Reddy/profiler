from app.services.confidence_service import (
    calculate_skill_confidence,
    calculate_overall_confidence
)


def test_single_source_skill():

    confidence = calculate_skill_confidence(
        ["github"]
    )

    assert confidence == 0.85


def test_multiple_sources_skill():

    confidence = calculate_skill_confidence(
        ["github", "resume"]
    )

    assert confidence == 1.0


def test_overall_confidence():

    candidate = {
        "full_name": "John",
        "email": "john@gmail.com",
        "phone": "+919999999999"
    }

    score = calculate_overall_confidence(
        candidate
    )

    assert score > 0.8