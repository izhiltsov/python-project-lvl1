from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine


def description():
    description = 'What number is missing in the progression?'
    return description


def make_progression(length, step):
    progression = []
    member = get_random_number(10)
    for i in range(length):
        progression.append(str(member))
        member += step
    return progression


def game_data():
    progression_length = 10  # for esy playing
    step = get_random_number(10)  # for not too big steps
    progression = make_progression(progression_length, step)
    random_index = get_random_number(progression_length - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)

    return [question, correct_answer]


def run_progression_game():
    game_engine(game_data, description)
