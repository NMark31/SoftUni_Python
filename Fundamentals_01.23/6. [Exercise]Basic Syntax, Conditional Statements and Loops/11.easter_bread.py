budget = float(input())
flour_price_per_kilo = float(input())
############################-LOGIC PLANE-###########################################
pack_of_eggs_price = flour_price_per_kilo * 0.75
liter_of_milk_price = flour_price_per_kilo * 1.25
loaf_price = flour_price_per_kilo + pack_of_eggs_price + (liter_of_milk_price * 0.25)
colored_eggs = 0
loaves_count = 0

while loaf_price < budget:
    budget -= loaf_price
    colored_eggs += 3
    loaves_count += 1

    if loaves_count % 3 == 0:
        colored_eggs -= loaves_count - 2
        if colored_eggs < 0:
            colored_eggs = 0

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
