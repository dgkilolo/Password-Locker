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
 

def main():
  print("Welcome to Password Locker")
  print("Enter your name")
  visitors_name = input()
  print(f"Hello {visitors_name}. Do you have an account?   y - Yes   n - No")
  visitor_response = input()
  while True:
    if visitor_response == 'n':
      print("Create account")
      print("-"*11)
      print("Your username...")
      username = input()
      print("Your password...")
      password = input()    

      save_account(create_account(username, password)) #creates and save the new account
      print('/n')
      print(f"New account: {username}   password: {password} created.")
      print('/n')
      break
    elif visitor_response == 'y':
      print("Sign into your account.")
      print('-'*10)
      print("Enter username...")
      yourUsername = input()
      print("Enter password...")
      yourPassword = input()

      if yourUsername == User.users_list:
        break
      elif yourUsername != User.users_list:
        print("Enter a valid username.")
      

  while True:
    print(f"Welcome {username}.")
    print("What would you like to do?")
    print("Use the shortcodes provided:  da - display applications  cn - create new application password  dl - delete credential   fc - find   ex - exit")
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
          print(f"{credential.application_name}    {credential.passwordApp} ")
        print('/n')
      else:
        print('/n')
        print("No credentials to display")
        print('/n')    
  
    elif short_code == 'dl':
      print("Enter the app name that you want to delete.")
      print('/n')
      deleteApp = input()
      kilolo = finding_credential(deleteApp)
      delete_credentials(kilolo)
      print(f"Been deleted. {deleteApp} ")

    elif short_code == 'fc':
      print("Enter the name of the app you are looking for.")
      searched_app = input()
      searched_credential = finding_credential(searched_app)
      print(f"We have found {searched_credential.application_name} ")
      


    elif short_code == 'ex':
      print("bye...")
      continue
        
      
      
     
       





if __name__ == "__main__":
  main()
