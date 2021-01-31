import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(number_1, number_2):
    if number_2 == 0:
        return number_1
    return get_gcd(number_2, number_1 % number_2)


def start_round():
    """Function defines conditions of the brain-gcd game."""

    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    question = '{} {}'.format(random_number_1, random_number_2)
    correct_answer = str(get_gcd(random_number_1, random_number_2))
    return question, correct_answer
