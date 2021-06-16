from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine


def description():
    description = 'Find the greatest common divisor of given numbers.'
    return description


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def game_data():
    max_mumber = 10  # for esy playing
    num1 = get_random_number(max_mumber)
    num2 = get_random_number(max_mumber)

    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))

    return [question, correct_answer]


def run_gcd_game():
    game_engine(game_data, description)
