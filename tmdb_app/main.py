from tmdb_app.api import Api
from tmdb_app.args_parser import ArgsParser
from tmdb_app.endpoints import ENDPOINTS
from tmdb_app.formatter import Formatter


def main():
    api = Api()
    args_parser = ArgsParser(["--type"])
    formatter = Formatter()

    movie_type_arg = args_parser.get_args().type
    if movie_type_arg not in ENDPOINTS:
        print("Please specify one of type: popular, top, playing, upcoming")
        return

    results = api.get(ENDPOINTS[movie_type_arg])

    if not results:
        print("No results found")
        return

    for i, movie in enumerate(results):
        formatter.get_table().add_row(str(i), movie["title"], movie.get("release_date", "")[:4], str(movie.get("vote_average", "N/A")))
        formatter.print_table()

if __name__ == "__main__":
    main()