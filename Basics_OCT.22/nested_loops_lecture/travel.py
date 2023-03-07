while True:
    destination = input()

    if destination == "End":
        break
    
    required_budget = float(input())
    saved_money = 0

    while saved_money < required_budget:
        saved_money += float(input())

    else: 
        print(f'Going to {destination}!')