def find_average(a:float , b:float) -> float:
  
  sum:float = a + b
  return sum / 2

def main():
  
  avg_1 = find_average(0,10)
  avg_2 =find_average(8,10)
  final = find_average(avg_1, avg_2)

  print("Average 1: ", avg_1)
  print("Average 2: ", avg_2)
  print("Final Average: ", final)

main()