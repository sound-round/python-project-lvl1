import random
from brain_games.games import engine


def run_brain_even():
    """Function defines conditions of the brain-even game."""

    def get_correct_answer(number):
        """Function defines correct answer for a random number."""

        if number % 2 == 0:
            return 'yes'
        return 'no'

    def randomizer():
        """Function returns a random number from 1 to 100."""

        return random.randint(1, 100)

    string = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.run_engine(get_correct_answer, randomizer, string)
