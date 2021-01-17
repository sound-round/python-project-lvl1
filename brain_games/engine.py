import prompt


def run(game):
    """Function runs a game."""

    print('Welcome to The Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(player_name))
    print(game.GAME_TASK)
    for win in range(0, 3):
        question, correct_answer = game.run()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            continue

        print("'{}' is wrong answer ;(. Correct answer was '{}'."
              "\nLet's try again, {}!".format(user_answer,
                                              correct_answer, player_name))
        break

    if user_answer == correct_answer:
        print('Congratulations, {}!'.format(player_name))
