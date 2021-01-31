import random
import operator

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100


def start_round():
    """Function defines conditions of the brain-calc game."""

    random_number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operators = [(operator.add, '+'), (operator.sub, '-'), (operator.mul, '*')]
    random_operator, random_sign = random.choice(operators)

    question = '{} {} {}'.format(random_number_1,
                                 random_sign, random_number_2)
    correct_answer = str(random_operator(random_number_1, random_number_2))
    return question, correct_answer
