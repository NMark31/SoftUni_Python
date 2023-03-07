# Input
trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

# Prices
puzzles_price = 2.60
dolls_price = 3
teddy_bears_price = 4.10
minions_price = 8.20
trucks_price = 2
total_toys_price = \
    puzzles_count * puzzles_price + \
        dolls_count * dolls_price + \
            teddy_bears_count * teddy_bears_price + \
                minions_count * minions_price + \
                    trucks_count * trucks_price

# Logic
total_toys_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count
discount = total_toys_price * 0.25
if total_toys_count >= 50:
    total_toys_price -= discount

rent = total_toys_price * 0.1
total = total_toys_price - rent

if total >= trip_price:
    print(f'Yes! {(total-trip_price):.2f} lv left.')

else:
    print(f'Not enough money! {(trip_price - total):.2f} lv needed.')  