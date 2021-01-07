import prompt
import random
import math


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


def run_brain_gcd():
    """Function defines conditions of the brain-gcd game."""

    def get_correct_answer(question):
        """Function defines greatest common divisor for two numbers"""

        a, b = question.split(' ')  # splits a string into numbers.
        number_1 = int(a)
        number_2 = int(b)
        return str(math.gcd(number_1, number_2))

    def randomiser():
        """Function returns string with two random numbers"""

        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        return '{} {}'.format(number_1, number_2)

    string = 'Find the greatest common divisor of given numbers.'
    run_engine(get_correct_answer, randomiser, string)


def run_brain_progression():
    """Function defines conditions of the brain-progression game."""

    def get_correct_answer(question):
        """Function defines the correct_answer."""

        progression_list = question.split(' ')
        index_number = progression_list.index('..')  # index of the hidden element.
        if index_number == 0:  # for the case if the first element was hidden.
            correct_answer = int(int(progression_list[1])
                                 - (int(progression_list[2])
                                 - int(progression_list[1])))
        elif index_number == len(progression_list) - 1:  # for the case if the last element was hidden.
            correct_answer = int(int(progression_list[-2])
                                 - int(progression_list[-3])
                                 + int(progression_list[-2]))
        else:
            pr_index = index_number - 1  # index of the previous element.
            nx_index = index_number + 1  # index of the next element.
            correct_answer = int((int(progression_list[nx_index]) -
                                  int(progression_list[pr_index])) / 2
                                 + int(progression_list[pr_index]))
        return str(correct_answer)

    def randomiser():
        """Function returns a progression with a hidden element in string."""

        first_number = random.randint(1, 20)  # defines the first number of a progression.
        step = random.randint(1, 5)  # defines a step of a progression.
        progression_list = [str(first_number)]
        limit = random.randint(5, 10)  # defines length of a progression.
        for i in range(1, limit):
            number = first_number + step * i
            progression_list.append(str(number))
        index_hidden_element = random.randint(0, len(progression_list) - 1)
        progression_list.pop(index_hidden_element)
        progression_list.insert(index_hidden_element, '..')
        progression_string = ' '.join(progression_list)
        return progression_string

    string = 'What number is missing in the progression?'
    run_engine(get_correct_answer, randomiser, string)
