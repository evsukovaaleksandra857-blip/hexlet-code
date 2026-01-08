from brain_games.engine import run_game
from brain_games.games.brain_progression import generate_question


def main():
    description = "What number is missing in the progression?"
    run_game(generate_question, description)


if __name__ == "__main__":
    main()
