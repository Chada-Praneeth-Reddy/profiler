import json
from app.normalizers.field_normalizers import (
    apply_field_normalization
)

def load_builtin_projection(name):

    with open("app/config/projection.json") as f:
        configs = json.load(f)

    return configs.get(name, configs["default"])


def load_uploaded_projection(file):

    return json.load(file.file)


def validate_type(value, expected_type):

    if value is None:
        return True

    mapping = {
        "string": str,
        "number": (int, float),
        "array": list,
        "object": dict,
    }

    return isinstance(
        value,
        mapping.get(expected_type, object)
    )


def apply_projection(candidate, config):

    result = {}

    fields = config.get("fields", [])

    on_missing = config.get(
        "on_missing",
        "null"
    )

    include_confidence = config.get(
        "include_confidence",
        False
    )

    include_provenance = config.get(
        "include_provenance",
        False
    )

    for field in fields:

        output_name = field["path"]

        source_name = field.get(
            "from",
            output_name
        )

        value = candidate.get(source_name)

        normalization_rule = field.get("normalize")

        if normalization_rule:

           value = apply_field_normalization(
        value,
        normalization_rule
         )

        print(f"{source_name} -> {output_name} = {value}")

        # Missing values
        if value is None:

            if field.get("required", False):
                result[output_name] = None

            if on_missing == "omit":
                continue

            if on_missing == "error":
                raise ValueError(
                    f"Missing field: {source_name}"
                )

            result[output_name] = None
            continue

        # Type validation
        expected_type = field.get("type")

        if expected_type:

            if not validate_type(
                value,
                expected_type
            ):
                raise ValueError(
                    f"{output_name} expected {expected_type}"
                )

        result[output_name] = value

    if include_confidence:

        result["overall_confidence"] = candidate.get(
            "overall_confidence",
            0.9
        )

    if include_provenance:

        result["provenance"] = candidate.get(
            "provenance",
            []
        )

    print("\n=== RESULT ===")
    print(result)

    return result