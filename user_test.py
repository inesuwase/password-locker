import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","mine") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

       
        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.password,"mine")
    def test_save_user(self):
        '''
        test_save_cuser test case to test if the user object is saved into
         the user list
        '''
        self.new_user.test_save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
     unittest.main()