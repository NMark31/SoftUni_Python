courses = {}

line = input()

while True:

    if ":" not in line:
        break

    student_name, student_id, course_name = line.split(":")
    
    if course_name not in courses:
        courses[course_name] = {student_name : student_id}
    
    else:
        courses[course_name][student_name] = student_id
    
    line = input()

line = line.replace("_", " ")

students = courses[line]

for student_name, student_id in students.items():
    print(f"{student_name} - {student_id}")
