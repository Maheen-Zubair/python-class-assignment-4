import random  

def roll_dice():
    die1 = random.randint(1, 6) 
    die2 = random.randint(1, 6) 
    return die1, die2  

for roll in range(3):
    die1, die2 = roll_dice() 
    print(f"""Roll {roll + 1}:
     Die 1 = {die1},  Die 2 = {die2}
          """)