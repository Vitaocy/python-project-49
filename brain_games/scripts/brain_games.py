from brain_games.cli import welcome_user
from brain_games.scripts.games.brain_even import main as brain_even
from brain_games.scripts.games.brain_calc import main as brain_calc


def main():
    name = welcome_user()
    brain_even(name)
    brain_calc(name)
    brain_gcd(name)


if __name__ == "__main__":
    main()