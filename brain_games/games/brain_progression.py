import random
import copy

DESCRIPTION = 'What number is missing in the progression?'


def round():
    """Function defines conditions of the brain-progression game."""

    # defines the first number of a progression.
    first_number = random.randint(1, 20)
    # defines a step of a progression.
    step = random.randint(1, 5)
    # progression = [str(first_number)]
    # defines length of a progression.
    length = random.randint(5, 10)
    progression = [str(first_number + step * i) for i in range(0, length)]
    index_hidden_element = random.randint(0, len(progression) - 1)
    new_progression = copy.deepcopy(progression)
    correct_answer = new_progression.pop(index_hidden_element)
    new_progression.insert(index_hidden_element, '..')
    question = ' '.join(new_progression)
    return question, correct_answer
