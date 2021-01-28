import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(random_number_1, random_number_2):
    while random_number_2:
        random_number_1, random_number_2 = random_number_2,\
                                           random_number_1 % random_number_2
    return str(random_number_1)


def round():
    """Function defines conditions of the brain-gcd game."""

    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    question = '{} {}'.format(random_number_1, random_number_2)
    correct_answer = get_gcd(random_number_1, random_number_2)
    return question, correct_answer
