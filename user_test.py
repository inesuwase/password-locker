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
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case test has run.
            '''
            User.user_list=[]
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)




if __name__ == '__main__':
     unittest.main()