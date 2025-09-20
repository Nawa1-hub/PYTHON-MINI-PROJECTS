name = input("Enter student name: ")
score = int(input("Enter score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score (must be 0-100)."

print("\nStudent:", name)
print("Score:", score)
print("Grade:", grade)
