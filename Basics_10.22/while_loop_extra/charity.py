target_value = int(input())
cash_value = 0
cash_transactions = 0
card_value = 0
card_transactions = 0
total_value = 0
transactions_count = 0


while total_value < target_value:
    product_value = input()
    transactions_count += 1
    
    if product_value == "End":
        print('Failed to collect required money for charity.')
        break

    if transactions_count % 2 == 0:
        if int(product_value) < 10:
            print(f'Error in transaction!')
            continue
        else:
            card_value += int(product_value)
            total_value += int(product_value)
            card_transactions += 1
            print('Product sold!')
    
    else:
        if int(product_value) > 100:
            print(f'Error in transaction!')
            continue
        else:
            cash_value += int(product_value)
            total_value += int(product_value)
            cash_transactions += 1
            print('Product sold!')
    
    

else:
    print(f'Average CS: {(cash_value / cash_transactions):.2f}')
    print(f'Average CC: {(card_value / card_transactions):.2f}')