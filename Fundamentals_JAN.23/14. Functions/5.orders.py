order_input = input()
quantity = int(input())

def order(product, count):
    price = None

    if product == 'coffee':
        price = count * 1.5
    
    elif product == 'water':
        price = count * 1.00
    
    elif product == 'coke':
        price = count * 1.4
    
    elif product == 'snacks':
        price = count * 2.00
    
    return f'{price:.2f}'

print(order(order_input, quantity))
