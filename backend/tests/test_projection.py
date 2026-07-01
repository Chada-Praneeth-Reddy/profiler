from app.services.projection_service import (
    apply_projection
)


def test_field_remapping():

    candidate = {
        "full_name": "John Doe",
        "skills": ["Python"]
    }

    config = {
        "fields": [
            {
                "path": "candidate_name",
                "from": "full_name",
                "type": "string"
            }
        ]
    }

    result = apply_projection(
        candidate,
        config
    )

    assert result["candidate_name"] == "John Doe"