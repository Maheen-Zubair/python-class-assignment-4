def enter_valid_number():
  while True:
    try:
      feet = float(input("Please enter the length in feet: "))
      return feet
    except ValueError:
      print("please enter a valid number!")

def convert_feet_to_inches():
    feet = enter_valid_number()
    inches = feet * 12
    print(f"The equivalent length in inches is: {inches} inches")

convert_feet_to_inches()