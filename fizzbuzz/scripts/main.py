#!env/bin/python
import sys

import prompt
from fizzbuzz.game import game


def main():
    try:
        game(input=prompt.integer, output=print)
    except KeyboardInterrupt:
        print('\nBue!')
        sys.exit(0)


if __name__ == '__main__':
    main()
