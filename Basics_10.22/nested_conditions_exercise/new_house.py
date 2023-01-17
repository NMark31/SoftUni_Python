# Input
type_of_flower = input()
quantity = int(input())
budget = int(input())

# Prices
rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolu_price = 2.5
total_price = 0

# Logic
if type_of_flower == 'Roses':
    if quantity > 80:
        total_price = quantity * rose_price * 0.9
    else:
        total_price = quantity * rose_price
elif type_of_flower == 'Dahlias':
    if quantity > 90:
        total_price = quantity * dahlia_price * 0.85
    else:
        total_price = quantity * dahlia_price
elif type_of_flower == 'Tulips':
    if quantity > 80:
        total_price = quantity * tulip_price * 0.85
    else:
        total_price = quantity * tulip_price
elif type_of_flower == 'Narcissus':
    if quantity < 120:
        total_price = quantity * narcissus_price
        total_price += total_price * 0.15
    else:
        total_price = quantity * narcissus_price
else:
    if quantity < 80:
        total_price = quantity * gladiolu_price
        total_price += total_price * 0.2
    else:
        total_price = quantity * gladiolu_price
# Output
if total_price <= budget:
    print(f"Hey, you have a great garden with {quantity} {type_of_flower} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - total_price):.2f} leva more.")
