def get_user_data(first_name , last_name , email_address):
  print("Received the following user data: ",end="")
  return first_name, last_name, email_address
def main():
  f_name = str(input("What is your first name?: "))
  l_name = str(input("What is your last name?: "))
  email = str(input("What is your email address? "))
  print(get_user_data(f_name, l_name , email))
main()