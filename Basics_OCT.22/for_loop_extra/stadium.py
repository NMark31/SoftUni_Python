stadium_capacity = int(input())
fans_count = int(input())
sector_A_count = 0
sector_B_count = 0
sector_V_count = 0
sector_G_count = 0

for _ in range(fans_count):
    sector = input()

    if sector == "A":
        sector_A_count += 1
    
    elif sector == "B":
        sector_B_count += 1

    elif sector == "V":
        sector_V_count += 1
    
    elif sector == "G":
        sector_G_count += 1

print(f'{(sector_A_count / fans_count) * 100:.2f}%')
print(f'{(sector_B_count / fans_count) * 100:.2f}%')
print(f'{(sector_V_count / fans_count) * 100:.2f}%')
print(f'{(sector_G_count / fans_count) * 100:.2f}%')
print(f'{(fans_count / stadium_capacity) * 100:.2f}%')
