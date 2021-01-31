import random
import operator

DESCRIPTION = 'What is the result of the expression?'


def get_question(number_1, number_2, sign):
    question = '{} {} {}'.format(number_1,
                                 sign, number_2)
    return question


def get_correct_answer(number_1, number_2, operator):
    correct_answer = str(operator(number_1, number_2))
    return correct_answer


def start_round():
    """Function defines conditions of the brain-calc game."""

    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    operators = [(operator.add, '+'), (operator.sub, '-'), (operator.mul, '*')]
    random_operator, random_sign = random.choice(operators)

    question = get_question(random_number_1, random_number_2, random_sign)
    correct_answer = get_correct_answer(random_number_1,
                                        random_number_2, random_operator)
    return question, correct_answer
