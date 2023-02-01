list_of_items = input().split("|")
budget = float(input())
items_bought = []
items_to_sell =[]
profit = 0
train_price = 150

for item in list_of_items:
    item = item.split("->")

    # item[0] is type, item[1] is price
    if item[0] == "Clothes" and float(item[1]) > 50.00:
        continue

    if item[0] == "Shoes" and float(item[1]) > 35.00:
        continue

    if item[0] == "Accessories" and float(item[1]) > 20.50:
        continue

    if budget < float(item[1]):
        continue

    budget -= float(item[1])
    items_bought.append(float(item[1]))

for element in (items_bought):
    new_element = 0.4 * element + element
    items_to_sell.append(new_element)
    profit += 0.4 * element

for i in items_to_sell:
    print(f"{i:.2f}", end=" ")

budget += sum(items_to_sell)
print(f"\nProfit: {profit:.2f}")
print(f"Hello, France!" if budget >= train_price else "Not enough money.")


