import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return divisor == number


def generate_round():
    """Function defines conditions of the brain-prime game."""

    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
