import os
import random

os.system("cls")


def printSymbol(n):
    if n == 1:
        return "rock"
    if n == 2:
        return "paper"
    if n == 3:
        return "scissor"


def play():
    os.system("cls")
    computer = random.randint(1, 3)
    user = input("Enter choice: (1=rock, 2=paper, 3=scissor): ")
    user = int(user)
    print("computer choice =", printSymbol(computer))
    print("User choice =", printSymbol(user))
    if (computer == user):
        print("Match Draw!")
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        print("You Won!")
    else:
        print("Computer Won!")


play()
