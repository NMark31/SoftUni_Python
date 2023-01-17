# Input Plane

area = float(input())

# Logic Plane

price_before_discout = area * 7.61
discount = price_before_discout * 0.18
total_price = price_before_discout - discount

# Output Plane

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")