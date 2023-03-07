max_low_grades = int(input())
problems_count = 0
fails_count = 0
last_problem = None
total_score = 0

while fails_count < max_low_grades:
    problem = input()

    if problem == 'Enough':
        print(f'Average score: {(total_score / problems_count):.2f}')
        print(f'Number of problems: {problems_count}')
        print(f'Last problem: {last_problem}')
        break

    grade = int(input())
    total_score += grade
    last_problem = problem
     
    if grade <= 4:
        fails_count += 1
    
    problems_count += 1

else:
    print(f'You need a break, {fails_count} poor grades.')
