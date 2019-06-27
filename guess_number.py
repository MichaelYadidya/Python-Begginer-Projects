import random

start_guess = input('Enter Y or N to proceed accordingly: ').lower()
range_estimator = int(input('Enter the range: '))

while start_guess == 'y':
    generator = random.randint(0,range_estimator)
    guessor = int(input('Enter your guess:  \n'))


    if generator == guessor:
        print('You guessed right.The number is: ',generator)
        break

    elif guessor > generator:
        print('You are off by round: ',guessor - generator)

    elif guessor < generator:
        print('You are off by round: ',generator - guessor)
