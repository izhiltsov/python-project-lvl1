from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine


def description():
    description = 'What is the result of the expression?'
    return description


def game_data():
    max_mumber = 10  # for esy playing
    num1 = get_random_number(max_mumber)
    num2 = get_random_number(max_mumber)

    operands = ['*', '+', '-']
    random_index = get_random_number(len(operands))
    operand = operands[random_index]

    question = f'{num1} {operand} {num2}'
    correct_answer = str(calculator(num1, num2, operand))

    return [question, correct_answer]


def calculator(num1, num2, operand):
    switcher = {
        '+': num1 + num2,
        '*': num1 * num2,
        '-': num1 - num2,
    }

    return switcher.get(operand, f'Error! Unknown operand state: {operand}!')


def run_calc_game():
    game_engine(game_data, description)
