from random import randint
import os


def roller():
    print('The Dice is rolled. You got: ',randint(1,6))

print("Welcome to the Dice Simulation app:")
repeat = input('Enter Y or N to roll the dice: ').lower()

while repeat == 'y':
    roller()
    repeat = input('Do you want to roll again? Enter Y or N: ').lower()

    if repeat == 'n':
        print('Quiting')
        break
