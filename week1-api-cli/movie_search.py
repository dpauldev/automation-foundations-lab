import argparse
import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

if not api_key:
    print("Error: TMDB_API_KEY not found. Check your .env file")
    sys.exit(1)

parser = argparse.ArgumentParser(description="Search for a movie using TMDB")
parser.add_argument("title", help="The movie title to search for")
args = parser.parse_args()

print(f"You searched for: {args.title}")

url = "https://api.themoviedb.org/3/search/movie"

params = {"api_key": api_key, "query": args.title}

response = requests.get(url, params, timeout=10)

if response.status_code != 200:
    print(
        f"Error: TMDB returned status {response.status_code}. Check the API Key and/or connection status."
    )
    sys.exit(1)

data = response.json()
results = data["results"]

if not results:
    print(f"No movie found for '{args.title}'. ")
    sys.exit(1)

movie = results[0]
print(f"Title: {movie['title']}")
print(f"Release Date: {movie['release_date']}")
print(f"Overview: {movie['overview']}")

movie_data = {
    "title": movie["title"],
    "release_date": movie["release_date"],
    "overview": movie["overview"],
}

with open("result.json", "w") as f:
    json.dump(movie_data, f, indent=4)

print(f"Saved details for {movie['title']} to result.json file")
