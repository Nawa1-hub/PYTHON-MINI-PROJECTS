students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [85, 92, 78, 88, 95]

def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

total = 0
for i in range(len(students)):
    grade = get_grade(marks[i])
    print(f"{students[i]}: {marks[i]} – Grade {grade}")
    total += marks[i]

average = total / len(marks)
print(f"Average marks: {average:.1f}")
