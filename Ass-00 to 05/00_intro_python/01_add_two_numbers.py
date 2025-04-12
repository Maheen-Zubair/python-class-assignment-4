# Problem Statement
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.


def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError: 
            print("Please enter a valid number.")

def sum():
    number1 = get_valid_number("Enter the first number: ")
    number2 = get_valid_number("Enter the second number: ")
    return number1 + number2  

print("The sum is:", sum())
