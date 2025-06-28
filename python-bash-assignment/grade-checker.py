mark = input("Enter your mark: ")

def check_grade(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            return "Invalid mark. Please enter a number between 0 and 100."
        elif mark >= 90:
            return "A"
        elif mark >= 80:
            return "B"
        elif mark >= 70:
            return "C"
        elif mark >= 60:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Invalid input. Please enter a numeric value."

result = check_grade(mark)
print(f"Your grade is: {result}")