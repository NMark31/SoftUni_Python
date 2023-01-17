import math
# Input
figure = input()
area = 0
#Logic
if figure == 'square':
    a = float(input())
    area = math.pow(a, 2)
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif figure == 'circle':
    r = float(input())
    area = math.pi * math.pow(r, 2)
elif figure == 'triangle':
    a = float(input())
    hb = float(input())
    area = a * hb / 2

print(figure)
print(f"{area:.3f}")
