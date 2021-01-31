import prompt


ROUNDS_COUNT = 3


def run(game):
    """Function runs a game."""

    print('Welcome to The Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(player_name))
    print(game.DESCRIPTION)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.start_round()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  "\nLet's try again, {}!".format(user_answer,
                                                  correct_answer, player_name))
            return
        print('Correct!')
    print('Congratulations, {}!'.format(player_name))
