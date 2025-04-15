pear = 1000
lychee = 50
mango = 8
apple = 12
banana = 4

def num_in_stock(fruit):
  if fruit == "pear":
    print("This fruit is in stock! Here is how many:",pear)
  elif fruit == "lychee":
    print("This fruit is in stock! Here is how many:",lychee)
  elif fruit == "mango":
    print("This fruit is in stock! Here is how many:",mango)
  elif fruit == "apple":
    print("This fruit is in stock! Here is how many:",apple)
  elif fruit == "banana":
    print("This fruit is in stock! Here is how many:",banana)
  else:
    print("This fruit is not in stock.")

def main():
  fruit = input("Enter a fruit: ")
  num_in_stock(fruit)
main()