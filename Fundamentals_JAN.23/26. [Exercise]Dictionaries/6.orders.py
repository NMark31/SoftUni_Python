value_products = {}
quantity_products = {}

while True:
    line = input()

    if line == "buy":
        break

    args = line.split()
    name = args[0]
    price = float(args[1])
    quantity = int(args[2])

    if name not in value_products:
        value_products[name] = price
        quantity_products[name] = quantity
    
    else:
        value_products[name] = price
        quantity_products[name] += quantity
        

for product in value_products:
    price = value_products[product]
    quantity = quantity_products[product]
    print(f"{product} -> {price * quantity:.2f}")
    