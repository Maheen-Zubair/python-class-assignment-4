def count_even(lst):
  even_count = 0
  for i in lst:
    if i % 2 == 0:
      even_count += 1
  return even_count

def main():
  user_input = []
  while True:
    asked = input("Enter an integer or press enter to stop: ")
    if asked == "":
      break 
    user_input.append(int(asked)) 
    
  result = count_even(user_input)
  print("Number of even numbers:", result)

main()