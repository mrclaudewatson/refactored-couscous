#UID: U72087839
#Name: Claude Watson
#Good ol' Guessing Game - Prompts the user to guess the correct value of a random number
#                         given 10 tries and a range between 1 and 100

import random

answer = random.randrange(1,101)
tries = 0
guess = int(input("Guess a number between 1 and 100:"))

while True:
    while guess < 1 or guess > 100:  # loop for invalid entry
        print("Invalid entry.", end="")
        guess = int(input(" Guess a number between 1 and 100:"))
    if guess < answer:
        tries += 1
        print("Too low, try again.", end="")
        guess = int(input(" Guess a number between 1 and 100:"))
    elif guess > answer:
        tries += 1
        print("Too high, try again.", end="")
        guess = int(input(" Guess a number between 1 and 100:"))
    if guess == answer:
        tries += 1
        print(f"Congrats! You guessed it right in {tries} tries!")
        break
    if tries == 9:
        print(f"You lose. The number was {answer}.", end="")
        break