class User:
    """
    Class that generates new instances of user.
    """
    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email,user_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.user_name = user_name
        self.password = password