import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def run():
    """Function defines conditions of the brain-even game."""

    question = random.randint(1, 100)
    correct_answer = 'no'
    if question % 2 == 0:
        correct_answer = 'yes'
    return question, correct_answer
