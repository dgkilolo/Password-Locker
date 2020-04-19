from passwordLocker import User

def create_account(user_name, user_password):
  '''
  Function to create a new account.
  '''
  new_account = User(user_name, user_password)
  return new_account

def save_account(account):
  '''
  Function to save a new account.
  '''
  account.append_account()

def main():
  print("Welcome to Password Locker")
  print("Enter your name")
  visitors_name = input()
  print(f"Hello {visitors_name}. Do you have an account?")
  print('/n')

  print("Create account")
  print("-"*11)
  print("Your username...")
  username = input()
  print("Your password...")
  password = input()

  save_account(create_account(username, password)) #creates and save the new account
  print('/n')
  print(f"New account {username} {password} created.")


if __name__ == "__main__":
  main()
