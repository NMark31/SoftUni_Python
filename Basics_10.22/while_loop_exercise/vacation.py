vacation_price = float(input())
available_money = float(input())
spending_days = 0
total_days = 0
action = None

while True:
    action = input()
    amount = float(input())
    total_days += 1
    
    if available_money < 0:
        available_money = 0
    
    if action == 'spend':
        spending_days += 1
        available_money -= amount
    
        if spending_days >= 5:
            print("You can't save the money.")
            print(total_days)
            break
    else:
        spending_days = 0
        available_money += amount
        

    if available_money >= vacation_price:
        print(f'You saved the money for {total_days} days.')
        break

    
