# Input
budget = float(input())
category = input()
number_of_people = int(input())

# Logic
remaining_budget = budget

if 1 <= number_of_people <= 4:
    remaining_budget = budget * 0.25    # Transport expenses removed
elif 5 <= number_of_people <= 9:
    remaining_budget = budget * 0.4     # Transport expenses removed
elif 10 <= number_of_people <= 24:
    remaining_budget = budget * 0.5     # Transport expenses removed
elif 25 <= number_of_people <= 49:
    remaining_budget = budget * 0.6     # Transport expenses removed
elif number_of_people >= 50:
    remaining_budget = budget * 0.75    # Transport expenses removed

total_price = number_of_people * 499.99 if category == "VIP" else number_of_people * 249.99

if total_price <= remaining_budget:
    print(f'Yes! You have {remaining_budget - total_price:.2f} leva left."')
else:
    print(f'Not enough money! You need {total_price - remaining_budget:.2f} leva.')
