import random
import copy

DESCRIPTION = 'What number is missing in the progression?'
GAP = '..'


def get_progression(first_number, step, length):
    progression = [str(first_number + step * i) for i in range(length)]
    return progression


def get_correct_answer(progression, index_hidden_element):
    copy_progression = copy.copy(progression)
    correct_answer = copy_progression.pop(index_hidden_element)
    return correct_answer


def get_question(progression, index_hidden_element):
    copy_progression = copy.copy(progression)
    copy_progression[index_hidden_element] = GAP
    question = ' '.join(copy_progression)
    return question


def round():
    """Function defines conditions of the brain-progression game."""

    # defines the first number of a progression.
    first_number = random.randint(1, 20)
    # defines a step of a progression.
    step = random.randint(1, 5)
    # defines length of a progression.
    length = random.randint(5, 10)
    progression = get_progression(first_number, step, length)

    index_hidden_element = random.randint(0, len(progression) - 1)

    question = get_question(progression, index_hidden_element)
    correct_answer = get_correct_answer(progression, index_hidden_element)

    return question, correct_answer
