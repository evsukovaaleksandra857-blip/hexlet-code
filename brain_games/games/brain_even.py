import random


def is_even(number):
    """Проверяет, чётное ли число."""
    return number % 2 == 0


def generate_question():
    """Возвращает (вопрос, правильный ответ)."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
