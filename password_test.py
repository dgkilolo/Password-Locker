import unittest
from passwordLocker import User

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

  def test_initialization(self): 
    '''
    Test initialization case to test if object is initialized properly
    '''
    self.assertEqual(self.new_account.username,"David")
    self.assertEqual(self.new_account.password,"boot")


if __name__ == '__main__':
  unittest.main()
    