import os
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/movie/"

def fetch_movies(movie_type):
    endpoint_map = {
        "playing": "now_playing",
        "popular": "popular",
        "top": "top_rated",
        "upcoming": "upcoming"
    }
    
    url = f"{BASE_URL}{endpoint_map[movie_type]}"
    params = {"api_key": API_KEY, "language": "en-US", "page": 1}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        return response.json().get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def display_movies(movies, category_name, limit=1):
    if not movies:
        print("No movies found or API error.")
        return

    print(f"\n╔{'═'*68}╗")
    print(f"║ {category_name.upper()} MOVIES{' '*(61-len(category_name))}║")
    print(f"╚{'═'*68}╝\n")
    
    for i, movie in enumerate(movies[:limit], 1):
        print(f"┌─ Movie #{i} {'─'*57}")
        print(f"│ Title      : {movie['title']}")
        print(f"│ Released   : {movie.get('release_date', 'N/A')}")
        print(f"│ Rating     : {movie['vote_average']}/10 ")
        print(f"│ Overview   : {movie['overview'][:60]}...")
        print(f"└{'─'*68}\n")

def main():
    if not API_KEY:
        print("Error: TMDB_API_KEY not found in environment. Check your .env file.")
        return

    parser = argparse.ArgumentParser(description="TMDB CLI Tool")
    parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=["playing", "popular", "top", "upcoming"],
        help="Category of movies to fetch"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of movies to display (default: 1)"
    )
    
    args = parser.parse_args()
    
    print("\n Fetching data from TMDB...", end=" ", flush=True)
    movie_data = fetch_movies(args.type)
    print("Done! ✓")
    
    display_movies(movie_data, args.type, limit=args.count)

if __name__ == "__main__":
    main()
