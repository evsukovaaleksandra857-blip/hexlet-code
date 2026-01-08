from brain_games.engine import run_game
from brain_games.games.brain_even import generate_question


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_question, description)


if __name__ == "__main__":
    main()
