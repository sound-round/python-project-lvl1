import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def start_round():
    """Function defines conditions of the brain-even game."""

    question = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'

    return question, correct_answer
