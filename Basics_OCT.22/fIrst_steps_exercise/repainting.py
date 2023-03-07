# Input
cover = int(input())
paint = int(input())
thinner = int(input())
manhours = int(input())

# Additional resources 
bags = 0.4
extra_cover = 2
extra_paint = paint * 0.10

# Prices
price_of_cover = 1.5
price_of_paint = 14.5
price_of_thinner = 5
total_materials_price = cover * price_of_cover \
    + paint * price_of_paint \
    + thinner * price_of_thinner \
    + bags \
    + extra_cover * price_of_cover \
    + extra_paint * price_of_paint
price_of_workers = total_materials_price * 0.30

# Logic
total = total_materials_price + price_of_workers * manhours

# Output
print(total)