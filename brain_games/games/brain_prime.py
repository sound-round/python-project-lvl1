import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run():
    """Function defines conditions of the brain-prime game."""

    question = random.randint(1, 100)
    correct_answer = 'yes'

    divisors = list(range(2, 101))
    # excludes the random number from the divisors
    if question != 1:
        divisors.pop(divisors.index(question))
    for divisor in divisors:
        if question % divisor == 0:
            correct_answer = 'no'
    return question, correct_answer
