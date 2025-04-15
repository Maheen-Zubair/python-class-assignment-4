def print_multiple(message, repeats):
  for i in range(repeats):
    print(message, end=" ")

def main():
  
  mes = input("Please type a message: ")
  rep = int(input("Enter a number of times to repeat your message: "))

  print_multiple(mes, rep)

main()