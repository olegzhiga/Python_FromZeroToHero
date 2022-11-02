import random

flag = False
while flag is False:
    randomNum = random.randint(1, 5)
    inputNum = int(input("Your choice form 1 for 5: "))
    if inputNum == randomNum:
        flag = True
        break

print(f"Yes, it is {randomNum}. You are right!")
