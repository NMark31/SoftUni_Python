import math

# Input
series = input()
series_length = int(input())
break_length = int(input())

# Times
lunch_time = break_length / 8
relax_time = break_length / 4
total_time = lunch_time + relax_time + series_length
# Logic
if break_length >= total_time:
    print(f'You have enough time to watch {series} and left with {math.ceil(break_length - total_time)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(total_time - break_length)} more minutes.")