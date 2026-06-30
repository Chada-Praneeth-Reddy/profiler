import re
from datetime import datetime


def extract_total_experience(text):
    pattern = r"(20\d{2})\s*-\s*(Present|20\d{2})"

    matches = re.findall(pattern, text)

    total_years = 0

    current_year = datetime.now().year

    for start, end in matches:

        start = int(start)

        if end == "Present":
            end = current_year
        else:
            end = int(end)

        total_years += max(0, end - start)

    return total_years