import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    divisor = 2
    while question % divisor != 0:
        divisor += 1
    return divisor == question


def round():
    """Function defines conditions of the brain-prime game."""

    question = random.randint(1, 100)
    predicate = is_prime(question)
    correct_answer = 'yes' if predicate else 'no'

    return question, correct_answer
