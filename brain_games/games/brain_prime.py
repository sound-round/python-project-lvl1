import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    return random.randint(1, 100)


def get_correct_answer(predicate):
    return 'yes' if predicate else 'no'


def is_prime(question):
    divisor = 2
    while question % divisor != 0:
        divisor += 1
    return divisor == question


def round():
    """Function defines conditions of the brain-prime game."""

    question = get_question()
    predicate = is_prime(question)
    correct_answer = get_correct_answer(predicate)

    return question, correct_answer
