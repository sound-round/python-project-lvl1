import prompt


def greeting():
    """Function greets player, asks his name and returns it."""

    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def run_engine(function, randomizer, string):
    """Function runs a game.
    The first argument is a function, defining a correct answer.
    The second argument is a function, returning a question.
    The third argument shows a task, which player has to solve."""

    name = greeting()
    print(string)
    counter = 0
    while counter < 3:
        question = randomizer()
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
