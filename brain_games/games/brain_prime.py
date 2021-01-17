import random
from brain_games import engine


def run():
    """Function defines conditions of the brain-prime game."""

    def randomize_number():
        """Function returns a random number from 1 to 100."""

        return random.randint(1, 100)

    def is_prime(random_number):
        """Function defines if the random number is prime."""

        divisors = list(range(2, 101))
        # excludes the random number from the divisors
        if random_number != 1:
            divisors.pop(divisors.index(random_number))
        for divisor in divisors:
            if random_number % divisor == 0:
                correct_answer = 'no'
                return correct_answer

        correct_answer = 'yes'
        return correct_answer

    GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.run(is_prime, randomize_number, GAME_TASK)
