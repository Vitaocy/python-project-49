from brain_games.cli import welcome_user
from random import randint, choice


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        operator = choice(['+', '-', '*'])
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        if operator == '+':
            correct_answer = num_1 + num_2
        if operator == '-':
            if num_1 < num_2:
                num_1, num_2 = num_2, num_1
            correct_answer = num_1 - num_2
        if operator == '*':
            num_1 = (num_1 % 20) + 1
            num_2 = (num_2 % 20) + 1
            correct_answer = num_1 * num_2
        print(f'Question: {num_1} {operator} {num_2}') 
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')