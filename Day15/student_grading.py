# Custom Exception for invalid marks
class InvalidMarksError(Exception):
    def __init__(self, message="Marks must be between 0 and 100."):
        self.message = message
        super().__init__(self.message)


# Function to calculate grade
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError()  # Custom exception for invalid range

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


# --- Main Program ---
def main():
    print("=== Student Grade Calculator ===")

    try:
        marks = float(input("Enter student's marks (0-100): "))
        grade = calculate_grade(marks)
        print(f"Grade: {grade}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except InvalidMarksError as e:
        print(e)


if __name__ == "__main__":
    main()
