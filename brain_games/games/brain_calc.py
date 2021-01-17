import random
from brain_games.games import engine


def run():
    """Function defines conditions of the brain-calc game."""

    def randomize_expression():
        """Function returns an expression for solving it."""

        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        random_operator = random.choice(['+', '-', '*'])
        return '{} {} {}'.format(random_number_1,
                                 random_operator, random_number_2)

    def get_correct_answer(generated_question):
        """Function defines correct answer for an expression"""

        return str(eval(generated_question))

    game_task = 'What is the result of the expression?'
    engine.run_engine(get_correct_answer, randomize_expression, game_task)
