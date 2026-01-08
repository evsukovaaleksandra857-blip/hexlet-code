import random


def generate_question():
    """
    Генерирует случайное математическое выражение и возвращает
    (вопрос, правильный_ответ_в_виде_строки).
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    # Вычисляем правильный ответ
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2

    question = f"{num1} {operator} {num2}"
    return question, str(correct_answer)
