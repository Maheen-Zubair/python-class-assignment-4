c = 299792458
def enter_valid_number():
  while True:
    try:
      mass = float(input("Enter kilos of mass: "))
      return mass
    except ValueError:
      print("please enter a valid number!")

def conversion():
  m = enter_valid_number()
  E = m * c**2
  print(f"\nm = {m} kg")
  print(f"C = {c} m/s")
  print(f"{E} joules of energy!")
conversion()