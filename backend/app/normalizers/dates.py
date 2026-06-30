from datetime import datetime


FORMATS = [
    "%d/%m/%Y",
    "%Y-%m-%d",
    "%d-%m-%Y",
    "%b %Y",
    "%B %Y"
]


def normalize_date(date_str):
    if not date_str:
        return None

    for fmt in FORMATS:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.isoformat()
        except ValueError:
            continue

    return date_str