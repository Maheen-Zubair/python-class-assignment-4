def is_odd():
  for i in range(10):
    if i % 2 != 0:
      print(i , "odd" , end=" ")
    else:
      print(i, "even" , end=" ")
is_odd()