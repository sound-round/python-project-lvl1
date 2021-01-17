import prompt


def run(get_correct_answer, randomize_question, GAME_TASK):
    """Function runs a game.
    The first argument is a function, defining a correct answer.
    The second argument is a function, returning a question.
    The third argument shows a task, which player has to solve."""

    print('Welcome to The Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(player_name))
    print(GAME_TASK)
    for win in range(0, 3):
        generated_question = randomize_question()
        correct_answer = get_correct_answer(generated_question)
        print('Question: {}'.format(generated_question))
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
