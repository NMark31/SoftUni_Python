# Input
num_of_pens = int(input())
num_of_sharpies = int(input())
litres_of_detergent = int(input())
discount = int(input()) / 100

# Prices
price_of_pens = 5.8
price_of_sharpies = 7.2
price_of_detergent = 1.2

# Logic

total_price = num_of_pens * price_of_pens + num_of_sharpies * price_of_sharpies + litres_of_detergent * price_of_detergent
total_price -= total_price * discount

# Output
print(total_price)
