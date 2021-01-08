import random
import math
from brain_games.games import engine


def run_brain_gcd():
    """Function defines conditions of the brain-gcd game."""

    def get_correct_answer(question):
        """Function defines greatest common divisor for two numbers"""

        a, b = question.split(' ')  # splits a string into numbers.
        number_1 = int(a)
        number_2 = int(b)
        return str(math.gcd(number_1, number_2))

    def randomizer():
        """Function returns string with two random numbers"""

        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        return '{} {}'.format(number_1, number_2)

    string = 'Find the greatest common divisor of given numbers.'
    engine.run_engine(get_correct_answer, randomizer, string)
