import math


def coordinates(values):

    if ((abs(values[0]) < abs(values[2])) and (abs(values[1]) <= abs(values[3]))) or \
            ((abs(values[1]) <= abs(values[2])) and (abs(values[1]) < abs(values[3]))):
        x = values[0]
        y = values[1]

    elif (abs(values[0]) == abs(values[2])) and (abs(values[1]) == abs(values[3])):
        x = values[0]
        y = values[1]

    else:
        x = values[2]
        y = values[3]

    return x, y


coordinates_as_list = []

for n in range(4):
    coordinates_as_list.append(float(input()))

x, y = coordinates(coordinates_as_list)
print(f"({math.floor(x)}, {math.floor(y)})")
