lunch_money = float(input())
daily_sales = float(input())
total_expenses = float(input())
present_price = float(input())

profit = (5 * lunch_money) + (5 * daily_sales) - total_expenses

if profit >= present_price:
    print(f'Profit: {profit:.2f} BGN, the gift has been purchased.')

else:
    print(f"Insufficient money: {present_price - profit:.2f} BGN.")
