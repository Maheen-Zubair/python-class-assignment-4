import random

DONE_LIKELIHOOD = 0.5

def chaotic_counting():
    for i in range(10):
        num = i + 1
        if done():
            return
        print(num)

def done():
    if random.random() < DONE_LIKELIHOOD: #50% chance h ke counting rukh jae
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

main()