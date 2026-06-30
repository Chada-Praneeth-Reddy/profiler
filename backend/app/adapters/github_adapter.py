import requests
from datetime import datetime
from collections import Counter



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

def calculate_total_stars(repos):
    return sum(repo.get("stargazers_count", 0) for repo in repos)

def most_starred_repo(repos):
    if not repos:
        return None

    best = max(
        repos,
        key=lambda r: r.get("stargazers_count", 0)
    )

    return {
        "name": best.get("name"),
        "stars": best.get("stargazers_count", 0)
    }

def extract_topics(repos):
    counter = Counter()

    for repo in repos:
        topics = repo.get("topics", [])

        for topic in topics:
            counter[topic.lower()] += 1

    return [topic for topic, _ in counter.most_common(10)]

def account_age_years(created_at):
    if not created_at:
        return 0

    created = datetime.fromisoformat(
        created_at.replace("Z", "+00:00")
    )

    today = datetime.now(created.tzinfo)

    return round(
        (today - created).days / 365,
        1
    )

def compute_activity_score(user, repos):
    followers = user.get("followers", 0)
    repo_count = len(repos)
    stars = calculate_total_stars(repos)

    score = (
        min(followers / 1000, 40)
        + min(repo_count / 2, 30)
        + min(stars / 500, 30)
    )

    return round(score)

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

TOPIC_MAP = {
    "react": "React",
    "nextjs": "Next.js",
    "nodejs": "Node.js",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "postgres": "PostgreSQL",
    "aws": "AWS",
    "tensorflow": "TensorFlow",
    "machine-learning": "Machine Learning"
}


def build_skills(languages, topics):
    skills = []

    for language in languages:
        skills.append({
            "name": language,
            "confidence": 0.9,
            "source": "github"
        })

    for topic in topics:
        if topic in TOPIC_MAP:
            skills.append({
                "name": TOPIC_MAP[topic],
                "confidence": 0.85,
                "source": "github-topic"
            })

    return skills


def estimate_seniority(user, repos):
    years = account_age_years(
        user.get("created_at")
    )

    stars = calculate_total_stars(repos)

    if years >= 8 or stars >= 1000:
        return "Senior"

    if years >= 4:
        return "Mid-Level"

    return "Junior"

def parse_github_profile(github_url):
    username = extract_username(github_url)

    user = fetch_user(username)
    repos = fetch_repositories(username)

    languages = aggregate_languages(repos)
    topics = extract_topics(repos)

    return {
        "github": {
            "username": username,
            "name": user.get("name"),
            "bio": user.get("bio"),
            "company": user.get("company"),
            "location": user.get("location"),

            "followers": user.get("followers"),
            "following": user.get("following"),
            "public_repos": user.get("public_repos"),

            "account_age_years":
                account_age_years(
                    user.get("created_at")
                ),

            "total_stars":
                calculate_total_stars(repos),

            "most_starred_repo":
                most_starred_repo(repos),

            "top_languages":
                languages,

            "top_topics":
                topics,

            "activity_score":
                compute_activity_score(
                    user,
                    repos
                ),

            "estimated_seniority":
                estimate_seniority(
                    user,
                    repos
                )
        },

        "skills":
            build_skills(
                languages,
                topics
            )
    }