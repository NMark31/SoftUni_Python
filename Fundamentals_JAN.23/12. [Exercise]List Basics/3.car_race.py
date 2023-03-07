race_track = [int(i) for i in (input().split())]

left_side = race_track[:len(race_track) // 2]
right_side = race_track[(len(race_track) // 2) + 1:]

left_car_time, right_car_time = 0, 0
winner = ''
winner_time = 0

for left in left_side:
    if left == 0:
        left_car_time *= 0.8
    else:
        left_car_time += left

for right in range(-1, -len(right_side) - 1, -1):
    if right_side[right] == 0:
        right_car_time *= 0.8
    else:
        right_car_time += right_side[right]


if left_car_time < right_car_time:
    winner = 'left'
    winner_time = left_car_time
else:
    winner = 'right'
    winner_time = right_car_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
