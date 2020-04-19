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
