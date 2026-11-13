class Account:

    def __init__(self, email : str , password : str):
        self.__email = email
        self.__password = password


    def deposit(self):
        pass

    def withdraw(self):
        pass

    def check_balance(self):
        pass

    def transaction_history(self):
        pass


    #Validation

    @staticmethod

    def validateEmail( email : str) -> bool:

        if (len(email) > 5) and ("."  in email) and ("@"  in email):
            return True
        else:
            return False

    @staticmethod

    def validatePassword( password : str) -> bool:
    
        if len(password) < 8:
            return False

        if not any(char.isupper() for char in password):
            return False

        if not any(char.islower() for char in password):
            return False

        if not any(char.isdigit() for char in password):
            return False

        if not any(char in "!@#$%^&*()-_+=" for char in password):
            return False

        return True



    # Get email and password

    # This is only for backend

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password#

