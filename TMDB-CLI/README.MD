# TMDB CLI Tool

A command-line interface tool for fetching and displaying movie information from The Movie Database (TMDB) API.

**Project Reference**: [roadmap.sh TMDB CLI Project](https://roadmap.sh/projects/tmdb-cli)

## Features

- Fetch movies from multiple categories:
  - Now Playing
  - Popular
  - Top Rated
  - Upcoming
- Beautiful formatted output with movie details
- Customizable number of results
- Simple command-line interface

## Prerequisites

- Python 3.6+
- TMDB API Key (get one from [TMDB](https://www.themoviedb.org/settings/api))

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project root:
```bash
TMDB_API_KEY=your_api_key_here
```

## Usage

Basic syntax:
```bash
python script.py --type <category> [--count <number>]
```

### Arguments

- `--type` (required): Category of movies to fetch
  - `playing` - Now playing in theaters
  - `popular` - Popular movies
  - `top` - Top rated movies
  - `upcoming` - Upcoming releases

- `--count` (optional): Number of movies to display (default: 1)

### Examples

Fetch 1 popular movie (default):
```bash
python script.py --type popular
```

Fetch 5 top-rated movies:
```bash
python script.py --type top --count 5
```

Fetch 3 upcoming movies:
```bash
python script.py --type upcoming --count 3
```

## Output Format

The tool displays movies with the following information:
- Title
- Release Date
- Rating (out of 10)
- Overview (truncated to 60 characters)

Example output:
```
╔════════════════════════════════════════════════════════════════════╗
║ POPULAR MOVIES                                                     ║
╚════════════════════════════════════════════════════════════════════╝

┌─ Movie #1 ─────────────────────────────────────────────────────────
│ Title      : Example Movie Title
│ Released   : 2024-01-15
│ Rating     : 8.5/10 
│ Overview   : This is an exciting movie about...
└────────────────────────────────────────────────────────────────────
```

## Error Handling

The tool includes error handling for:
- Missing API key
- Network request failures
- Invalid API responses

## Dependencies

- `requests` - HTTP library for API calls
- `python-dotenv` - Environment variable management

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to submit issues or pull requests to improve this tool.

## API Reference

This tool uses the TMDB API v3. For more information, visit the [TMDB API Documentation](https://developers.themoviedb.org/3).