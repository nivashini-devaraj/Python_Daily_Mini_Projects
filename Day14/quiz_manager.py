import csv

class QuizScoreManager:
    def __init__(self, filename="scores.csv"):
        self.filename = filename

    # Add a new quiz score
    def add_score(self, student_name, subject, score):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_name, subject, score])
        print(f" Score added for {student_name} in {subject}: {score}")

    # View all quiz scores
    def view_scores(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                scores = list(reader)
                if not scores:
                    print("No quiz scores found.")
                else:
                    print("\n All Quiz Scores:")
                    print("Name\tSubject\tScore")
                    print("-" * 30)
                    for row in scores:
                        print("\t".join(row))
        except FileNotFoundError:
            print("No score records found (file missing).")

    # Search for a student's scores by name
    def search_score(self, student_name):
        found = False
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                print(f"\n Searching scores for '{student_name}'...")
                for row in reader:
                    if row and row[0].lower() == student_name.lower():
                        print(f" Found: {row[0]} - {row[1]}: {row[2]}")
                        found = True
                if not found:
                    print(f" No scores found for '{student_name}'.")
        except FileNotFoundError:
            print("No score records found (file missing).")


# --- Menu-driven Program ---
def main():
    manager = QuizScoreManager()

    while True:
        print("\n===== QUIZ SCORE MANAGER =====")
        print("1. Add Quiz Score")
        print("2. View All Scores")
        print("3. Search for Student's Score")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            score = input("Enter score: ")
            manager.add_score(name, subject, score)

        elif choice == "2":
            manager.view_scores()

        elif choice == "3":
            name = input("Enter student name to search: ")
            manager.search_score(name)

        elif choice == "4":
            print(" Exiting Quiz Score Manager. ")
            break

        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
