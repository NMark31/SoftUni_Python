# Input
budget = float(input())
extra_count = int(input())
price_per_dress = float(input())

# Prices
decor = budget * 0.10
total_dress_price = extra_count * price_per_dress

discount = total_dress_price * 0.10 if extra_count > 150 else 0
total_price = total_dress_price + decor - discount

# Logic
if total_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {(total_price - budget):.2f} leva more.')

else:
    print("Action!")
    print(f'Wingard starts filming with {(budget - total_price):.2f} leva left.')
    