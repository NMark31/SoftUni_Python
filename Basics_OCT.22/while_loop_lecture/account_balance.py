transaction = None
balance = 0

while True:
    transaction = input()

    if transaction == 'NoMoreMoney':
        break

    money = float(transaction)

    if money >= 0:
        print(f'Increase: {money:.2f}')
        balance += money
    else:
        print('Invalid operation!')
        break

print(f'Total: {balance:.2f}')
