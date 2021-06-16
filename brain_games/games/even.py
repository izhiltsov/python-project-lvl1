from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine


def description():
    description = 'Answer "yes" if the number is even, otherwise answer "no"'
    return description


def game_data():
    number = get_random_number()
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [question, correct_answer]


def run_even_game():
    game_engine(game_data, description)
