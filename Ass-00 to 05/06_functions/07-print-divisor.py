def print_divisors(num: int) -> int:
  print("Here are the divisors of" ,num, "is" , end=" " )

  for i in range(num):
    val = i + 1

    if num % val == 0:
      print(val , end=" ")

def main():
  num = int(input("Enter a number: "))
  print_divisors(num)
main()