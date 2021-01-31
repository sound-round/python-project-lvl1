import random
import copy


DESCRIPTION = 'What number is missing in the progression?'
GAP = '..'
MIN_LENGTH = 5
MAX_LENGTH = 10
MAX_STEP = 5
MIN_STEP = 1


def get_progression(start, step, length):
    progression = [str(start + step * i) for i in range(length)]
    return progression


def get_question(progression, hidden_element_index):
    copy_progression = copy.copy(progression)
    copy_progression[hidden_element_index] = GAP
    question = ' '.join(copy_progression)
    return question


def start_round():
    """Function defines conditions of the brain-progression game."""

    # defines the first number of a progression.
    start = random.randint(1, 20)
    # defines a step of a progression.
    step = random.randint(MIN_STEP, MAX_STEP)
    # defines length of a progression.
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = get_progression(start, step, length)

    hidden_element_index = random.randint(0, len(progression) - 1)

    question = get_question(progression, hidden_element_index)
    correct_answer = progression[hidden_element_index]

    return question, correct_answer
