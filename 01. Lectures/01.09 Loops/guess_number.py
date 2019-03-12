'''
Created on Nov 2, 2017

@author: arusignu
'''

import random

MAX_TRIES = 7

print('''--- Welcome to Guess My Number ---

I\'m thinking of a number between 1 and 100.
Try to guess the number in %d'''% MAX_TRIES, end='')
if MAX_TRIES == 1:
    print(' attempt...')
else:
    print(' attempts...')

# Set the inital Values
number = random.randint(1,100)
tries = 1
guess = int(input('Enter guess %d: ' % tries))

# Guessing loop
while guess != number:
    if guess > number:
        print('    Lower...')
    else:
        print('    Higher...')
    tries += 1
    if tries > MAX_TRIES:
        break
    guess = int(input('Enter guess %d: ' % tries))
    
if tries <= MAX_TRIES:
    attempts = tries
    print('\nCongradulations! You correctly guessed the number %d, and it took you only %d' % (number, tries), end='')
else:
    attempts = MAX_TRIES
    print('\nSorry, you did not guess the number %d in %d' % (number, MAX_TRIES), end='')
if attempts == 1:
    print(' try!')
else:
    print(' tries!')