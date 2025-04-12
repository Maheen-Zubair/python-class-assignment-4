# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:
# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!
# You make a guess, saying your number is either higher than or lower than the computer's number
# f your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!
# These steps make up one round of the game. The game is over after all rounds have been played

import random

NUM_ROUNDS = 5

def high_low_game():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0

    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        computer_num: int = random.randint(1, 100)
        your_num: int = random.randint(1, 100)
        print("Your number is", your_num)

        choice: str = input("Do you think your number is higher or lower than the computer's?: ")

        higher_and_correct:bool=  choice == "higher" and your_num > computer_num
        lower_and_correct:bool=  choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        print("Your score is: ", your_score)
        print()

    print("Thanks for playing!")

high_low_game()