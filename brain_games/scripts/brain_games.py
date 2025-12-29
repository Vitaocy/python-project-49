from brain_games.cli import welcome_user
from brain_games.scripts.games.brain_calc import main as brain_calc
from brain_games.scripts.games.brain_even import main as brain_even
from brain_games.scripts.games.brain_gcd import main as brain_gcd
from brain_games.scripts.games.brain_prime import main as brain_prime


def main():
    name = welcome_user()
    brain_even(name)
    brain_calc(name)
    brain_gcd(name)
    brain_prime(name)

if __name__ == "__main__":
    main()