import csv

class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename = filename

    # Add a student record
    def add_student(self, name, age, grade):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, grade])
        print(f" Student '{name}' added successfully!")

    # View all student records
    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                students = list(reader)
                if not students:
                    print("No student records found.")
                else:
                    print("\n All Student Records:")
                    print("Name\tAge\tGrade")
                    print("-" * 25)
                    for row in students:
                        print("\t".join(row))
        except FileNotFoundError:
            print("No student records found (file missing).")

    # Search for a specific student
    def search_student(self, name):
        found = False
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0].lower() == name.lower():
                        print(f"\n Student Found:\nName: {row[0]}\nAge: {row[1]}\nGrade: {row[2]}")
                        found = True
                        break
            if not found:
                print(f" No record found for '{name}'.")
        except FileNotFoundError:
            print("No student records found (file missing).")


# --- Menu-driven Program ---
def main():
    manager = StudentManager()

    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            manager.add_student(name, age, grade)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_student(name)

        elif choice == "4":
            print(" Exiting...")
            break

        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
