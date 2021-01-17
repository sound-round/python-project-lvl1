import random
from brain_games.games import engine


def run():
    """Function defines conditions of the brain-even game."""

    def number_randomizer():
        """Function returns a random number from 1 to 100."""

        return random.randint(1, 100)

    def is_even(random_number):
        """Function defines if the random number is even"""

        if random_number % 2 == 0:
            return 'yes'
        return 'no'

    game_task = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.run_engine(is_even, number_randomizer, game_task)
