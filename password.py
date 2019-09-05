
class User:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] 

    def __init__(self,user_name,number,email,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.phone_number = number
        self.email = email
        self.password = password
