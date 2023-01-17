#Input
weight = float(input())
service_type = input()
distance = int(input())

#Price list (in lv)
under_1 = 0.03 * distance
one_to_9 = 0.05 * distance
ten_to_39 = 0.1 * distance
forty_to_89 = 0.15 * distance
ninety_to_150 = 0.20 * distance
total_cost = 0

if service_type == 'standard':
    if weight < 1:
        total_cost = under_1
    elif weight < 10:
        total_cost = one_to_9
    elif weight < 40:
        total_cost = ten_to_39
    elif weight < 90:
        total_cost = forty_to_89
    elif weight < 150:
        total_cost = ninety_to_150

elif service_type == 'express':
    if weight < 1:
        total_cost = under_1 + under_1 * 0.8 * weight
    elif weight < 10:
        total_cost = one_to_9 + one_to_9 * 0.4 * weight
    elif weight < 40:
        total_cost = ten_to_39 + ten_to_39 * 0.05 * weight
    elif weight < 90:
        total_cost = forty_to_89 + forty_to_89 * 0.02 * weight
    elif weight < 150:
        total_cost = ninety_to_150 + ninety_to_150 * 0.01 * weight

print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_cost:.2f} lv.')
