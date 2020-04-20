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
  

class Credentials:
  '''
  Class generatess new instances of accounts that the user would like to store a password for.
  '''
  credentials_list = [] #an empty list for the users accounts

  def __init__ (self, application_name, application_password):
    self.app = application_name
    self.passwordApp = application_password
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
  
