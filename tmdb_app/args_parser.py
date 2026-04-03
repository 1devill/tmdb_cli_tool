import argparse

class ArgsParser:
    def __init__(self, args):
        self.parser = argparse.ArgumentParser()
        for arg in args:
            self.parser.add_argument(arg, required=True)
        self.args = args

    def get_args(self):
        return self.parser.parse_args()