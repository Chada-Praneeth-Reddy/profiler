import pandas as pd
from app.normalizers.phone import normalize_phone

def parse_recruiter_csv(file):
    df = pd.read_csv(file, dtype=str).fillna("")

    if df.empty:
        return {}

    row = df.iloc[0]

    return {
        "full_name": row.get("name") or row.get("full_name") or "" or row.get("first_name") or row.get("last_name") or row.get("first_name") + " " + row.get("last_name"),
        "email": row.get("email") or "",
        "phone": normalize_phone(
        row.get("phone") or row.get("mobile") or row.get("contact") or "" ),
        "source": "recruiter_csv",
        "skills": []
    }