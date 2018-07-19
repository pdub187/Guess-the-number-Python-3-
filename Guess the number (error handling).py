print('What is your name?') # asks the user their name
name = input() # assigns the entered name to the input 'name'

import random # imports the random library
secretnumber = random.randint(1,20) # sets secretnumber as a value

print('Hi there, ' + name + '. I just picked a number between 1 and 20. See if you can guess what it is.')

for guessestaken in range(1,6): # sets 5 as the maximum number of guesses
    while True: # starts a loop that will continue to ask the user to input a number until they enter a numerical value
        try:
            guess=int(input())
        except ValueError: # handles the error that arises from inputting a string value
            print("Please enter a numerical value")
        else:
            break # causes the program to exit the loop if a number was enter
    if guess > 20: #checks that the number was within the specified range
        print('Are you fucking dense?')
    elif guess > secretnumber: 
        print('That is too high. Guess again.')
    elif guess < secretnumber:
        print('That is too low. Guess again.')
    else: 
        break # breaks the program out of the for loop. There are now two scenarios possible.

if guess == secretnumber: # prints if the user has correctly guessed the number
    print('Congratulations, ' + name + ' You guessed correctly with only ' + str(guessestaken) + ' attempts!!!')
else: #prints if the user did not guess the number
    print('Sorry. You have run out of guesses.')
