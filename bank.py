from account import Account


class Bank:

    #Keep all account

    def __init__(self):
        self.__accounts = []

    #SignUp function
    #Main UI should work with return value

    def signUp(self, email : str , password : str):

        if self.isEmailUsed(email):
            return False

        if not Account.validateEmail(email):
            return False

        if not Account.validatePassword(password):
            return False

        account = Account(email,password)
        self.__accounts.append(account)

        return True

    #login Function
    #Login should only work after you signed up

    def login(self,email : str , password : str) -> Account | None:

        for account in self.__accounts:
            if account.getEmail() == email and account.getPassword() == password:
                return account

        return None


    #check validation


    def isEmailUsed(self,email : str) -> bool:
        if self.__accounts != []:
            for account in self.__accounts:
                if account.getEmail() == email:
                    return True

        return False
