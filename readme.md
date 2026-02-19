# 🚀 API Projects Collection

A curated collection of Python applications demonstrating API integration, data parsing, error handling, and beautiful terminal output. Each project is designed to help developers learn different aspects of working with REST APIs.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Projects](https://img.shields.io/badge/Projects-4-green.svg)
[![roadmap.sh](https://img.shields.io/badge/roadmap.sh-projects-purple.svg)](https://roadmap.sh)

---

## 📚 Projects

### 1. 🔥 GitHub Trending
Fetch and display trending GitHub repositories with customizable filters.

**Features:**
- View trending repos by time period (daily, weekly, monthly)
- Filter by programming language
- Beautiful formatted output with stars and forks count
- Uses GitHub's official REST API

**Tech Stack:** Python, Requests, GitHub API

📁 [View Project](./github-trending/) | 🌐 [roadmap.sh](https://roadmap.sh/projects/github-trending-cli)

---

### 2. 👤 GitHub User Activity
Track and display recent activity for any GitHub user.

**Features:**
- View user's recent commits, pull requests, and issues
- Display repository activity
- Filter by activity type
- Real-time data from GitHub API

**Tech Stack:** Python, Requests, GitHub API

📁 [View Project](./github-user-activity/)

---

### 3. 🎬 TMDB Movies
Browse and discover movies from The Movie Database.

**Features:**
- View now playing, popular, top-rated, and upcoming movies
- Search movies by title
- Display ratings, release dates, and descriptions
- Beautiful terminal interface

**Tech Stack:** Python, Requests, TMDB API

📁 [View Project](./tmdb-movies/)

---

### 4. 🌤️ Weather API
Get current weather information for any location.

**Features:**
- Real-time weather data
- Temperature, humidity, and conditions
- Support for multiple locations
- Clean and readable output

**Tech Stack:** Python, Requests, Weather API

📁 [View Project](./weather-api/)

---

## 🎯 What You'll Learn

By exploring these projects, you'll learn:

- ✅ **API Integration** - Working with RESTful APIs and handling HTTP requests
- ✅ **Authentication** - Managing API keys and tokens securely
- ✅ **Data Parsing** - Processing JSON responses and extracting data
- ✅ **Error Handling** - Handling network errors, rate limits, and API failures
- ✅ **Command-Line Arguments** - Using `argparse` for user input
- ✅ **Environment Variables** - Storing sensitive data securely
- ✅ **Date/Time Manipulation** - Working with datetime objects
- ✅ **Output Formatting** - Creating beautiful terminal interfaces
- ✅ **Code Organization** - Structuring Python projects properly

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- API keys (where required)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/api-projects.git
   cd api-projects
   ```

2. **Choose a project:**
   ```bash
   cd github-trending
   # or
   cd github-user-activity
   # or
   cd tmdb-movies
   # or
   cd weather-api
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Follow project-specific instructions** in each project's README.

---

## 📋 Project Structure

```
api-projects/
│
├── github-trending/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── github-user-activity/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── tmdb-movies/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── weather-api/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
└── README.md (this file)
```

---

## 🔑 API Keys Setup

Some projects require API keys. Here's where to get them:

| Project | API Provider | Sign Up Link | Free Tier |
|---------|-------------|--------------|-----------|
| GitHub Trending | GitHub | [github.com/settings/tokens](https://github.com/settings/tokens) | 60 req/hour (5000 with auth) |
| GitHub User Activity | GitHub | [github.com/settings/tokens](https://github.com/settings/tokens) | 60 req/hour (5000 with auth) |
| TMDB Movies | The Movie Database | [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api) | Yes (1000 req/day) |
| Weather API | OpenWeatherMap | [openweathermap.org/api](https://openweathermap.org/api) | Yes (60 req/min) |

### How to Store API Keys Securely

1. **Create a `.env` file** in each project folder:
   ```bash
   cp .env.example .env
   ```

2. **Add your API keys:**
   ```env
   GITHUB_TOKEN=your_token_here
   TMDB_API_KEY=your_key_here
   WEATHER_API_KEY=your_key_here
   ```

3. **Never commit `.env` files** - they're already in `.gitignore`

---

## 🛠️ Technologies Used

- **Language:** Python 3.7+
- **HTTP Library:** Requests
- **Argument Parsing:** argparse
- **Environment Variables:** python-dotenv
- **Date/Time:** datetime

---

## 📖 Common Dependencies

All projects use similar dependencies:

```txt
requests>=2.31.0
python-dotenv>=1.0.0
```

Install globally for all projects:
```bash
pip install requests python-dotenv
```

---

## 🎨 Example Outputs

### GitHub Trending
```
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

### TMDB Movies
```
╔════════════════════════════════════════════════════════════════════╗
║ POPULAR MOVIES                                                     ║
╚════════════════════════════════════════════════════════════════════╝

┌─ Movie #1 ──────────────────────────────────────────────────────────
│ Title      : The Shawshank Redemption
│ Released   : 1994-09-23
│ Rating     : 8.7/10 ⭐
│ Overview   : Two imprisoned men bond over a number of years...
└────────────────────────────────────────────────────────────────────
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Ideas for New Projects

- [ ] Reddit API browser
- [ ] Stack Overflow search tool
- [ ] Cryptocurrency price tracker
- [ ] News aggregator
- [ ] Spotify playlist manager
- [ ] Twitter/X timeline viewer

---

## 📝 Best Practices Demonstrated

Each project follows these best practices:

- ✅ **Error Handling** - Proper try-except blocks and meaningful error messages
- ✅ **Code Organization** - Functions for single responsibilities
- ✅ **Documentation** - Clear README files and code comments
- ✅ **Security** - API keys stored in environment variables
- ✅ **User Experience** - Beautiful formatted output and helpful error messages
- ✅ **Command-Line Interface** - Intuitive argument parsing
- ✅ **Rate Limiting** - Respectful API usage
- ✅ **Type Hints** - Clear function signatures (where applicable)

---

## 🐛 Troubleshooting

### Common Issues

**Problem:** `ModuleNotFoundError: No module named 'requests'`
```bash
pip install requests
```

**Problem:** `API key not found`
- Make sure you created a `.env` file
- Check that the key name matches the one in the code
- Verify the key is valid on the API provider's website

**Problem:** `Rate limit exceeded`
- Wait for the rate limit to reset (usually 1 hour)
- Use authentication to increase limits
- Reduce the frequency of requests

**Problem:** `Connection error`
- Check your internet connection
- Verify the API endpoint is correct
- Check if the API service is down

---

## 📚 Resources

### API Documentation
- [GitHub REST API](https://docs.github.com/en/rest)
- [TMDB API](https://developers.themoviedb.org/3)
- [OpenWeatherMap API](https://openweathermap.org/api)

### Learning Resources
- [roadmap.sh Backend Projects](https://roadmap.sh/backend/projects)
- [Python Requests Documentation](https://requests.readthedocs.io/)
- [Working with APIs in Python](https://realpython.com/python-api/)
- [Command Line Arguments in Python](https://realpython.com/command-line-interfaces-python-argparse/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [roadmap.sh](https://roadmap.sh) for project ideas and inspiration
- GitHub, TMDB, and OpenWeatherMap for providing free APIs
- The Python community for excellent libraries

---

## 📞 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/api-projects](https://github.com/yourusername/api-projects)

---

## 🌟 Show Your Support

If you found these projects helpful, please consider:

- ⭐ Starring the repository
- 🍴 Forking and building upon it
- 📢 Sharing with others learning Python
- 💬 Opening issues for suggestions

---

**Happy Coding! 🚀**

Made with ❤️ for developers learning API integration