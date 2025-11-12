# Custom Exception for insufficient balance
class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient balance for this transaction."):
        self.message = message
        super().__init__(self.message)


# BankAccount Class
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")
        except ValueError as e:
            print(e)

    # Withdraw money
    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise InsufficientBalanceError()
            self.balance -= amount
            print(f"Withdrawn Rs.{amount:.2f}. Remaining balance: Rs.{self.balance:.2f}")
        except ValueError as e:
            print(e)
        except InsufficientBalanceError as e:
            print(e)

    # Check balance
    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance:.2f}")


# --- Menu-driven ATM Simulator ---
def main():
    print("Welcome to Simple ATM Simulator")
    account = BankAccount(balance=1000.0)  # Starting balance

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()

        elif choice == "2":
            amount = input("Enter amount to deposit: ")
            account.deposit(amount)

        elif choice == "3":
            amount = input("Enter amount to withdraw: ")
            account.withdraw(amount)

        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
