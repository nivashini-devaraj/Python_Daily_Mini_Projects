class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()   

    # Load tasks from file
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []  

    # Save tasks to file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    # Add a new task
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f" Task '{task}' added.")

    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            print()

    # Remove a task by number
    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f" Task '{removed}' removed.")
        else:
            print(" Invalid task number.")


def main():
    manager = TaskManager()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            manager.add_task(task)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.view_tasks()
            try:
                num = int(input("Enter the task number to remove: "))
                manager.remove_task(num)
            except ValueError:
                print(" Please enter a valid number.")
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice, try again.")


if __name__ == "__main__":
    main()
