class Account:

    # email and pass as private variable
    # calling them normally cause error
    # created two new functions just to access them
    # (See below)

    def __init__(self, email : str , password : str):
        self.__email = email
        self.__password = password
        self.__balance:float = 0.0


    def deposit(self):
        pass

    def withdraw(self):
        pass

    def check_balance(self):
        pass

    def transfer(self,target:Account, amount:float)-> bool:
        """Return True if the transfer is successful, otherwise return False."""
        if amount >= 0 and self.__balance >= amount:
            self.__balance -= amount
            target.setBalance(target.getBalance() + amount)
            return True
        return False

    def transaction_history(self):
        pass


    #Validation
    #These functions are used in Bank

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
    # Way to access private variable

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    # Get balance
    
    def getBalance(self):
        """Return the current balance of the account."""
        return self.__balance

    #Set balance

    def setBalance(self, balance : float)-> None:
        """Set the balance of the account to the specified value."""
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Balance cannot be negative.")