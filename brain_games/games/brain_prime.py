import random


def is_prime(n):
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2  # True только для 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def generate_question():
    """Возвращает (вопрос, правильный_ответ)."""
    number = random.randint(2, 100)
    return str(number), "yes" if is_prime(number) else "no"
