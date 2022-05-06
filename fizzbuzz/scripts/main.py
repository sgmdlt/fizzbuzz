#!env/bin/python
import sys

import prompt
from fizzbuzz.game import game


def main():
    try:
        game(from_input=prompt.integer, to_output=print, end=False)
    except KeyboardInterrupt:
        print('\nBue!')
        sys.exit(0)


if __name__ == '__main__':
    main()
