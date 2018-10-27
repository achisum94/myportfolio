# this is a guess the number game
import random

print('hello wat is your name')
name = input()

print('well, ' + name + ', i am thinking for a number between 1 and 20' )
secretNumber = random.randint(1,20)

for guessesTaken in range(1, 7):
    print ('take a guess')
    guess = int(input())
    
    if guess < secretNumber:
        print ('your guess is to low')
    elif guess > secretNumber:
        print ('your guess is too high')
    else:
        break # this codition is for the correct guess

if guess == secretNumber:
    print('good job, ' + name + '! you guessed my number in' + str(guessesTaken) + ' guesses')
else:
    print('nope. the number i was thinking of was ' + str(secretNumber))
    
    
        


