import pandas as pd


def parse_recruiter_csv(file):
    df = pd.read_csv(file, dtype=str).fillna("")

    if df.empty:
        return {}

    row = df.iloc[0]

    return {
        "full_name": row.get("name") or row.get("full_name") or "",
        "email": row.get("email") or "",
        "phone": row.get("phone") or row.get("mobile") or "",
        "source": "recruiter_csv",
        "skills": []
    }