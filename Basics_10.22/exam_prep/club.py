target_revenue = float(input())

current_revenue = 0

while current_revenue < target_revenue:
    cocktail_name = input()

    if cocktail_name == "Party!":
        print(f'We need {target_revenue - current_revenue:.2f} leva more.')
        break

    cocktail_count = int(input())
    order_value = 0


    order_value += len(cocktail_name) * cocktail_count

    if order_value % 2 != 0:
        current_revenue += order_value * 0.75
    else:
        current_revenue += order_value

else:
    print('Target acquired.')

print(f'Club income - {current_revenue:.2f} leva.')
