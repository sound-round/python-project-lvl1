import random
import math
from brain_games import engine


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def run():
    """Function defines conditions of the brain-gcd game."""

    def randomize_numbers():
        """Function returns string with two random numbers"""

        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        return '{} {}'.format(random_number_1, random_number_2)

    def find_greatest_common_divisor(question):
        """Function defines greatest common divisor for two numbers"""

        a, b = question.split(' ')  # splits a string into numbers.
        number_1 = int(a)
        number_2 = int(b)
        return str(math.gcd(number_1, number_2))

    engine.run(find_greatest_common_divisor,
               randomize_numbers, GAME_TASK)