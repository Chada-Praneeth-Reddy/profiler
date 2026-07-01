import re
from datetime import datetime


def extract_total_experience(text):

    pattern = r"(20\d{2})\s*-\s*(Present|20\d{2})"

    matches = re.findall(pattern, text)

    current_year = datetime.now().year

    total = 0

    for start, end in matches:

        start = int(start)

        if end == "Present":
            end = current_year
        else:
            end = int(end)

        total += max(0, end - start)

    return total