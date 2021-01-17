import random
from brain_games import engine


def run():
    """Function defines conditions of the brain-progression game."""

    def randomize_progression():
        """Function returns a progression with a hidden element in string."""

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
        progression_list.pop(index_hidden_element)
        progression_list.insert(index_hidden_element, '..')
        progression_string = ' '.join(progression_list)
        return progression_string

    def find_hidden_element(generated_question):
        """Function finds the hidden element."""

        progression_list = generated_question.split(' ')
        # find index of the hidden element.
        index_number = progression_list.index('..')
        # for the case if the first element was hidden.
        if index_number == 0:
            hidden_element = int(int(progression_list[1])
                                 - (int(progression_list[2])
                                 - int(progression_list[1])))
        # for the case if the last element was hidden.
        elif index_number == len(progression_list) - 1:
            hidden_element = int(int(progression_list[-2])
                                 - int(progression_list[-3])
                                 + int(progression_list[-2]))
        else:
            previous_index = index_number - 1  # index of the previous element.
            next_index = index_number + 1  # index of the next element.
            hidden_element = int((int(progression_list[next_index]) -
                                  int(progression_list[previous_index])) / 2
                                 + int(progression_list[previous_index]))
        return str(hidden_element)

    game_task = 'What number is missing in the progression?'
    engine.run_engine(find_hidden_element, randomize_progression, game_task)
