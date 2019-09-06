class Credintials:                                                                            
    """
    Class that generates new instances of user.
    """
    credintials_list = [] # Empty passwordlist

    def __init__(self,account_name,user_name,password):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
    def save_credintials(self):

        '''
        save_credintials method saves ucredintials objects into credintiala_list
        '''

        Credintials.credintials_list.append(self) 
    def test_delete_credintials(self):

        '''
        delete_credintials method deletes a saved credintials from the credintials_list
        '''

        Credintials.credintials_list.remove(self) 
    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a credintials that matches that name.

        Args:
            name: name to search for
        Returns :
            Credintials of person that matches the name.
        '''

        for credintials in cls.credintials_list:
            if credintials.user_name == name:
                return credintials  