import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    question = random.randint(1, 100)
    return question


def get_correct_answer(predicate):
    return 'yes' if predicate else 'no'


def is_even(question):
    return question % 2 == 0


def round():
    """Function defines conditions of the brain-even game."""

    question = get_question()
    predicate = is_even(question)
    correct_answer = get_correct_answer(predicate)

    return question, correct_answer
