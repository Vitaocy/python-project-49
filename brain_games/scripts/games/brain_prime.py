from brain_games.cli import welcome_user
from random import randint


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if number < 2:
            correct_answer = 'no'
        else:
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    correct_answer = 'no'
                    break
            else:
                correct_answer = 'yes'
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')