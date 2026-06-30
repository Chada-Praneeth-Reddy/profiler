import re


def normalize_phone(phone: str | None):
    if not phone:
        return None

    digits = re.sub(r"\D", "", phone)

    # Indian numbers
    if len(digits) == 10:
        digits = "91" + digits

    if not digits.startswith("+"):
        digits = "+" + digits

    return digits