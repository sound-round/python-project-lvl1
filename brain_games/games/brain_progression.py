import random


DESCRIPTION = 'What number is missing in the progression?'


def run():
    """Function defines conditions of the brain-progression game."""

    # defines the first number of a progression.
    first_number = random.randint(1, 20)
    # defines a step of a progression.
    step = random.randint(1, 5)
    progression_list = [str(first_number)]
    # defines length of a progression.
    length = random.randint(5, 10)
    for i in range(1, length):
        next_number = first_number + step * i
        progression_list.append(str(next_number))
    index_hidden_element = random.randint(0, len(progression_list) - 1)
    correct_answer = progression_list.pop(index_hidden_element)
    progression_list.insert(index_hidden_element, '..')
    question = ' '.join(progression_list)
    return question, correct_answer
