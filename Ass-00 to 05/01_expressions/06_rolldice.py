import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"Die 1 rolled: {die1}")
    print(f"Die 2 rolled: {die2}")
    print(f"Total of both dice: {total}")

roll_dice()