from passwordLocker import User
from passwordLocker import Credentials

def create_account(user_name, user_password):
  '''
  Function to create a new account.
  '''
  new_account = User(user_name, user_password)
  return new_account

def create_application(application_name, application_password):
  '''
  Function to create new application for which password is required.
  '''
  new_application = Credentials(application_name, application_password)
  return new_application

def save_account(account):
  '''
  Function to save a new account.
  '''
  account.append_account()

def save_application(app):
  '''
  Function to save a new applications name and password.
  '''
  app.append_application()

def display_credentials():
  '''
  Function that displays saved credentials.
  '''
  return Credentials.display_applications()

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
  print('/n')

  while True:
    print("What would you like to do?")
    print("Use the shortcodes provided:  da - display applications  cn - create new application password")
    short_code = input()

    if short_code == 'cn':
      print("Application for which password is to be saved.")
      print('-'*10)
      print("New App Name...")
      appName = input()
      print("App password...")
      appPassword = input()

      save_application(create_application(appName, appPassword)) #create new application name and create it's password
      print('/n')
      print(f"New Application: {appName}, password: {appPassword} is saved.")

    elif short_code == 'da':
      if display_credentials():
        print("A list of your saved credentials")
        print('-'*10)
        print("App:       Password:")
        for credential in display_credentials():
          print(f"{credential.app}    {credential.passwordApp} ")
        print('/n')
      else:
        print('/n')
        print("No credentials to display")
        print('/n')





if __name__ == "__main__":
  main()
