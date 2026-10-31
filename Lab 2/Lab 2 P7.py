
students = [
    {"name": "Shimul", "marks": 85},
    {"name": "Rahim", "marks": 45},
    {"name": "Karim", "marks": 75},
    {"name": "Hasan", "marks": 90},
    {"name": "Sakib", "marks": 35}
]

total = 0
passed = 0

highest = students[0]

print("Student Records:")


for student in students:
    print("Name:", student["name"], "Marks:", student["marks"])

    total += student["marks"]

    if student["marks"] >= 50:
        passed += 1

    if student["marks"] > highest["marks"]:
        highest = student

average = total / len(students)

print("\nTotal Students:", len(students))
print("Passed Students:", passed)
print("Class Average:", average)

print("Highest Mark Student:", highest["name"])
print("Highest Marks:", highest["marks"])
