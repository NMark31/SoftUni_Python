import math

# Input
from functools import total_ordering


first_time = int(input())
second_time = int(input())
third_time = int(input())

# Logic
total_time = first_time + second_time + third_time
minutes = total_time // 60
seconds = total_time % 60
minutes = math.floor(minutes)

# Output
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
