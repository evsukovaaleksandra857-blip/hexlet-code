from brain_games.engine import run_game
from brain_games.games.brain_gcd import generate_question


def main():
    description = "Find the greatest common divisor of given numbers."
    run_game(generate_question, description)


if __name__ == "__main__":
    main()
