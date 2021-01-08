import random
from brain_games.games import engine


def run_brain_calc():
    """Function defines conditions of the brain-calc game."""

    def get_correct_answer(question):
        """Function defines correct answer for an expression"""

        return str(eval(question))

    def randomizer():
        """Function returns an expression"""

        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        sign = random.choice(['+', '-', '*'])
        return '{} {} {}'.format(number_1, sign, number_2)

    string = 'What is the result of the expression?'
    engine.run_engine(get_correct_answer, randomizer, string)
