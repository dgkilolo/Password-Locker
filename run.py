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
  # print(f"Hello {visitors_name}.\n Do you have an account? \n  y - Yes \n  n - No \n  ex - exit")
  # visitor_response = input()
  while True:
    print(f"Hello {visitors_name}.\n Do you have an account? \n  y - Yes \n  n - No \n  ex - exit")
    visitor_response = input()
    if visitor_response == 'n':
      print("Create account")
      print("-"*17)
      print("Your username...")
      username = input()
      print("Your password...")
      password = input()    

      save_account(create_account(username, password)) #creates and save the new account
      print('\n')
      print(f"New account: {username}   password: {password} created.")
      print('\n')
      
    elif visitor_response == 'y':
      print("Sign into your account.")
      print('-'*10)
      print("Enter username...")
      yourUsername = input()      
      print("Enter password...")
      yourPassword = input()

      authenticated_password = user_authentication(yourUsername,yourPassword)
      if authenticated_password == yourPassword:
        print("You have logged in Well.")
      else:
        print("Invalid username or password.")
        continue
    elif visitor_response == 'ex':
      break

    else:
      print("Invalid input")
      

    while True:    
      print("What would you like to do?")
      print("Use the shortcodes provided: \n da - display applications \n cn - create new application password \n dl - delete credential \n fc - find \n ex - exit")
      short_code = input()
      print('\n')

      if short_code == 'cn':

        print("Auto generate password? \n y - Yes \n n - No ")
        auto_choice = input()

        if auto_choice == 'n':
          print("Application for which password is to be saved.")
          print('-'*10)
          print("New App Name...")
          appName = input()
          print("App password...")
          appPassword = input()

        elif auto_choice == 'y':
          print("Application for which password is to be saved.")
          print('-'*10)
          print("New App Name...")
          appName = input()
          print("App password...")
          appPassword = autogenerate_password()

        save_application(create_application(appName, appPassword)) #create new application name and create it's password
        print('\n')
        print(f"New Application: {appName}, password: {appPassword} is saved.")

        

      elif short_code == 'da':
        if display_credentials():
          print("Saved Credentials")
          print('--'*12)
          print("App:       Password:")
          for credential in display_credentials():
            print(f"{credential.application_name}    {credential.application_password} ")
          print('\n')
        else:
          print('\n')
          print("No credentials to display")
          print('\n')    
    
      elif short_code == 'dl':
        print("Enter the app name that you want to delete.")      
        deleteApp = input()
        found_credential = finding_credential(deleteApp)
        
        if finding_credential(deleteApp):
          delete_credentials(found_credential)
          print(f"Been deleted. {deleteApp} ")
        else:
          print("Not found.")
        

      elif short_code == 'fc':
        print("Enter the name of the app you are looking for.")
        searched_app = input()
        searched_credential = finding_credential(searched_app)
        print(f"We have found {searched_credential.application_name} {searched_credential.application_password} ")
        print('\n')


      elif short_code == 'ex':
        print("bye...")
        break   

      else:
        print("Invalid input.") 
            
     
       
if __name__ == "__main__":
  main()
