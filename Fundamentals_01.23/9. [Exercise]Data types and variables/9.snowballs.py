import sys

num_of_balls = int(input())

max_value = -sys.maxsize
weight = 0
time = 0
quality = 0

for _ in range(num_of_balls):
    w = int(input())
    t = int(input())
    q = int(input())

    value = (w / t) ** q

    if value > max_value:
        max_value = value
        weight = w
        time = t
        quality = q

print(f'{weight} : {time} = {int(max_value)} ({quality})')
