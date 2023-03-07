products = {}

while True:
    line = input()

    if line == "statistics":
        break

    key, value = line.split(": ")

    if key not in products:
        products[key] = int(value)
    
    else:
        products[key] += int(value)


print("Products in stock:")
for prod, qtty in products.items():
    print(f"- {prod}: {qtty}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
