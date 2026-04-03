import argparse

from tmdb_app.api import Api
from tmdb_app.endpoints import ENDPOINTS
from tmdb_app.formatter import Formatter

def create_table(formatter):
    formatter.add_column("#", justify="right")
    formatter.add_column("Title", style="cyan")
    formatter.add_column("Year")
    formatter.add_column("Rating", justify="right")


def main():
    api = Api()
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', required=True)
    formatter = Formatter("TMDB Movies")
    create_table(formatter)

    movie_type_arg = parser.parse_args().type
    if movie_type_arg not in ENDPOINTS:
        print("Please specify one of type: popular, top, playing, upcoming")
        return

    results = api.get(ENDPOINTS[movie_type_arg])

    if not results:
        print("No results found")
        return

    for i, movie in enumerate(results):
        formatter.add_row(str(i), movie["title"], movie.get("release_date", "")[:4], str(movie.get("vote_average", "N/A")))

    formatter.print_table()

if __name__ == "__main__":
    main()