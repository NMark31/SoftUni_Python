student_name = input()
grade = 1
fail_count = 0
total_score = 0

while grade <= 12:
    score = float(input())

    if score < 4.00:
        fail_count += 1

        if fail_count >= 2:
            print(f'{student_name} has been excluded at {grade} grade')
            break
        continue

    grade += 1
    total_score += score
    
else:
    print(f'{student_name} graduated. Average grade: {(total_score / 12):.2f}')