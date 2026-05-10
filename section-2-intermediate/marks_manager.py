student_marks_name = {}
studen_grade = {}
student_count = int(input("Enter how many students are in your class: "))
for i in range(student_count):
    student_name = input("Enter student  name : ")
    student_marks = int(input("Enter that student marks: "))
    if student_marks>=90:
        grade = "A Grade"
    elif 71<=student_marks<=89:
        grade = "B Grade"
    elif 50<=student_marks<=70:
        grade = "C Grade"
    elif 15<=student_marks<=49:
        grade = "D Grade"
    elif student_marks<=14:
        grade = "E Grade"
    elif student_marks == 0:
        grade = "F Grade"
    student_marks_name[student_name] = student_marks
    studen_grade[student_name] = grade
rule = max(student_marks_name.values())
rule_ = min(student_marks_name.values())
total = 0
for n in student_marks_name.values():
    total += n
average = total/len(student_marks_name)
print("===== CLASS REPORT =====")
print("Names      Marks      Grades")
print("-------------------------")

for name, marks in student_marks_name.items():
    grade = studen_grade[name]
    print(f"{name} : {marks} : {grade}")

print("-------------------------")
print(f"Average : {average}")
print(f"Highest : {rule}")
print(f"Lowest  : {rule_}")
print("=========================")