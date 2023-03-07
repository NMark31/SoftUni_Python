# Input
mackerel_price = float(input()) #price per kilo
sprat_price = float(input()) #price per kilo

bonito_count = float(input()) #kilograms of the product
scad_count = float(input()) #kilograms of the product
mussels_count = int(input()) #kilograms of the product

# Prices
bonito_price = mackerel_price + (mackerel_price * 0.60)
scad_price = sprat_price + (sprat_price * 0.80)
mussels_price = 7.5

# Logic
total_value = (bonito_count * bonito_price) + (scad_count * scad_price) + (mussels_count * mussels_price)

# Outpu
print(f'{total_value:.2f}')
