data = {"apple": 10, "durian": 12, "jackfruit": 20, "kiwi": 13, "rambutan":21, "mango":16}

def check():
  apples = int(input(f"How many (apple) do you want?: "))
  durians = int(input(f"How many (durian) do you want?: "))
  jackfruits = int(input(f"How many (jackfruit) do you want?: "))
  kiwis = int(input(f"How many (kiwi) do you want?: "))
  rambutans = int(input(f"How many (rambutan) do you want?: "))
  mangoes = int(input(f"How many (mango) do you want?: "))
  total = apples * data["apple"] + durians*data["durian"] +jackfruits*data["jackfruit"] + kiwis*data["kiwi"] + rambutans*data["rambutan"] + mangoes*data["mango"]
  print("Your Total is: ", total)
check()