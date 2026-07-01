from app.normalizers.phone import normalize_phone


def test_indian_phone():

    assert normalize_phone(
        "9876543210"
    ) == "+919876543210"


def test_existing_country_code():

    assert normalize_phone(
        "+919876543210"
    ) == "+919876543210"