from brain_games.cli import get_user_name, get_user_answer


def game_engine(game_data, game_description):
    user_name = get_user_name()
    print(game_description())
    play_count = 3
    for i in range(play_count):
        [question, correct_answer] = game_data()
        print(f'Question: {question}')
        user_answer = get_user_answer()
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f'"{user_answer}" is a wrong answer ;(.'
                f' Correct answer is "{correct_answer}".')
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')
