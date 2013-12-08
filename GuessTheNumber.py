# This is a guessing game.
import random
import time

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
myName = input()
print('It is good to meet you, ' + myName)
time.sleep(1)
print('I am going to think a number between 1 and 20.')
time.sleep(2)
print('Then, you will have to find my number in 3 guesses to win the game.')
time.sleep(2)
def GuessTheNumber():
    print('Let me think...')
    time.sleep(2)
    number =  random.randint(1,20)
    print('Ok, got it.')
    time.sleep(0.5)
    guessesTaken = 0
    while guessesTaken < 3:
        print('Take a guess.')
        guess = input()
        guess =int(guess)
        time.sleep(0.5)
        guessesTaken = guessesTaken + 1

        if guess < number:
            print('Your guess is too low. Try again.')
            time.sleep(0.5)

        if guess > number:
            print('Your guess is too high. Try again.')
            time.sleep(0.5)

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '. You got it in ' + guessesTaken + ' guesses.')
        PlayAgain()
    if guess != number:
        number = str(number)
        print('Too bad, ' + myName + '. I was thinking of ' + number + '.')
        PlayAgain()
GuessTheNumber()
                   
