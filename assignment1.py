
def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 85:
        return "A"
    elif score >= 80:
        return "A-"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    else:
        return "F"

def calculate_gpa(grades):
    grade_points = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "C+": 2.7, "C": 2.3, "D+": 1.7, "D": 1.0, "F": 0.0}
    total_points = sum(grade_points[grade] for grade in grades)
    return total_points / len(grades)

def main():
    num_subjects = 7
    grades = []

    for i in range(1, num_subjects + 1):
        score = int(input(f"Enter the score for subject {i}: "))
        grades.append(calculate_grade(score))

    print("\nGrades:")
    for i, grade in enumerate(grades, start=1):
        print(f"Subject {i}: {grade}")

    gpa = calculate_gpa(grades)
    print(f"\nGPA: {gpa:.2f}")

if __name__ == "__main__":
    main()

# next
    
def calculate_percentage(total_marks, max_marks):
    return (total_marks / (max_marks * 7)) * 100

def calculate_division(percentage):
    if percentage >= 60:
        return "First Division"
    elif percentage >= 45:
        return "Second Division"
    elif percentage >= 33:
        return "Third Division"
    else:
        return "Fail"

def main():
    max_marks_per_subject = 100

    marks = []
    for i in range(1, 8):
        marks.append(int(input(f"Enter the marks obtained in subject {i}: ")))

    total_marks = sum(marks)
    percentage = calculate_percentage(total_marks, max_marks_per_subject)

    print("\nTotal Marks Obtained:", total_marks)
    print("Percentage:", round(percentage, 2))

    division = calculate_division(percentage)
    print("Division:", division)

if __name__ == "__main__":
    main()
