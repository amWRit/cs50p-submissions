import random
import sys

def main():

    while True:
        level = input("Level: ")
        if level.isdigit():
            level = int(level)
            if level > 0:
                n = random.randint(1, level)
                break

    while True:
            try:
                guess = input("Guess: ")
                if guess.isdigit():
                    guess = int(guess)
                    if guess == n:
                        print("Just right!")
                        sys.exit()
                    elif guess > n:
                        print("Too large!")
                    elif guess < n:
                        print("Too small!")
            except TypeError:
                print("")


main()