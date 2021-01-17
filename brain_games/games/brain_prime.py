import random
from brain_games import engine


def run():
    """Function defines conditions of the brain-prime game."""

    def randomize_number():
        """Function returns a random number from 1 to 100."""

        return random.randint(1, 100)

    def is_prime(random_number):
        """Function defines if the random number is prime."""

        divisors_list = list(range(2, 101))
        # excludes the random number from the divisors_list
        if random_number != 1:
            divisors_list.pop(divisors_list.index(random_number))
        for divisor in divisors_list:
            if random_number % divisor == 0:
                correct_answer = 'no'
                return correct_answer

        correct_answer = 'yes'
        return correct_answer

    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.run_engine(is_prime, randomize_number, game_task)
