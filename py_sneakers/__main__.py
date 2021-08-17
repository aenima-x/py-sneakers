import sys
from py_sneakers.py_sneakers import Sneakers


def main():
    Sneakers(sys.stdin.read()).decrypt()


if __name__ == "__main__":
    main()