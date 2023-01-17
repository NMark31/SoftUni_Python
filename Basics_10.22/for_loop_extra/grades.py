num_of_students = int(input('Number of grades: '))
excellent_count = 0
very_good_count = 0
good_count = 0
poor_count = 0
total_grade = 0

for _ in range(num_of_students):
    grade = float(input('Enter grade: '))

    if grade >= 5.00:
        excellent_count += 1
        
    elif grade >= 4.00:
        very_good_count += 1

    elif grade >= 3.00:
        good_count += 1

    else:
        poor_count += 1

    total_grade += grade

average_grade = total_grade / num_of_students

print('**************************************************************')
print(f'Top students: {(excellent_count / num_of_students) * 100:.2f}%')
print(f'Between 4.00 and 4.99: {(very_good_count / num_of_students) * 100:.2f}%')
print(f'Between 3.00 and 3.99: {(good_count / num_of_students) * 100:.2f}%')
print(f'Fail: {(poor_count / num_of_students) * 100:.2f}%')
print(f'Average: {average_grade:.2f}')
