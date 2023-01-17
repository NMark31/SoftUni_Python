import math

# Input
record = float(input())
distance = float(input())
time_per_meter = float(input())

# Times
water_resistance = math.floor((distance / 15)) * 12.5
total_time = distance * time_per_meter + water_resistance

#Logic
if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {abs(record - total_time):.2f} seconds slower.')
