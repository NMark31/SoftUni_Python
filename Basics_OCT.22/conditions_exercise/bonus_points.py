# Input
score = int(input())

# Logic
if score <= 100:
    bonus_points = 5

elif score > 1000:
    bonus_points = score * 0.1

else:
    bonus_points = score * 0.2

if score % 2 == 0:
    bonus_points += 1

elif score % 10 == 5:
    bonus_points += 2

# Output
print(bonus_points)
print(bonus_points + score)
