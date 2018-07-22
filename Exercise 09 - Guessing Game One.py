"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed
too low, too high, or exactly right. (Hint: remember to use the user
input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game
ends, print this out.
"""

import random

rand = random.randint(1, 9)
print('Guess the number:\n')
count = 1
guess = 0

while guess is not '' and int(guess) is not rand:
    guess = input()
    if guess == '':
        break
    else:
        guess = int(guess)
    if int(guess) > rand:
        print('Guess is too high. Guess again or press enter to quit.\n')
        count += 1
    elif int(guess) < rand:
        print('Guess is too low. Guess again or press enter to quit.\n')
        count += 1
    else:
        print('You got it! It took you ' + str(count) + ' tries!')

if guess is '':
    print('You gave up!')
