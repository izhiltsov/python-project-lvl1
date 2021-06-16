from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine


description = 'Answer "yes" if the number is even, otherwise answer "no"'


def game_data():
    random_number = get_random_number()
    question = str(random_number)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [question, correct_answer]


def run_even_game():
    game_engine(game_data, description)
