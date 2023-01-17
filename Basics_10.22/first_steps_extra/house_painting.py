import math
# Input
x = float(input())
y = float(input())
h = float(input())

# Logic
front_wall_paintable = (math.pow(x, 2)) - (1.2 * 2)
back_wall_paintable = math.pow(x, 2)
left_wall_paintable = (x * y) - (math.pow(1.5, 2))
right_wall_paintable = (x * y) - (math.pow(1.5, 2))

roof = (2 * (x * y)) + (2* (x * h / 2))
facade = front_wall_paintable + back_wall_paintable + left_wall_paintable + right_wall_paintable

green_paint = facade / 3.4
red_paint = roof / 4.3

# Output
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
