import unittest # Importing the unittest module
from credintials import Credintials # Importing the credintials class

class TestCredintials(unittest.TestCase):

    '''
    Test class that defines test cases for the cledintials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credintials = Credintials("facebook","James","mine") # create credintials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

       
        self.assertEqual(self.new_credintials.account_name,"facebook")
        self.assertEqual(self.new_credintials.user_name,"James")
        self.assertEqual(self.new_credintials.password,"mine")
    def test_save_credintials(self):
        '''
        test_save_credintials test case to test if the credintials object is saved into
         the credintials list
        '''
        self.new_credintials.save_credintials() # saving the new credintials
        self.assertEqual(len(Credintials.credintials_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case test has run.
            '''
            Credintials.credintials_list=[]
    def test_save_multiple_credintials(self):
            '''
            test_save_multiple_credintials to check if we can save multiple credintials
            objects to our credintials_list
            '''
            self.new_credintials.save_credintials()
            test_save_credintials = Credintials("twitter","Test","test@user.com") # new credintials
            test_save_credintials.save_credintials()
            self.assertEqual(len(Credintials.credintials_list),2)
    def test_delete_credintials(self):
            '''
            test_delete_credintials to test if we can remove a credintials from our credintials list
            '''
            self.new_credintials.save_credintials()
            test_save_credintials = Credintials("twitter","Test","test@user.com") # new credintials
            test_save_credintials.save_credintials()

            self.new_credintials.test_delete_credintials()# Deleting a credintials object
            self.assertEqual(len(Credintials.credintials_list),1)
    




if __name__ == '__main__':
     unittest.main()