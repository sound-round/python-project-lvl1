import prompt
import random


def greeting():
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def brain_even():

    def get_correct_answer(number):
        if number % 2 == 0:
            return 'yes'
        return 'no'

    name = greeting()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    while counter < 3:
        number = random.randint(1, 100)
        correct_answer = get_correct_answer(number)
        print('Question: {}'.format(number))
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
