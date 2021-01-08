import random
from brain_games.games import engine


def run_brain_progression():
    """Function defines conditions of the brain-progression game."""

    def get_correct_answer(question):
        """Function defines the correct_answer."""

        progression_list = question.split(' ')
        # index of the hidden element.
        index_number = progression_list.index('..')
        # for the case if the first element was hidden.
        if index_number == 0:
            correct_answer = int(int(progression_list[1])
                                 - (int(progression_list[2])
                                 - int(progression_list[1])))
        # for the case if the last element was hidden.
        elif index_number == len(progression_list) - 1:
            correct_answer = int(int(progression_list[-2])
                                 - int(progression_list[-3])
                                 + int(progression_list[-2]))
        else:
            pr_index = index_number - 1  # index of the previous element.
            nx_index = index_number + 1  # index of the next element.
            correct_answer = int((int(progression_list[nx_index]) -
                                  int(progression_list[pr_index])) / 2
                                 + int(progression_list[pr_index]))
        return str(correct_answer)

    def randomizer():
        """Function returns a progression with a hidden element in string."""

        # defines the first number of a progression.
        first_number = random.randint(1, 20)
        # defines a step of a progression.
        step = random.randint(1, 5)
        progression_list = [str(first_number)]
        # defines length of a progression.
        limit = random.randint(5, 10)
        for i in range(1, limit):
            number = first_number + step * i
            progression_list.append(str(number))
        index_hidden_element = random.randint(0, len(progression_list) - 1)
        progression_list.pop(index_hidden_element)
        progression_list.insert(index_hidden_element, '..')
        progression_string = ' '.join(progression_list)
        return progression_string

    string = 'What number is missing in the progression?'
    engine.run_engine(get_correct_answer, randomizer, string)
