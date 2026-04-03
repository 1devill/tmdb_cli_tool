# TMDB CLI Tool
Related roadmap project - [tmdb-cli](https://roadmap.sh/projects/tmdb-cli)

<p align="center">
  <img src="https://img.shields.io/github/stars/1devill/tmdb_cli_tool?style=for-the-badge&color=yellow" />
  <img src="https://img.shields.io/github/forks/1devill/tmdb_cli_tool?style=for-the-badge&color=green" />
  <img src="https://img.shields.io/github/issues/1devill/tmdb_cli_tool?style=for-the-badge&color=blue" />
  <img src="https://img.shields.io/github/issues-pr/y1devill/tmdb_cli_tool?style=for-the-badge&color=orange" />
</p>
A simple command-line application that fetches and displays movie data from The Movie Database (TMDB) API in a pretty tabular format.

## Features
1. Filter by category (popular, top, upcoming, playing)
2. Colorized tabular output for better readability
3. Detailed movie information including release dates and ratings
4. Error handling for network issues

## You will get an output:
<p align="center">
  <img width="467" height="436" alt="Screenshot 2026-04-03 at 20 17 22" src="https://github.com/user-attachments/assets/218b00f9-080b-4f59-a6bf-5f84ac1a8786" />
</p>

## Prerequisites
* Python 3.12 or higher
* TMDB API key (You can get an API key from [TMDB](https://www.themoviedb.org))

## Installation
```bash
git clone https://github.com/1devill/tmdb_cli_tool.git
cd tmdb-app
pip install -r requirements.txt
pip install -e .
```

## 🔑 Environment setup

First check `.env.example` for the reference, which variables you need
Create a `.env` file in the root directory:

```env
TMDB_API_KEY=your_api_key_here
BASE_API_URL=https://api.themoviedb.org/3
```

## 💻 Usage

```bash
tmdb-app --type=popular
tmdb-app --type=top
tmdb-app --type=upcoming
tmdb-app --type=playing
```

## 🏗 Project structure

```bash
tmdb_app/
├── main.py          # CLI entry point
├── api.py           # API logic
├── endpoints.py     # API endpoints mapping
└── formatter.py     # Response formatter
```

## Future Improvements

- Add pagination
- Add search functionality
- Improve CLI output with rich formatting
- Add tests

## Author

Daniil

- GitHub: https://github.com/1devill
