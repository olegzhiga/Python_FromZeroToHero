# Guess the random number

import random

randomNumber = random.randint(1, 5)
userNumber = input("I made a number from 1 to 5, try to guess what is this number: ")
countAttempts = 1

while randomNumber != userNumber:
    userNumber = input("You didn't guess, try again: ")
    countAttempts += 1

print("Yes, you right!")
print(f"You guessed right on the {countAttempts} try")

