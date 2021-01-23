import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def run():
    """Function defines conditions of the brain-calc game."""

    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    random_operator, random_sign = random.choice([(operator.add, '+'),
                                                  (operator.sub, '-'),
                                                  (operator.mul, '*')])
    question = '{} {} {}'.format(random_number_1,
                                 random_sign, random_number_2)
    correct_answer = str(random_operator(random_number_1, random_number_2))
    return question, correct_answer
