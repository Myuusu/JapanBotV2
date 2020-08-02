class Account:
    def __init__(self, user_id, balance):
        self.account = {
            "user_id": user_id,
            "balance": balance
        }

    def __getitem__(self, key):
        return self.account[key]

    def __setitem__(self, key, value):
        self.account[key] = value

    def get_balance(self):
        return self.__getitem__("balance")

    def get_user_id(self):
        return self.__getitem__("user_id")

    def set_balance(self, balance):
        self.__setitem__("balance", balance)
