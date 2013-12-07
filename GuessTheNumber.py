# This is a guess number game.
import random

guessesTaken = 0

print ('Hello, what is your name?')
myName = input()
print('It is good to meet you, ' + myName + '. Let me think a number between 1 and 20.')

number =  random.randint(1,20)
print('Ok, got it. Find my number in 3 guesses.')

while guessesTaken < 3:
    print('Take a guess.')
    guess = input()
    guess =int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low. Try again.')

    if guess > number:
        print('Your guess is too high. Try again.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '. You got it in ' + guessesTaken + ' guesses.')

if guess != number:
    number = str(number)
    print('Too bad, ' + myName + '. I was thinking of ' + number + '.')