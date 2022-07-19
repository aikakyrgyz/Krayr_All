# import random
from random import randint

MAX = 5

name = input('Welcome.\n Please enter your name! ')

while True:
    guessed = False
    num_tries = 0

    choice = input('Would you want to play [yes] or [no]?: ')  # NO, nO, No
    if choice.lower() == 'no': #ignore the case of letters
        print('You chose not to play, exiting ...')
        break
    # continue with the game
    while choice != 'yes' and choice != 'no':
        choice = input('Please enter [yes] or [no]')
    range_ = input('Choose the range, example [0-50]: ').split('-')
    # '0-50'
    # '0-50'.split('-')
    # 0-50-70-80.split('-') -> [0, 50, 70, 80]
    # [0, 50]
    # randint(range_[0], range_[1]) -> randint(0, 50) -> returns a random an integer
    # split -> list -> 0-50 -> [0, 50]
    # type casting to an int
    # the secret number is going to be within range 0-50
    secret_num = randint(int(range_[0]), int(range_[1])) # randint(start, end)
    print(f'You will have to guess a number between {int(range_[0])} and {int(range_[1])}')
    while not guessed:
        user_num = int(input('Enter your guess: '))
        num_tries += 1
        if user_num == secret_num:
            print(f'Congrats, {name.title()}')
            print(f'You needed just {num_tries} tries to guess the number. Yes, it was {secret_num}. Bye')
            break
        elif user_num > int(range_[1]) or user_num < int(range_[0]):
            print('Your number is out of range')
            print(f'You will have to guess a number between {int(range_[0])} and {int(range_[1])}')
            continue
        else:
            print('Oh, your guess was wrong!')
            if num_tries > MAX:
                hint = input('Would you like a hint? [yes] or [no]: ')
                if hint.lower() == 'yes':
                    if user_num - secret_num > 0:
                        print(f'The secret number is lower than {user_num}')
                    else:
                        print(f'The secret number is higher than {user_num}')







