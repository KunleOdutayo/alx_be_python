class BankAccount:
    def __init__(self,initial_balance):
        if initial_balance >= 0:
            self._initial_balance = initial_balance
        else:
            print('Initial balance cannot be negative. Settinig to 0.')
            self._account_balance = 0
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return True
        else:
            print('Deposit amount must be positive.')
            return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        elif amount <= 0:
            print('Withdrawal amount must be positive.')
            return False
        else:
            return False
    def display_balance(self):
        print("Current Balance: {self._account_balance:.2f}")