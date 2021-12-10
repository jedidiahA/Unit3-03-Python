#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Dec 7, 2021
# This program guesses a number between 1 and 10.
import random


def main():
    hidden = random.randint(1, 10)
    # a number between 1 and 10
    # print hidden

    guess = int(input("Guess a number between 1 and 10 :"))

    if guess == hidden:
        print("you guessed right")

    if guess != hidden:
        print("you guessed wrong")
        print("The correct answer is")
        print(hidden)


if __name__ == "__main__":
    main()
