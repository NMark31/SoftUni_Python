employee_happiness = list(map(int, input().split()))
improvement_factor = int(input())

improved_happiness = [x * improvement_factor for x in employee_happiness]

average_happiness = sum(improved_happiness)/len(improved_happiness)

happy_empoyees = list(filter(lambda x: x >= average_happiness, improved_happiness))

if len(happy_empoyees) >= len(improved_happiness) / 2:
    print(f"Score: {len(happy_empoyees)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_empoyees)}/{len(improved_happiness)}. Employees are not happy!")
