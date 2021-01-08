import random
from brain_games.games import engine


def run_brain_prime():
    """Function defines conditions of the brain-prime game."""

    def get_correct_answer(number):
        """Function defines correct answer for a random number."""

        range_list = list(range(2, 101))
        # excludes the number from the range
        if number != 1:
            range_list.pop(range_list.index(number))
        for divisor in range_list:
            if number % divisor == 0:
                correct_answer = 'no'
                return correct_answer

        correct_answer = 'yes'
        return correct_answer

    def randomizer():
        """Function returns a random number from 1 to 100."""

        return random.randint(1, 100)

    string = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.run_engine(get_correct_answer, randomizer, string)
