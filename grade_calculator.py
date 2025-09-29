def calculate_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    elif 0 <= mark <= 59:
        return "F"
    else:
        return "Invalid Mark"

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [95, 82, 67, 74, 89]

for i in range(len(students)):
    grade = calculate_grade(marks[i])
    print(f"{students[i]}: {marks[i]} – Grade {grade}")
