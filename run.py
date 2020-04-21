import random
import string
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

def delete_credentials(theApp):
  '''
  Function that deletes credentials.
  '''
  return Credentials.delete_credential(theApp)

def finding_credential(namez):
  return Credentials.find_credential(namez)

def find_users(user):
  return User.users_list(user)

def user_authentication (username, password):
  '''
  Function to authenticate users.
  '''
  return User.username_authentication(username,password)

def autogenerate_password():
  '''
  Generate a random password for the application.
  '''
  characater_pool = string.ascii_letters + string.digits
  return "".join((random.choice(characater_pool) for i in range(8))) 

def main():
  print("Welcome to PASSWORD LOCKER")
  print('--'*15)
  print("Enter your name...")
  visitors_name = input()  
  while True:
    print(f"Hello {visitors_name}.\n \n Do you have an account? \n  y - Yes \n  n - No \n  ex - exit")
    visitor_response = input()
    print('\n')
    if visitor_response == 'n':
      print("Create account")
      print("-"*17)
      print("Your username...")
      username = input()
      print("Your password...")
      password = input()    

      save_account(create_account(username, password)) #creates and save the new account
      print('\n')
      print('-'*3)
      print(f"New account: {username}   password: {password} created.")
      print('-'*3)
      print('\n')
      
    elif visitor_response == 'y':
      print("Sign into your account.")
      print('--'*12)
      print("Enter username...")
      yourUsername = input()      
      print("Enter password...")
      yourPassword = input()

      authenticated_password = user_authentication(yourUsername,yourPassword)
      if authenticated_password == yourPassword:
        print('\n')
        print('-'*3)
        print("Successfully Logged In.")
        print(f"Welcome, {yourUsername}.")
        print('-'*3)
        print('\n')
      else:
        print('\n')
        print('*'*3)
        print("Invalid username or password.")
        print('*'*3)
        print('\n')
        continue
    elif visitor_response == 'ex':
      print("See you later :)")
      break

    else:
      print('*'*3)
      print("Invalid input")
      print('*'*3)
      print('\n')
      continue      

    while True:       
      print("What would you like to do?")
      print("Use the shortcodes provided: \n da - display applications \n cn - create new application password \n dl - delete credential \n fc - find \n ex - exit")
      short_code = input()
      print('\n')

      if short_code == 'cn':

        print("Auto generate password? \n y - Yes \n n - No ")
        auto_choice = input()

        if auto_choice == 'n':
          print("Credentials to be Saved.")
          print('-'*10)
          print("New App Name...")
          appName = input()
          print("App password...")
          appPassword = input()

        elif auto_choice == 'y':
          print('\n')
          print("Credentials to be Saved. :auto")
          print('-'*10)
          print("New App Name...")
          appName = input()
          print("App password...")
          appPassword = autogenerate_password()

        else:
          print('\n')
          print('*'*3)
          print("Invalid Input")
          print('*'*3)
          print('\n')
          continue

        save_application(create_application(appName, appPassword)) #create new application name and create it's password
        print('\n')
        print('-'*3)
        print(f"New Application: {appName}, password: {appPassword} is saved.")
        print('-'*3)
        print('\n')        

      elif short_code == 'da':
        if display_credentials():
          print("Saved Credentials")
          print('--'*9)
          print("App:       Password:")
          for credential in display_credentials():
            print(f"{credential.application_name}    {credential.application_password} ")
          print('\n')
        else:
          print('*'*3)
          print("No credentials to display")
          print('*'*3)
          print('\n')    
    
      elif short_code == 'dl':
        print("Enter the app name that you want to delete.")      
        deleteApp = input()
        found_credential = finding_credential(deleteApp)
        
        if finding_credential(deleteApp):
          delete_credentials(found_credential)
          print('\n')
          print('-'*3)
          print(f"{deleteApp} has been Deleted. ")
          print('-'*3)
          print('\n')
        else:
          print('\n')
          print('*'*3)
          print(f" {deleteApp}; Not found.")
          print('*'*3)
          print('\n')

      elif short_code == 'fc':
        print("Enter the name of the app you are looking for.")
        searched_app = input()
        searched_credential = finding_credential(searched_app)

        if finding_credential(searched_app):
          print('\n')
          print('-'*3)
          print(f"We have found   {searched_credential.application_name} : {searched_credential.application_password} ")
          print('-'*3)
          print('\n')
        else:
          print('\n')
          print('*'*3)
          print(f" {searched_app} Not Found. ")
          print('*'*3)
          print('\n')       

      elif short_code == 'ex':
        print(f"See you later {username}")
        print('--'*13)
        print('\n')
        break   

      else:
        print('*'*3)
        print("Invalid input.") 
        print('*'*3)
        print('\n')                
       
if __name__ == "__main__":
  main()
