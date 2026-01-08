from brain_games.engine import run_game
from brain_games.games.brain_calc import generate_question


def main():
    description = "What is the result of the expression?"
    run_game(generate_question, description)


if __name__ == "__main__":
    main()
