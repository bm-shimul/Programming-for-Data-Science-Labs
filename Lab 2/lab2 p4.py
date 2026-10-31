
def calculate_grade(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

grade = calculate_grade(marks)

average = sum(marks) / len(marks)

print("\nMarks:", marks)
print("Average:", average)
print("Grade:", grade)
