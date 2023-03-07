# Input
chrizantema_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()

interim_price = 0

# Logic 
if season == 'Spring' or season == 'Summer':

    if holiday == 'Y':
        chrizantema_price = 2 + 2 * 0.15
        tulips_price = 2.5 + 2.5 * 0.15
        roses_price = 4.1 + 4.1 * 0.15      
    else:
        chrizantema_price = 2
        tulips_price = 2.5
        roses_price = 4.1

    interim_price = chrizantema_count * chrizantema_price + tulips_count * tulips_price + roses_count * roses_price

elif season == 'Autumn' or season == 'Winter':

    if holiday == 'Y':
        chrizantema_price = 3.75 + 3.75 * 0.15
        tulips_price = 4.15 + 4.15 * 0.15
        roses_price = 4.5 + 4.5 * 0.15      
    else:
        chrizantema_price = 3.75
        tulips_price = 4.15
        roses_price = 4.5

    interim_price = chrizantema_count * chrizantema_price + tulips_count * tulips_price + roses_count * roses_price

if tulips_count > 7 and season == 'Spring':
    interim_price *= 0.95

if roses_count >= 10 and season == 'Winter':
    interim_price -= interim_price * 0.1

if chrizantema_count + tulips_count + roses_count > 20:
    interim_price -= interim_price * 0.2

total_price = interim_price + 2

print(f'{total_price:.2f}')
