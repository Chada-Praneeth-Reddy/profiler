from app.normalizers.phone import normalize_phone
from app.normalizers.dates import normalize_date


def apply_field_normalization(value, rule):

    if value is None:
        return None

    if rule == "phone_e164":
        return normalize_phone(value)

    if rule == "date_iso":
        return normalize_date(value)

    if rule == "skills_flat":

        if isinstance(value, list):

            return [
                skill["name"]
                for skill in value
                if isinstance(skill, dict)
            ]

    return value