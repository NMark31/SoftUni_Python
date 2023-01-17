# In
chicken_menus = int(input())
fish_menus = int(input())
vegi_menus = int(input())

# Prices
price_chicken = 10.35
price_fish = 12.4
price_vegi = 8.15
total_price_menus = chicken_menus * price_chicken + fish_menus * price_fish + vegi_menus * price_vegi
price_desert = total_price_menus * 0.2
delivery = 2.5

# Logic
total = total_price_menus + price_desert + delivery

# Out
print (total)