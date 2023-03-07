pc_count = int(input())

total_rating = 0
sales_count = 0

for i in range(pc_count):
    number = int(input())

    rating = number % 10
    sales = number // 10
    
    if rating == 2:
        sales *= 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales *= 1

    total_rating += rating
    sales_count += sales

print(f'{sales_count:.2f}')
print(f'{total_rating / pc_count:.2f}')
