import requests


GITHUB_API = "https://api.github.com"


def extract_username(github_url: str) -> str:
    """
    https://github.com/torvalds -> torvalds
    """
    return github_url.rstrip("/").split("/")[-1]


def fetch_user(username: str) -> dict:
    response = requests.get(f"{GITHUB_API}/users/{username}")

    if response.status_code != 200:
        return {}

    return response.json()


def fetch_repositories(username: str) -> list:
    response = requests.get(
        f"{GITHUB_API}/users/{username}/repos?per_page=100"
    )

    if response.status_code != 200:
        return []

    return response.json()


def aggregate_languages(repositories: list) -> list:
    """
    Collect unique languages from repositories.
    """
    languages = set()

    for repo in repositories:
        language = repo.get("language")

        if language:
            languages.add(language)

    return sorted(list(languages))


def build_skills(languages: list) -> list:
    skills = []

    for language in languages:
        skills.append(
            {
                "name": language,
                "confidence": 0.9,
                "source": "github",
            }
        )

    return skills


def parse_github_profile(github_url: str) -> dict:
    username = extract_username(github_url)

    user = fetch_user(username)
    repos = fetch_repositories(username)

    languages = aggregate_languages(repos)

    return {
        "github_url": github_url,
        "github_username": username,
        "github_name": user.get("name"),
        "github_bio": user.get("bio"),
        "github_followers": user.get("followers"),
        "github_public_repos": user.get("public_repos"),
        "skills": build_skills(languages),
    }