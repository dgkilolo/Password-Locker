import unittest
from passwordLocker import User
from passwordLocker import Credentials

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviours
  Args:
    TestCase class that helps in creating new test cases.
  '''

  def setUp(self):
    '''
    Set up method that runs before each taste case, creating the results we expect.
    '''
    self.new_account = User("David","boot")
    self.new_application = Credentials("Facebook", "word")

  def test_initialization(self): 
    '''
    Test initialization case to test if object is initialized properly
    '''
    self.assertEqual(self.new_account.username,"David")
    self.assertEqual(self.new_account.password,"boot")

    self.assertEqual(self.new_application.application_name,"Facebook")
    self.assertEqual(self.new_application.application_password,"word")

  def test_display_credentials(self):
    '''
    Method that returns a list of the credentials saved.
    '''
    self.assertEqual(Credentials.display_applications(), Credentials.credentials_list)

  def test_delete_credential(self):
    '''
    Test to remove credential from the credentials list
    '''
    self.new_application.append_application()
    test_credential = Credentials("Twitter","bird") #new credential
    test_credential.append_application()

    self.new_application.delete_credential() #method to delete credential object
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_find_contact_by_name(self):
    '''
    Test to check if we can find a credential by the credential name.
    '''
    self.new_application.append_application()
    test_credential = Credentials("Instagram", "gram343") #new credential
    test_credential.append_application()

    found_credential = Credentials.find_credential("Instagram")
    self.assertEqual(found_credential.application_name, test_credential.application_name)


if __name__ == '__main__':
  unittest.main()
    