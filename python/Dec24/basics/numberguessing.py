"""
number guessing.py

This module contians the number guessing game
"""

import random

def start_game():
    min = 1
    max = 10
    max_guess_count = 3
    random_number = random.randint(min, max)
    guessed = False
    for guess_count in range(max_guess_count):
        guessed_number = int(
            input(f"Enter any number of your choice in range of {min} to {max}: ")
        )
        if guessed_number == random_number:
            print("Wonderful you have guessed correctly")
            guessed = True
            break
        elif guessed_number < random_number:
            print("you are close think a little bit upwards")
        elif guessed_number > random_number:
            print("you are close think a little bit downwards")
    if not guessed:
        print("you have lost, Better luck next time")

if __name__ == '__main__':
    # if this module is executed
    start_game()
