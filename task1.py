student = {
    "Farhaan": 90,
    "Abhishek" :89,
    "Ammar" : 85,
    "Ahmed" : 80,
    "Abdullah" : 75,
    "Umar": 88
}
student_name = input("Enter the name of the student: ")

if student_name in student:
    print(f"The marks of {student_name} is {student[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")