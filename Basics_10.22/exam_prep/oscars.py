rent = int(input())

total_expenses = 0

figurine_price = rent * 0.7
catering_price = figurine_price * .85
sound_price = catering_price * .5

total_expenses = rent + figurine_price + catering_price + sound_price
print(f'{total_expenses:.2f}')
