from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import main as brain_even_main
from brain_games.scripts.brain_calc import main as brain_calc_main


def main():
    name = welcome_user()
    brain_even_main(name)
    brain_calc_main(name)


if __name__ == "__main__":
    main()