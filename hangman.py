import time

name = input('What\'s your name: ')
print('Hello, '+ name, 'Time to play HangMan')

time.sleep(1)
print('Start Guessing')
time.sleep(0.5)


word = 'secret' # this is where you put the word.
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_',)
            failed +=1

    if failed == 0:
        print('You won')
        break

    else:
        guess = input('Guess a Character: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('Wrong')
            print('You have',+ turns,'more  guesses')

            if turns == 0:
                print('You Loose')
