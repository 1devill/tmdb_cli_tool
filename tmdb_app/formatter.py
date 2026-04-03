from rich.console import Console
from rich.table import Table

class Formatter:
    def __init__(self, title):
        self.console = Console()
        self.table = Table(title=title)

    def add_column(self, header, **kwargs):
        self.table.add_column(header, **kwargs)

    def print_table(self):
        self.console.print(self.table)

    def add_row(self, *args):
        self.table.add_row(*args)
