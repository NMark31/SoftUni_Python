budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_expences = float(input()) / 100

if number_of_nights > 7:
    price_per_night *= 0.95

total_price = (number_of_nights * price_per_night) + (budget * percent_expences)

if total_price <= budget:
    print(f"Ivanovi will be left with {budget - total_price:.2f} leva after vacation.")

else:
    print(f"{total_price - budget:.2f} leva needed.")
    