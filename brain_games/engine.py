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
    wins_counter = 0
    WINS_LIMIT = 3
    while wins_counter < WINS_LIMIT:
        generated_question = randomize_question()
        correct_answer = get_correct_answer(generated_question)
        print('Question: {}'.format(generated_question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            wins_counter += 1
            continue

        print("'{}' is wrong answer ;(. Correct answer was '{}'."
              "\nLet's try again, {}!".format(user_answer,
                                              correct_answer, player_name))
        wins_counter = 0

    print('Congratulations, {}!'.format(player_name))
