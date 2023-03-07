detergent_amount = int(input()) * 750
dishes_count = 0
pots_count = 0
loadings_counter = 1

while detergent_amount >= 0:
    amount = input()

    if amount == "End":
        print('Detergent was enough!')
        print(f"{dishes_count} dishes and {pots_count} pots were washed.")
        print(f"Leftover detergent {detergent_amount} ml.")
        break

    if loadings_counter % 3 == 0:
        pots_count += int(amount)
        detergent_amount -= int(amount) * 15
    
    else:
        dishes_count += int(amount)
        detergent_amount -= int(amount) * 5
    
    loadings_counter += 1

else:
    print(f"Not enough detergent, {abs(detergent_amount)} ml. more necessary!")
