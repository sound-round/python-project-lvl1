#!usr/bin/env python

import prompt
import random
from brain_games import cli
from brain_games.scripts import brain_games

def main():

    def get_correct_answer(number):
        if number % 2 == 0:
            return 'yes'
        return 'no'

    brain_games.main()

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
            print("'{}' is wrong answer ;(. Correct answer was '{}'".format(user_answer, correct_answer))
            counter = 0
#    print('Congratulations, {}!'.format(cli.name)

if __name__ == '__main__':
    main()
