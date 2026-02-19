import os
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

def main():
    parser = argparse.ArgumentParser(description="GitHub User Activity Dashboard")

    parser.add_argument(
        "--username",
        type=str,
        required=True,
        help="GitHub username"
    )
    parser.add_argument(
        "--max",
        type=int,
        default=10,
        help="Max number of events to show"
    )
    
    args = parser.parse_args()

    API_URL = f"https://api.github.com/users/{args.username}/events/public"

    headers = {}
    if GITHUB_API_KEY:
        headers["Authorization"] = f"token {GITHUB_API_KEY}"

    try:
        response = requests.get(API_URL, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to GitHub API. {e}")
        exit(1)

    if response.status_code != 200:
        print(f"Error: Could not fetch data for '{args.username}'. Status code: {response.status_code}")
        if response.status_code == 404:
            print("User not found.")
        elif response.status_code == 403:
            print("API rate limit exceeded. Please try again later.")
        exit(1)

    events = response.json()
    if not events:
        print("No recent public activity found.")
        exit(0)

    summary = {"PushEvent": 0, "PullRequestEvent": 0, "IssuesEvent": 0, "Other": 0}

    print(f"\n{'='*60}")
    print(f"Last {args.max} public events for {args.username}")
    print(f"{'='*60}\n")

    for event in events[:args.max]:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        created_at = event["created_at"]

        if event_type in summary:
            summary[event_type] += 1
        else:
            summary["Other"] += 1

        print(f"• {event_type} in {repo_name}")
        print(f"  Time: {created_at}")

        if event_type == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            if commits:
                print(f"  Commits ({len(commits)}):")
                for commit in commits:
                    message = commit.get("message", "No message").split('\n')[0]
                    print(f"    - {message}")
            else:
                print("    No commits in this push")

        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action", "unknown")
            pr_title = event.get("payload", {}).get("pull_request", {}).get("title", "")
            print(f"  Action: {action}")
            if pr_title:
                print(f"  PR: {pr_title}")

        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "unknown")
            issue_title = event.get("payload", {}).get("issue", {}).get("title", "")
            print(f"  Action: {action}")
            if issue_title:
                print(f"  Issue: {issue_title}")

        elif event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type", "unknown")
            ref = event.get("payload", {}).get("ref", "")
            print(f"  Created: {ref_type} {ref}")

        elif event_type == "WatchEvent":
            print(f"  Starred the repository")

        elif event_type == "ForkEvent":
            forkee = event.get("payload", {}).get("forkee", {}).get("full_name", "")
            print(f"  Forked to: {forkee}")

        print()

    print(f"{'='*60}")
    print("Summary of activity:")
    print(f"{'='*60}")
    for k, v in summary.items():
        if v > 0:
            print(f"{k}: {v}")
    print()


if __name__ == "__main__":
    main()
