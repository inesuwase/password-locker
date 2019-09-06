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
