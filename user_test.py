import unittest # Importing the unittest module
from password import User # Importing the contact class

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
        self.new_password = User("James","mine") # create password object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

       
        self.assertEqual(self.new_password.user_name,"James")
        self.assertEqual(self.new_password.password,"mine")


# if __name__ == '__main__':
#     unittest.main()
#     def test_save_password(self):
#         '''
#         test_save_password test case to test if the password object is saved into
#          the password list
#         '''
#         self.new_password.test_save_password() # saving the new password
#         self.assertEqual(len(User.password_list),1)

# if __name__ ==  '__main__':
#     unittest.main()