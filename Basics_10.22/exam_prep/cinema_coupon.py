coupon_value = int(input())

tickets_count = 0
misc_count = 0

while coupon_value >= 0:
    purchase = input()

    if purchase == 'End':
        break

    current_value = 0

    if len(purchase) > 8:
        current_value += ord(purchase[0]) + ord(purchase[1])

        if current_value > coupon_value:
            break
        tickets_count += 1

    else:
        current_value += ord(purchase[0])

        if current_value > coupon_value:
            break
        misc_count += 1
    
    coupon_value -= current_value

print(tickets_count)
print(misc_count)
