import random
import sys

guess = 0
guesscount = 1
#main
rnge = int(input("The number will be random between 1 and ? : "))
SecretNumber = random.randint(1, rnge) #decide randome int range
guesses = int(input("How many guesses would you like to take?: "))


while int(guess) != SecretNumber:
    if guesscount <= guesses:
        guess = input("Guess a number between 1-" + str(rnge) + ", you have " + str(guesses) + " guesses: ")
        guesscount = guesscount + 1
    elif guesscount > 6:
        print("You Lose :(")
        sys.exit(0)
print("You did it!")
