import prompt


def run_game(game_logic, description):
    """
    Запускает игру.

    :param game_logic: функция, возвращающая (вопрос, правильный_ответ)
    :param description: описание игры (например, правило)
    """
    from brain_games.cli import welcome_user  # получаем имя

    name = welcome_user()
    print(description)

    for _ in range(3):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
