import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question():
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    question = '{} {}'.format(random_number_1, random_number_2)

    return question, random_number_1, random_number_2


def get_correct_answer(random_number_1, random_number_2):
    while random_number_1 > 0 and random_number_2 > 0:
        if random_number_1 > random_number_2:
            random_number_1 %= random_number_2
        else:
            random_number_2 %= random_number_1
    return str(random_number_1 + random_number_2)


def run():
    """Function defines conditions of the brain-gcd game."""

    question, random_number_1, random_number_2 = get_question()
    correct_answer = get_correct_answer(random_number_1, random_number_2)
    return question, correct_answer
