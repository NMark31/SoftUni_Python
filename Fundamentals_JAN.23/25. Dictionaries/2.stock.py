items = input().split()
needed_products = input().split()
products = {}

for idx in range(0, len(items), 2):
    key = items[idx]
    value = int(items[idx + 1])
    products[key] = value

for product in needed_products:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    
    else:
        print(f"Sorry, we don't have {product}")
