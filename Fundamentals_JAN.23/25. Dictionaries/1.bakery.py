items = input().split()
products = {}
for idx in range(0, len(items), 2):
    key = items[idx]
    value = int(items[idx + 1])
    products[key] = value

print(products)
