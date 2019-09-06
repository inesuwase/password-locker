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
        self.new_user = User("James","Muriuki","0712345678","james@ms.com","James","mine") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"James")
        self.assertEqual(self.new_password.last_name,"Muriuki")
        self.assertEqual(self.new_password.phone_number,"0712345678")
        self.assertEqual(self.new_password.email,"james@ms.com")
        self.assertEqual(self.new_password.user_name,"James")
        self.assertEqual(self.new_password.password,"mine")


if __name__ == '__main__':
    unittest.main()