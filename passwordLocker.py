class User:
  '''
  Class that generates new instances of users. Password lockers accounts.
  '''
  users_list = [] #an empty list for users.

  def __init__ (self, user_name, user_password): #this method helps us define properties for our objects.
    self.username = user_name
    self.password = user_password
    '''
    creates instance variables to take in each new instance of our class.
    the two instances take up the username and password of the new user.
    '''

  def append_account(self):
    '''
    append_account method save new account objects into the users_list.
    '''
    User.users_list.append(self)
  
  
  @classmethod
  def find_user (cls,user):
    '''
    Method that takes in the username and returns that credential from the list if it exists.
    '''
    for user in cls.users_list:
      if user.user_name == user:
        return user
  
  @classmethod
  def username_authentication(cls, username, password):
    '''
    Method to authenticate username and password.
    '''
    for user in cls.users_list:
      if user.username == username and user.password == password:
        return password 

class Credentials:
  '''
  Class generatess new instances of accounts that the user would like to store a password for.
  '''
  credentials_list = [] #an empty list for the users accounts

  def __init__ (self, application_name, application_password):
    self.application_name = application_name
    self.application_password = application_password
    '''
    Creates new instances for our class.
    The new instances take the application name for which the user would like to store/generate a password.
    '''
  
  def append_application(self):
    '''
    append_application method saves the applications into the credentials list
    '''
    Credentials.credentials_list.append(self)
  
  @classmethod
  def display_applications(cls):
    '''
    Method that returns the credentials list.
    '''
    return cls.credentials_list

  def delete_credential(self):
    '''
    Methods that deletes a saved credential
    '''
    Credentials.credentials_list.remove(self)

  @classmethod
  def find_credential(cls, name):
    '''
    Method that takes in a name and returns a credential that matches that name.
    '''
    for credential in cls.credentials_list:
      if credential.application_name == name:
        return credential

  

  
