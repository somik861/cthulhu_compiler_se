from argparse import ArgumentParser
from pathlib import Path

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)

    args = parser.parse_args()
