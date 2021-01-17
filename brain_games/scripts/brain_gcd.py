#!usr/bin/env python

from brain_games import engine
from brain_games.games import brain_gcd


def main():
    engine.run(brain_gcd)


if __name__ == '__main__':
    main()
