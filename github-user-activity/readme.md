# 📊 GitHub User Activity Dashboard

A Python command-line tool that fetches and displays detailed public activity for any GitHub user using the GitHub REST API.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- 📈 **Real-time Activity Tracking** - Fetch the latest public events for any GitHub user
- 🔍 **Detailed Event Information** - View commit messages, PR titles, issue details, and more
- 📊 **Activity Summary** - Get a breakdown of activity by event type
- ⚙️ **Customizable Output** - Configure the number of events to display
- 🎨 **Clean Formatting** - Easy-to-read output with organized sections
- 🚀 **Multiple Event Types** - Supports PushEvents, Pull Requests, Issues, Forks, Stars, and more

## 📋 Table of Contents

- [Installation](#-installation)
- [Usage](#-usage)
- [Command-Line Arguments](#-command-line-arguments)
- [Examples](#-examples)
- [Event Types](#-event-types)
- [Understanding the Output](#-understanding-the-output)
- [API Information](#-api-information)
- [Troubleshooting](#-troubleshooting)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Steps

1. **Clone or download this repository**
```bash
cd /path/to/your/directory
```

2. **Install required dependencies**
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests
```

3. **Verify installation**
```bash
python main.py --help
```

## 💻 Usage

### Basic Syntax

```bash
python main.py --username <GITHUB_USERNAME> [--max <NUMBER>]
```

### Quick Start

Display recent activity for a user:
```bash
python main.py --username octocat
```

## 🎯 Command-Line Arguments

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `--username` | string | ✅ Yes | - | GitHub username to fetch activity for |
| `--max` | integer | ❌ No | 10 | Maximum number of events to display (1-100) |

### Argument Details

#### `--username`
- The GitHub username of the account you want to track
- Case-sensitive
- Must be a valid, existing GitHub user

#### `--max`
- Controls how many events are shown
- Useful for getting a quick overview (use lower numbers) or detailed history (use higher numbers)
- Maximum practical limit is around 100 events (API limitation)

## 📝 Examples

### Example 1: Basic Usage
```bash
python main.py --username torvalds
```
**Output:**
```
============================================================
Last 10 public events for torvalds
============================================================

• PushEvent in torvalds/linux
  Time: 2024-02-07T10:30:00Z
  Commits (3):
    - Fix memory leak in kernel module
    - Update documentation
    - Merge pull request #1234

• PullRequestEvent in torvalds/linux
  Time: 2024-02-06T15:20:00Z
  Action: closed
  PR: Add support for new hardware

...
```

### Example 2: Show More Events
```bash
python main.py --username octocat --max 25
```

### Example 3: Check Your Own Activity
```bash
python main.py --username SamiKhan43 --max 15
```

### Example 4: Quick Overview
```bash
python main.py --username github --max 5
```

## 🎭 Event Types

The tool tracks and displays the following GitHub event types:

### 1. **PushEvent** 🚀
- **What it is:** Code commits pushed to a repository
- **Details shown:** 
  - Number of commits
  - Commit messages (first line only)
- **Example:**
  ```
  • PushEvent in user/repo
    Commits (2):
      - Fix bug in login
      - Update dependencies
  ```

### 2. **PullRequestEvent** 🔄
- **What it is:** Pull request opened, closed, or merged
- **Details shown:**
  - Action (opened, closed, merged, etc.)
  - Pull request title
- **Example:**
  ```
  • PullRequestEvent in user/repo
    Action: opened
    PR: Add dark mode feature
  ```

### 3. **IssuesEvent** 🐛
- **What it is:** Issue created, closed, or updated
- **Details shown:**
  - Action (opened, closed, reopened, etc.)
  - Issue title
- **Example:**
  ```
  • IssuesEvent in user/repo
    Action: opened
    Issue: Bug in user authentication
  ```

### 4. **CreateEvent** ✨
- **What it is:** Branch, tag, or repository created
- **Details shown:**
  - Type of creation (branch, tag, repository)
  - Name of created item
- **Example:**
  ```
  • CreateEvent in user/repo
    Created: branch feature-login
  ```

### 5. **WatchEvent** ⭐
- **What it is:** User starred a repository
- **Details shown:** Simple confirmation message
- **Example:**
  ```
  • WatchEvent in user/repo
    Starred the repository
  ```

### 6. **ForkEvent** 🍴
- **What it is:** Repository forked
- **Details shown:** Where it was forked to
- **Example:**
  ```
  • ForkEvent in original/repo
    Forked to: user/repo
  ```

### 7. **Other Events**
The tool also tracks but provides basic info for:
- `DeleteEvent` - Branch or tag deletion
- `PublicEvent` - Repository made public
- `MemberEvent` - Collaborator added
- `ReleaseEvent` - Release published
- And more...

## 📊 Understanding the Output

### Output Structure

```
============================================================
Last X public events for USERNAME
============================================================

• EventType in repository/name
  Time: YYYY-MM-DDTHH:MM:SSZ
  [Event-specific details]

• EventType in repository/name
  Time: YYYY-MM-DDTHH:MM:SSZ
  [Event-specific details]

...

============================================================
Summary of activity:
============================================================
PushEvent: 5
PullRequestEvent: 3
IssuesEvent: 2
Other: 1
```

### Reading the Summary

The summary section provides a count of each event type:
- **PushEvent:** Number of code pushes
- **PullRequestEvent:** Number of PR activities
- **IssuesEvent:** Number of issue activities
- **Other:** All other event types combined

## 🌐 API Information

### GitHub REST API

This tool uses the **GitHub Events API** endpoint:
```
https://api.github.com/users/{username}/events/public
```

### Rate Limiting

**Unauthenticated Requests:**
- **Limit:** 60 requests per hour per IP address
- **Reset:** Every hour

**Authenticated Requests:**
- **Limit:** 5,000 requests per hour
- **How to authenticate:** Add a personal access token (see Advanced Usage below)

### Data Freshness

- Events are updated in real-time
- The API returns up to 300 of the most recent public events
- Events older than 90 days are not included

## 🔧 Troubleshooting

### Common Errors and Solutions

#### 1. **"Error: Could not fetch data for 'username'. Status code: 404"**
- **Cause:** Username doesn't exist or is typed incorrectly
- **Solution:** Double-check the username spelling

#### 2. **"Error: Could not fetch data for 'username'. Status code: 403"**
- **Cause:** API rate limit exceeded
- **Solution:** Wait one hour or use authentication (see below)

#### 3. **"No recent public activity found."**
- **Cause:** User has no public activity or hasn't made any recent events
- **Solution:** This is normal - try a different user or check the user's profile

#### 4. **"ModuleNotFoundError: No module named 'requests'"**
- **Cause:** The requests library isn't installed
- **Solution:** Run `pip install requests`

#### 5. **"python: can't open file 'main.py'"**
- **Cause:** You're not in the correct directory
- **Solution:** Navigate to the directory containing main.py:
  ```bash
  cd /path/to/github-user-activity/
  ```

### Advanced: Using Authentication (Optional)

To increase your rate limit, you can add a GitHub personal access token:

1. **Generate a token** at https://github.com/settings/tokens
2. **Modify the code** (add to line ~16):
```python
headers = {"Authorization": f"token YOUR_TOKEN_HERE"}
response = requests.get(API_URL, headers=headers)
```

## 📁 Project Structure

```
github-user-activity/
│
├── main.py              # Main application script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### File Descriptions

- **main.py:** Core application logic - fetches data, processes events, displays output
- **requirements.txt:** Lists all Python packages needed to run the application
- **README.md:** Comprehensive documentation and usage guide

## 🎓 Learning Resources

### What This Project Teaches

- ✅ Working with REST APIs
- ✅ Parsing JSON data
- ✅ Command-line argument handling
- ✅ Error handling and user feedback
- ✅ Data processing and formatting
- ✅ Python best practices

### Key Concepts

**API Payloads:**
In API responses, the "payload" is the actual data/content of an event. For example:
```json
{
  "type": "PushEvent",
  "payload": {              // ← This is the payload
    "commits": [...],
    "size": 2
  }
}
```

**Safe Dictionary Access:**
The code uses `.get()` to safely access dictionary values:
```python
event.get("payload", {}).get("commits", [])
```
This prevents errors if keys don't exist.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report bugs:** Open an issue describing the problem
2. **Suggest features:** Share ideas for improvements
3. **Submit pull requests:** Fix bugs or add features
4. **Improve documentation:** Help make this README better

### Development Setup

```bash
# Fork the repository
git clone https://github.com/yourusername/github-user-activity.git
cd github-user-activity

# Create a branch
git checkout -b feature/your-feature-name

# Make changes and test
python main.py --username octocat

# Commit and push
git add .
git commit -m "Add your feature"
git push origin feature/your-feature-name
```

## 📜 License

This project is open source and available under the MIT License.

## 🔗 Links

- **Project Roadmap:** https://roadmap.sh/projects/github-user-activity
- **GitHub API Documentation:** https://docs.github.com/en/rest
- **Python Requests Library:** https://requests.readthedocs.io/

## 👤 Author

Created as part of the [roadmap.sh](https://roadmap.sh) backend development projects.

## 🙏 Acknowledgments

- GitHub for providing the free public API
- The Python community for the excellent `requests` library
- roadmap.sh for the project inspiration

---

**Happy Coding! 🚀**

If you find this tool useful, please consider giving it a ⭐ on GitHub!