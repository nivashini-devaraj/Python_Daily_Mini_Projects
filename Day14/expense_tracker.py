class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename

    # Add a new expense
    def add_expense(self, category, amount, date):
        with open(self.filename, "a") as file:  # append mode
            file.write(f"{category},{amount},{date}\n")
        print(f" Expense added: {category} - ${amount} on {date}")

    # View all expenses
    def view_expenses(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("No expenses recorded yet.")
                    return

                print("\n📘 All Expenses:")
                print("Category\tAmount\tDate")
                print("-" * 35)
                for line in lines:
                    category, amount, date = line.strip().split(",")
                    print(f"{category}\t${amount}\t{date}")
        except FileNotFoundError:
            print("No expense file found. Please add an expense first.")

    # Calculate total expenditure
    def total_expenses(self):
        total = 0
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) >= 2:
                        amount = float(parts[1])
                        total += amount
            print(f"\n Total Expenditure: ${total}")
        except FileNotFoundError:
            print("No expense file found. Please add an expense first.")
        except ValueError:
            print(" Error reading amounts from file.")


# --- Menu-driven Program ---
def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenditure")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            date = input("Enter date (DD-MM-YYYY): ")
            tracker.add_expense(category, amount, date)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expenses()

        elif choice == "4":
            print(" Exiting Expense Tracker.")
            break

        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
