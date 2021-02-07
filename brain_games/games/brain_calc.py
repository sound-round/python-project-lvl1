import random
import operator


DESCRIPTION = 'What is the result of the expression?'
map_operator_to_operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculate(first_number, second_number, operator):
    return map_operator_to_operation[operator](first_number, second_number)


def generate_round():
    """Function defines conditions of the brain-calc game."""

    first_random_number = random.randint(1, 100)
    second_random_number = random.randint(1, 100)
    random_operator = random.choice(list(map_operator_to_operation.keys()))
    question = '{} {} {}'.format(first_random_number,
                                 random_operator, second_random_number)
    correct_answer = str(calculate(first_random_number,
                                   second_random_number,
                                   random_operator))
    return question, correct_answer
