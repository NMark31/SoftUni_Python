import math

number_of_people = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_entrance_price = number_of_people * entrance_fee
total_umbrella_price = math.ceil((number_of_people / 2)) * umbrella_price
total_sunbed_price = math.ceil((number_of_people * 0.75)) * sunbed_price

total_price = total_sunbed_price + total_entrance_price + total_umbrella_price
print(f'{total_price:.2f} lv.')
