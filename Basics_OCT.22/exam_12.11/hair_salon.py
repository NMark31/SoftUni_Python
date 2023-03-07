daily_target = int(input())

daily_sales = 0

while daily_sales < daily_target:
    service = input()

    if service == 'closed':
        print(f'Target not reached! You need {daily_target - daily_sales}lv. more.')
        break

    elif service == 'haircut':
        style = input()

        if style == 'mens':
            daily_sales += 15
        elif style == 'ladies':
            daily_sales += 20
        elif style == 'kids':
            daily_sales += 10

    elif service == 'color':
        style = input()

        if style == 'touch up':
            daily_sales += 20
        elif style == 'full color':
            daily_sales += 30

else:
    print("You have reached your target for the day!")

print(f'Earned money: {daily_sales}lv.')
