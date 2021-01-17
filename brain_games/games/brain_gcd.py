import random
import math
from brain_games import engine


TASK = 'Find the greatest common divisor of given numbers.'


def run():
    """Function defines conditions of the brain-gcd game."""

    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    question = '{} {}'.format(random_number_1, random_number_2)
    correct_answer = str(math.gcd(random_number_1, random_number_2))
    return question, correct_answer

