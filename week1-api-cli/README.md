# Week 1 — Movie Search CLI

Searches TMDB for a movie title and saves the top match's title, release date, and overview to `result.json`.

## Setup
1. Copy `.env.example` to `.env` at the repo root and add your TMDB API key
2. `uv sync`

## Usage
uv run week1-api-cli/movie_search.py "movie title"

## AI Disclosure
This project was built by me, with Claude AI used as a first-principles teaching tool throughout development, and Claude Code used afterward for a code review and two small fixes (request timeout, correct exit-code handling).
