import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    return question % 2 == 0


def round():
    """Function defines conditions of the brain-even game."""

    question = random.randint(1, 100)
    predicate = is_even(question)
    correct_answer = 'yes' if predicate else 'no'

    return question, correct_answer
