from rich.console import Console
from rich.table import Table


class Formatter:
    def __init__(self):
        self.console = Console()
        self.table = Table(title="TMDB Movies")
        self.table.add_column("#", justify="right")
        self.table.add_column("Title", style="cyan")
        self.table.add_column("Year")
        self.table.add_column("Rating", justify="right")

    def get_table(self):
        return self.table

    def print_table(self):
        self.console.print(self.table)
