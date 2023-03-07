#Input

cpu_price = float(input()) * 1.57
gpu_price = float(input()) * 1.57
ram_price = float(input()) * 1.57
ram_count = int(input())
discount = float(input())

total_money_needed = cpu_price + gpu_price
total_money_needed -= total_money_needed * discount
total_money_needed += ram_count * ram_price

print(f'Money needed - {total_money_needed:.2f} leva.')
