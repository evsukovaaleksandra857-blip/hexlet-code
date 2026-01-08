import random


def generate_question():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = 10

    # Генерируем прогрессию сразу в списке
    progression = [str(start + i * step) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    # Скрываем элемент
    progression[hidden_index] = ".."
    question = " ".join(progression)

    return question, correct_answer
