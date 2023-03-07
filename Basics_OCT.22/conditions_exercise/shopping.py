# Input
budget = float(input())
GPU = int(input())
CPU = int(input())
RAM = int(input())

# Prices
GPU_price = 250
CPU_price = (GPU * GPU_price) * 0.35
RAM_price = (GPU * GPU_price) * 0.10
total_price_raw = GPU * GPU_price + CPU * CPU_price + RAM * RAM_price
discount = total_price_raw * 0.15 if GPU > CPU else 0

total_price = total_price_raw - discount

# Output
if budget >= total_price:
    print(f'You have {(budget - total_price):.2f} leva left!')

else:
    print(f'Not enough money! You need {(total_price - budget):.2f} leva more!')
    