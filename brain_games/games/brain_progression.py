import random


DESCRIPTION = 'What number is missing in the progression?'
GAP = '..'
MIN_LENGTH = 5
MAX_LENGTH = 10


def get_progression(start, step, length):
    progression = [start + step * i for i in range(length)]
    return progression


def get_question(progression, hidden_element_index, hiding_marker):
    copied_progression = progression[:]
    modified_progression = list(map(str, copied_progression))
    modified_progression[hidden_element_index] = hiding_marker
    question = ' '.join(modified_progression)
    return question


def generate_round():
    """Function defines conditions of the brain-progression game."""
    progression_start = random.randint(1, 20)
    progression_step = random.randint(1, 5)
    progression_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = get_progression(progression_start,
                                  progression_step,
                                  progression_length)
    hidden_element_index = random.randint(0, len(progression) - 1)
    question = get_question(progression, hidden_element_index, GAP)
    correct_answer = str(progression[hidden_element_index])
    return question, correct_answer
