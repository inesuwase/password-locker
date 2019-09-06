class User:
    """
    Class that generates new instances of user.
    """
    password_list = [] # Empty passwordlist

    def __init__(self,user_name,password):

      # docstring removed for simplicity


        self.user_name = user_name
        self.password = password
class Credintials:
    """
    Class that generates new instances of user.
    """
    password_list = [] # Empty passwordlist

    def __init__(self,account_name,user_name,password):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
