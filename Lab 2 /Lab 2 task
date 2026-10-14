programming_ds = float (input("Enter your Programming DS Mark"))
data_processing = float (input("Enter your Data Processing Mark"))
data_visualization = float (input("Enter your Data Visualization Mark"))
java = float (input("Enter your java Mark"))



marks = [programming_ds, data_processing, data_visualization, java]

total_marks = 0
for mark in marks:
    total_marks += mark

print(f"total marks: {total_marks}")

highest_mark = 0
for mark in marks:
    if mark > highest_mark:
        highest_mark = mark

print(f"Highest mark: {highest_mark}")

lowest_mark = marks[0]
for mark in marks:
   if mark < lowest_mark:
      lowest_mark=mark 

print (f"Lowest Mark : {lowest_mark}")
print (f"Average Mark: {total_marks / len(marks)} ")
passed_courses = [mark for mark in marks if mark >=50 ]
print(f"Number of passed courses : { len (passed_courses )} out of {len (marks)}")
