import random
import time

# Define the function PlayAgain() that asks whether the user wishes to play the game again.
def PlayAgain():
        time.sleep(0.7)
        print('Would you like to try again?')
        theAnswer = input()
        theAnswer = theAnswer.lower()
        if theAnswer ==  'yes':    
          GuessTheNumber()
        else:
          print('Ok then. See you later!')

print ('Hello, what is your name?')
myName = input() # User inputs his/her name.

print('It is good to meet you, ' + myName)
time.sleep(1) # Define the time delay (in this case, 1 second delay).

print('I am going to select a number between 1 and 20.')
time.sleep(2)

print('Then, you will have to find my number in 3 guesses to win the game.')
time.sleep(2)

# Define the function GuessTheNumber() that lets the user play the game.
def GuessTheNumber():
    print('Let me think...')
    time.sleep(2)

    # Randomly select a number between 1 and 20 
    number =  random.randint(1,20)
    print('Ok, got it.')
    time.sleep(0.5)

    guessesTaken = 0 # No guess made yet.

    while guessesTaken < 3:
        print('Take a guess.')
        guess = input() # User makes a guess.
        guess =int(guess)
        time.sleep(0.5)

        guessesTaken = guessesTaken + 1

        if guess < number: # If the guessed number is LOWER than the selected number...
            print('Your guess is too low. Try again.')
            time.sleep(0.5)

        if guess > number: # If the guessed number is HIGHER than the selected number...
            print('Your guess is too high. Try again.')
            time.sleep(0.5)

        if guess == number: # If the guessed number is EQUAL to the selected number...
            break

    if guess == number: # If the user SUCCESSFULLY finds the number in three guesses...
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '. You got it in ' + guessesTaken + ' guesses.')
        PlayAgain()

    if guess != number: # If the user CANNOT find the number in at least three guesses...
        number = str(number)
        print('Too bad, ' + myName + '. The number I selected was ' + number + '.')
        PlayAgain()

GuessTheNumber()
                   
