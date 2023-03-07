# Input
screen_type = input()
r = int(input())
c = int(input())

# Logic
ticket_price = 0

if screen_type == 'Premiere':
    ticket_price = 12.00
elif screen_type == 'Normal':
    ticket_price = 7.50
else:
    ticket_price = 5.00

total_revenue = c * r * ticket_price
print(f'{total_revenue:.2f} leva')
