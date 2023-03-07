from math import ceil

num_of_students = int(input())
num_of_lectures = int(input())
bonus = int(input())
students_bonuses = [0]
max_lectures = [0]

for n in range (num_of_students):
    lectures_attended = int(input())
    if num_of_lectures == 0:
        students_bonuses.append(0)
        continue

    students_bonuses.append(lectures_attended / num_of_lectures * (5 + bonus))
    max_lectures.append(lectures_attended)

print(f"Max Bonus: {ceil(max(students_bonuses))}.")
print(f"The student has attended {max(max_lectures)} lectures.")

