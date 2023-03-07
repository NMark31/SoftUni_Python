fire_info = input().split("#")
water_amount = int(input())
put_out_cells = []
total_fire = 0

for fire in fire_info:
    fire_split = fire.split(" = ")

    if fire_split[0] == "High" and not(81 <= int(fire_split[1]) <= 125):
        continue

    if fire_split[0] == "Medium" and not(51 <= int(fire_split[1]) <= 80):
        continue

    if fire_split[0] == "Low" and not(1 <= int(fire_split[1]) <=  50):
        continue
    
    if water_amount < int(fire_split[1]):
        continue

    water_amount -= int(fire_split[1])
    total_fire += int(fire_split[1])
    put_out_cells.append(fire_split[1])

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {(total_fire * 0.25):.2f}")
print(f"Total Fire: {total_fire}")
