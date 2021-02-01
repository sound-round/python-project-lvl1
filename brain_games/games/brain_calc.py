import random
import operator

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATORS = ['+', '-', '*']
MAP_OPERATOR_TO_OPERATION = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculate_answer(first_number, second_number, operator):
    return MAP_OPERATOR_TO_OPERATION[operator](first_number, second_number)


def generate_round():
    """Function defines conditions of the brain-calc game."""

    first_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_operator = random.choice(OPERATORS)
    question = '{} {} {}'.format(first_random_number,
                                 random_operator, second_random_number)
    correct_answer = str(calculate_answer(first_random_number,
                                          second_random_number,
                                          random_operator))
    return question, correct_answer
