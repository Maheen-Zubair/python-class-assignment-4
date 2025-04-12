import math

def enter_valid_number():
  while True:
    try:
     ab :float= float(input("Enter the AB length: "))
     ac:float = float(input("Enter the AC length: "))
     return ab,ac    
    except ValueError:
      print("please enter a valid number!")

def calculate_hypotenuse():
    ab,ac = enter_valid_number()
    
    bc= math.sqrt(ab**2 + ac**2)
    print(f"The length of the BC(hypotenuse) is: {bc}")

calculate_hypotenuse()