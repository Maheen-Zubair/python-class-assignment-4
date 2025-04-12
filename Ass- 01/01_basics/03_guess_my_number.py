# Problem Statement
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

def guess_the_number():
    secret_number: int = 26
    
    print("I am thinking of a number between 1 and 99...")
    
    guess = int(input("Enter a guess: "))
    while guess != secret_number:
        if guess < secret_number:  
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() 
        guess: int = int(input("Enter a new guess: ")) 
        
    print("Congrats! The number was: " + str(secret_number))
    
guess_the_number()

