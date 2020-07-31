class Account:
    def __init__(self, user_id, balance):
        self.user_id: int = user_id
        self.balance: int = balance

    async def return_balance(self):
        return f'Account Balance of: {self.balance:,.d} points.'

