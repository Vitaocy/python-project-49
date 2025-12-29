from brain_games.cli import welcome_user
from random import randint, choice


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    for _ in range(3):
        start = randint(1, 20)
        step = randint(1, 10)
        length = randint(5, 10)
        hidden_index = randint(0, length - 1)

        progression = [str(start + step * i) for i in range(length)]
        correct_answer = progression[hidden_index]
        progression[hidden_index] = '..'

        print(f'Question: {" ".join(progression)}')
        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
