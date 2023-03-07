# Input
budget = float(input())
season = input()

car_class = ''
car_type = ''
car_price = 0

# Logical
if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.35
    else:
        car_type = 'Jeep'
        car_price = budget * 0.65

elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.45
    else:
        car_type = 'Jeep'
        car_price = budget * 0.8

else:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    car_price = budget * 0.9

# Output
print(f'{car_class}')
print(f'{car_type} - {car_price:.2f}')
