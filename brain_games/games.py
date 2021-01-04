import prompt
import random


def greeting():
    """Function greets player, asks his name and returns it."""
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def run_engine(function, randomiser, string):
    """Function runs a game.
    The first argument is a function, defining a correct answer.
    The second argument is a function, returning a question.
    The third argument shows a task, which player has to solve."""

    name = greeting()
    print(string)
    counter = 0
    while counter < 3:
        question = randomiser()
        correct_answer = function(question)
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  "\nLet's try again, {}!".format(user_answer,
                                                  correct_answer, name))
            counter = 0
    print('Congratulations, {}!'.format(name))


def run_brain_even():
    """Function defines conditions of the brain-even game."""

    def get_correct_answer(number):
        """Function defines correct answer for a random number."""

        if number % 2 == 0:
            return 'yes'
        return 'no'

    def randomiser():
        """Function returns a random number from 1 to 100."""
        return random.randint(1, 100)

    string = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_engine(get_correct_answer, randomiser, string)


def run_brain_calc():
    """Function defines conditions of the brain-calc game."""

    def get_correct_answer(question):
        """Function defines correct answer for an expression"""

        return str(eval(question))

    def randomiser():
        """Function returns an expression"""
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        sign = random.choice(['+', '-', '*'])
        return '{} {} {}'.format(number_1, sign, number_2)

    string = 'What is the result of the expression?'
    run_engine(get_correct_answer, randomiser, string)
