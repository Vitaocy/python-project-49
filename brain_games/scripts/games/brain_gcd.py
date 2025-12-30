from brain_games.cli import welcome_user
from random import randint


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    for _ in range(3):
        base_gcd = randint(2, 10)
        num1 = base_gcd * randint(2, 12)
        num2 = base_gcd * randint(2, 12)
        
        correct_answer = gcd(num1, num2)

        print(f'Question: {num1} {num2}')
        
        user_input = input('Your answer: ')

        if int(user_input) == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
