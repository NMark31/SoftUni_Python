import math

total_area = int(input()) * int(input()) * 4
paintable_area = math.ceil(total_area - (total_area * (int(input()) / 100)))
painted_area = 0

while True:
    paint_liters = input()

    if paint_liters == 'Tired!':
        print(f"{paintable_area - painted_area} quadratic m left.")
        break

    painted_area += int(paint_liters)

    if painted_area - paintable_area > 0:
        print(f"All walls are painted and you have {painted_area - paintable_area} l paint left!" )
        break
    
    elif painted_area - paintable_area == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break
