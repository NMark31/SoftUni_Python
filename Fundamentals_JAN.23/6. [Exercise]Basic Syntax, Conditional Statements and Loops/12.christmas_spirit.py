decorations_per_run = int(input())
days_until_xmas = int(input())
total_price = 0
xmas_spirit_points = 0

for i in range(1, days_until_xmas + 1):

    if i % 11 == 0:
        decorations_per_run += 2
    if i % 2 == 0:
        total_price += decorations_per_run * 2
        xmas_spirit_points += 5

    if i % 3 == 0:
        total_price += decorations_per_run * 5 + decorations_per_run * 3
        xmas_spirit_points += 13

    if i % 5 == 0:
        total_price += decorations_per_run * 15
        xmas_spirit_points += 17
        if i % 3 == 0:
            xmas_spirit_points += 30
    if i % 10 == 0:
        xmas_spirit_points -= 20
        total_price += 23

if days_until_xmas % 10 == 0:
    xmas_spirit_points -= 30

if xmas_spirit_points < 0:
    xmas_spirit_points = 0
print(f"Total cost: {total_price}")
print(f"Total spirit: {xmas_spirit_points}")
