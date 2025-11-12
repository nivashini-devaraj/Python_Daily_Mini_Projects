# Base Class
class BankAccount:
    def __init__(self):
        self.balance = 0  # starting balance is 0

    def deposit(self, amount):
        self.balance += amount
        print(f" Deposited: {amount}")
        print(f"Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Not enough balance.")
        else:
            self.balance -= amount
            print(f" Withdrawn: {amount}")
            print(f"Current Balance: {self.balance}")

    def check_balance(self):
        print(f" Your Balance: {self.balance}")


# Derived Class (inherits from BankAccount)
class ATM(BankAccount):
    def __init__(self):
        super().__init__()  # call the parent constructor


# --- Example Use ---
user = ATM()

user.deposit(1000)       # add money
user.check_balance()     # view balance
user.withdraw(400)       # take money out
user.check_balance()     # view again
