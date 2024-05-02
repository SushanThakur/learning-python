import os
import random

os.system("cls")


def play():
    os.system("cls")
    guess = input("Guess a number: (1-10): ")
    guess = int(guess)
    x = random.randint(1, 10)

    if (guess == x):
        print("You guessed it right")
    else:
        print("Your guess was incorrect")
        print("correct guess was", x)

    t = input("continue? (y/n): ")
    if t == 'y':
        play()
    else:
        return


play()
