# Input
vegetables_price = float(input())
fruits_price = float(input())
total_vegetables = int(input())
total_fruits = int(input())

# Logic
total_revenue = (vegetables_price * total_vegetables) + (fruits_price * total_fruits)
total_revenue_euro = total_revenue / 1.94

# Output
print(f'{total_revenue_euro:.2f}')
