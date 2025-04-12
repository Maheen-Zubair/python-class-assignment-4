# Problem Statement
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

import random

def guess_my_number():
    print("I am thinking of a number between 0 and 99...")

    computer_number = random.randint(0, 99)

    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess > computer_number:
            print("Your guess is too high")
            print("")
        elif user_guess < computer_number:
            print("Your guess is too low")
            print("")
        else:
            print(f"Congrats! The number was: {computer_number}")
            print("")
            break

guess_my_number()
