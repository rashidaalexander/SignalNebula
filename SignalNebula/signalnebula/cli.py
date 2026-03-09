
from __future__ import annotations
import argparse
from .engine import analyze
from .utils import to_json

def main() -> None:
    parser = argparse.ArgumentParser(prog="signalnebula")
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("analyze")
    a.add_argument("path")
    s = sub.add_parser("spectrum")
    s.add_argument("path")
    args = parser.parse_args()
    result = analyze(args.path)
    print(to_json(result))

if __name__ == "__main__":
    main()
