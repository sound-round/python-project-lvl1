import prompt


def greeting():
    """Function greets player, asks his name and returns it."""

    print('Welcome to The Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(player_name))
    return player_name


def run_engine(correct_answer_definer, question_randomizer, game_task):
    """Function runs a game.
    The first argument is a function, defining a correct answer.
    The second argument is a function, returning a question.
    The third argument shows a task, which player has to solve."""

    player_name = greeting()
    print(game_task)
    wins_counter = 0
    WINS_LIMIT = 3
    while wins_counter < WINS_LIMIT:
        generated_question = question_randomizer()
        correct_answer = correct_answer_definer(generated_question)
        print('Question: {}'.format(generated_question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            wins_counter += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  "\nLet's try again, {}!".format(user_answer,
                                                  correct_answer, player_name))
            wins_counter = 0
    print('Congratulations, {}!'.format(player_name))
