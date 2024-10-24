class Account:

    def __init__(self, _id: int, name: str, balance: int = 0):
        self._id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> int | str:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return f"Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self._id} has {self.balance} balance"
