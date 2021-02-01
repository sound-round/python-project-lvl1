import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_gcd(first_number, second_number):
    if second_number == 0:
        return first_number
    return get_gcd(second_number, first_number % second_number)


def generate_round():
    """Function defines conditions of the brain-gcd game."""

    first_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = '{} {}'.format(first_random_number, second_random_number)
    correct_answer = str(get_gcd(first_random_number, second_random_number))
    return question, correct_answer
