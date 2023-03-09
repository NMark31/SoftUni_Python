n = int(input())

all_grades = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in all_grades:
        all_grades[student] = [grade]

    else:
        all_grades[student].append(grade)

for student, grade in all_grades.items():
    avg_grade = sum(grade) / len(grade)
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade:.2f}")
