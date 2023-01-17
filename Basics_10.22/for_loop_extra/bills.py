months = int(input())
electricity_bill = 0
water_bill = months * 20
internet_bill = months * 15
others_bill = 0
average = 0

for _ in range(months):
    electricity_price = float(input())

    electricity_bill += electricity_price
    others_price = electricity_price + 20 + 15
    others_bill += others_price + (others_price * 0.2)

average = (electricity_bill + water_bill + internet_bill + others_bill) / months

print(f'Electricity: {electricity_bill:.2f} lv')
print(f'Water: {water_bill:.2f} lv')
print(f'Internet: {internet_bill:.2f} lv')
print(f'Other: {others_bill:.2f} lv')
print(f'Average: {average:.2f} lv')
