from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine


def description():
    descr = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return descr


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    if num > 1:
        return True


def game_data():
    number = get_random_number()
    question = str(number)

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return [question, correct_answer]


def run_prime_game():
    game_engine(game_data, description)
