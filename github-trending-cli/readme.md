# 🔥 GitHub Trending CLI

A beautiful command-line tool to fetch and display trending GitHub repositories using the official GitHub API.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![roadmap.sh](https://img.shields.io/badge/roadmap.sh-project-purple.svg)](https://roadmap.sh/projects/github-trending-cli)

> **📚 Project from [roadmap.sh](https://roadmap.sh/projects/github-trending-cli)**  
> This project is part of the roadmap.sh backend projects collection, designed to help developers practice building CLI applications, integrating third-party APIs, handling errors, and working with configurations.

## ✨ Features

- 📊 View trending repositories by time period (daily, weekly, monthly)
- 🔍 Filter by programming language
- 🎨 Beautiful formatted output with Unicode box-drawing
- ⚡ Fast and lightweight
- 🚀 Uses official GitHub API (no authentication required)
- 📈 Shows stars, forks, and descriptions

## 🎯 Project Requirements

This project implements the following requirements from [roadmap.sh](https://roadmap.sh/projects/github-trending-cli):

- ✅ **CLI Application** - Command-line interface for interacting with GitHub API
- ✅ **GitHub REST API Integration** - Fetches trending repository data
- ✅ **No Authentication Required** - Works with public repositories
- ✅ **Time Range Filtering** - Support for daily, weekly, and monthly trends
- ✅ **Error Handling** - Robust error handling for API requests and invalid input
- ✅ **JSON Parsing** - Parses and processes GitHub API responses
- ✅ **Sorting** - Repositories sorted by star count
- ✅ **Formatted Output** - Clear display of repository name, description, stars, forks, and language
- ✅ **Command-Line Arguments** - `--duration`, `--lang`, `--count` options
- ✅ **Documentation** - Comprehensive README with installation and usage instructions

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/github-trending-cli.git
   cd github-trending-cli
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

Create a `requirements.txt` file with:
```
requests>=2.31.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```bash
python main.py
```

This will show the top 5 daily trending repositories across all languages.

### With Options

```bash
# Show weekly trending Python repositories
python main.py --duration weekly --lang python

# Show top 10 daily trending JavaScript repositories
python main.py --duration daily --lang javascript --count 10

# Show monthly trending repositories (all languages)
python main.py --duration monthly --count 20
```

## 🎯 Command-Line Arguments

| Argument | Short | Type | Default | Description |
|----------|-------|------|---------|-------------|
| `--duration` | `-d` | string | `daily` | Time range: `daily`, `weekly`, `monthly` |
| `--lang` | `-l` | string | `""` (all) | Programming language filter |
| `--count` | `-c` | integer | `5` | Number of repositories to display |
| `--help` | `-h` | - | - | Show help message |

## 📊 Examples

### Example 1: Daily Python Trending
```bash
python main.py --duration daily --lang python --count 5
```

**Output:**
```
🔍 Fetching data from GitHub... Done! ✓

╔════════════════════════════════════════════════════════════════════╗
║ DAILY TRENDING - PYTHON                                            ║
╚════════════════════════════════════════════════════════════════════╝

┌─ Repository #1 ─────────────────────────────────────────────────────
│ Name       : openai/whisper
│ Language   : Python
│ Stars      : ⭐ 45,234 | Forks: 🔱 5,678
│ Description: Robust Speech Recognition via Large-Scale Weak Supe...
│ URL        : https://github.com/openai/whisper
└────────────────────────────────────────────────────────────────────
```

### Example 2: Weekly JavaScript Trending
```bash
python main.py --duration weekly --lang javascript --count 3
```

### Example 3: All Languages Monthly
```bash
python main.py --duration monthly --count 10
```

## 🎨 Supported Languages

You can filter by any programming language GitHub recognizes:

- `python`
- `javascript`
- `typescript`
- `java`
- `go`
- `rust`
- `cpp` (C++)
- `c`
- `ruby`
- `php`
- `swift`
- `kotlin`
- `csharp` (C#)
- And many more!

**Tip:** Language names are case-insensitive.

## 🔧 How It Works

1. **Date Calculation:** Calculates the start date based on duration (1, 7, or 30 days ago)
2. **Query Building:** Constructs a GitHub API search query: `created:>DATE+language:LANG`
3. **API Request:** Sends request to `https://api.github.com/search/repositories`
4. **Response Parsing:** Extracts repository data from JSON response
5. **Display:** Formats and displays results with beautiful Unicode boxes

## 📡 API Information

- **Endpoint:** `https://api.github.com/search/repositories`
- **Rate Limit:** 60 requests per hour (unauthenticated)
- **Authentication:** Not required (but recommended for higher limits)

### Adding GitHub Token (Optional)

To increase rate limits to 5,000/hour:

1. Create a personal access token: https://github.com/settings/tokens
2. Modify the headers in `main.py`:
   ```python
   headers = {
       "Accept": "application/vnd.github+json",
       "User-Agent": "GitHub-Trending-CLI",
       "Authorization": "token YOUR_TOKEN_HERE"
   }
   ```

## 🐛 Troubleshooting

### Error: `No repositories found`
- Try a different language or time period
- Check your internet connection
- GitHub API might be rate-limited (wait an hour)

### Error: `AttributeError: type object 'datetime.datetime' has no attribute 'UTC'`
- Your Python version is < 3.11
- Use `timezone.utc` instead of `datetime.UTC`

### Warning: `datetime.utcnow() is deprecated`
- Update the code to use `datetime.now(timezone.utc)`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- GitHub API for providing the data
- Python `requests` library
- Unicode box-drawing characters for beautiful CLI output

## 📞 Contact

Samiullah - [@Instagram](https://www.instagram.com/samiiiii_560/)

Project Link: [https://github.com/SamiKhan43/api-projects](https://github.com/SamiKhan43/api-projects)

## 🔮 Future Enhancements

- [ ] Export results to JSON/CSV
- [ ] Add color support with `colorama`
- [ ] Interactive mode with arrow key navigation
- [ ] Save favorite repositories
- [ ] Compare trending across multiple languages
- [ ] Desktop notifications for new trending repos

## 📚 Learning Objectives

By building this project, you will learn:

- 🔧 **CLI Development** - Building command-line applications with `argparse`
- 🌐 **API Integration** - Working with RESTful APIs and handling HTTP requests
- 📊 **Data Processing** - Parsing JSON responses and extracting relevant information
- ⚠️ **Error Handling** - Implementing robust error handling for network and API errors
- 📅 **Date/Time Manipulation** - Working with datetime objects and timedelta
- 🎨 **Output Formatting** - Creating beautiful CLI interfaces with Unicode characters
- 🔍 **Query Building** - Constructing complex API queries with filters
- 📦 **Package Management** - Managing dependencies and virtual environments

## 🏆 Project Status

This project fulfills all the requirements from the [roadmap.sh GitHub Trending CLI project](https://roadmap.sh/projects/github-trending-cli):

| Requirement | Status |
|-------------|--------|
| CLI Application | ✅ Complete |
| GitHub API Integration | ✅ Complete |
| Time Range Filtering | ✅ Complete |
| Language Filtering | ✅ Complete |
| Error Handling | ✅ Complete |
| JSON Parsing | ✅ Complete |
| Sorted by Stars | ✅ Complete |
| Formatted Output | ✅ Complete |
| Command-Line Arguments | ✅ Complete |
| Documentation | ✅ Complete |

## 📸 Screenshots

```
╔════════════════════════════════════════════════════════════════════╗
║ WEEKLY TRENDING - RUST                                             ║
╚════════════════════════════════════════════════════════════════════╝

┌─ Repository #1 ─────────────────────────────────────────────────────
│ Name       : denoland/deno
│ Language   : Rust
│ Stars      : ⭐ 92,456 | Forks: 🔱 5,123
│ Description: A modern runtime for JavaScript and TypeScript.
│ URL        : https://github.com/denoland/deno
└────────────────────────────────────────────────────────────────────
```

---


**Happy Coding! 🚀**

If you find this tool useful, please consider giving it a ⭐ on GitHub!