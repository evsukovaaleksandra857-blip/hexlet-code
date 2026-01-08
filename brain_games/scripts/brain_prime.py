from brain_games.engine import run_game
from brain_games.games.brain_prime import generate_question


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_question, description)


if __name__ == "__main__":
    main()
