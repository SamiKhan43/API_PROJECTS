import requests
import argparse
from datetime import datetime, timedelta, timezone

BASE_URL = "https://api.github.com/search/repositories"

def fetch_trending_repos(language, duration, limit):

    today = datetime.now(timezone.utc)
    if duration == "daily":
        since_date = today - timedelta(days=1)

    elif duration == "weekly":
        since_date = today - timedelta(days=7)

    else:  
        since_date = today - timedelta(days=30)
    
    date_str = since_date.strftime("%Y-%m-%d")
    language_query = f"+language:{language}" if language else ""
    query = f"created:>{date_str}{language_query}"
    
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }
    
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "GitHub-Trending-CLI"
    }
    
    try:
        response = requests.get(BASE_URL, params=params, headers=headers)
        response.raise_for_status()
        return response.json().get('items', [])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def display_repos(repos, duration, language, limit):
    if not repos:
        print("No repositories found or API error.")
        return
    
    lang_name = language.upper() if language else "ALL LANGUAGES"
    category_name = f"{duration.upper()} TRENDING - {lang_name}"
    
    print(f"\n╔{'═'*68}╗")
    print(f"║ {category_name}{' '*(67-len(category_name))}║")
    print(f"╚{'═'*68}╝\n")
    
    for i, repo in enumerate(repos[:limit], 1):
        name = repo.get("full_name", "N/A")
        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)
        language = repo.get("language", "N/A")
        description = repo.get("description") or "No description"  
        url = repo.get("html_url", "")
        
        if len(description) > 60:
            description = description[:60] + "..."
        
        print(f"┌─ Repository #{i} {'─'*53}")
        print(f"│ Name       : {name}")
        print(f"│ Language   : {language}")
        print(f"│ Stars      : ⭐ {stars:,} | Forks: {forks:,}")
        print(f"│ Description: {description}")
        print(f"│ URL        : {url}")
        print(f"└{'─'*68}\n")

def main():
    parser = argparse.ArgumentParser(description="GitHub Trending CLI Tool")
    
    parser.add_argument(
        "--duration",
        type=str,
        default="daily",
        choices=["daily", "weekly", "monthly"],
        help="Time range for trending repos"
    )
    
    parser.add_argument(
        "--lang",
        type=str,
        default="",
        help="Programming language to filter (e.g., python, javascript)"
    )
    
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of repositories to display (default: 5)"
    )
    
    args = parser.parse_args()
    
    print("\n Fetching data from GitHub...", end=" ", flush=True)
    repo_data = fetch_trending_repos(args.lang, args.duration, args.count)
    print("Done! ✓")
    
    display_repos(repo_data, args.duration, args.lang, args.count)

if __name__ == "__main__":
    main()