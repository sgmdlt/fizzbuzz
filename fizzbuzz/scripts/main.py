#!env/bin/python
import sys

from fizzbuzz.game import game


def main():
    try:
        game()
    except KeyboardInterrupt:
        print('\nBue!')
        sys.exit(0)


if __name__ == '__main__':
    main()
