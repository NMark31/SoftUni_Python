budget = float(input())
dummies = int(input())
dummy_dress_price = float(input())
decor = budget * 0.1

if dummies > 150:
    dummy_dress_price *= 0.9

total_price = dummy_dress_price * dummies + decor

if total_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {total_price - budget:.2f} leva more.')

else:
    print("Action!") 
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")
