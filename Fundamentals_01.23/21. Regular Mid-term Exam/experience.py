experience_needed = float(input())
battles_count = int(input())

total_experience = 0

for battle in range(1, battles_count + 1):
    xp  = float(input())
    total_experience += xp

    if battle % 3 == 0:
        total_experience += xp * 0.15

    if battle % 5 == 0:
        total_experience -= xp * 0.1

    if battle % 15 == 0:
        total_experience += xp * 0.05
    
    if total_experience >= experience_needed:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break
else:
    print(f"Player was not able to collect the needed experience, {experience_needed - total_experience:.2f} more needed.")
