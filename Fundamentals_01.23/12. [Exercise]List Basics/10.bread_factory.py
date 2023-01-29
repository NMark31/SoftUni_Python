energy = 100
gained_energy = 0
coins = 100
events = input().split("|")

for event in events:
    event = event.split("-")
    event_id = event[0]
    event_value = event[1]

    if event_id == "rest":
        if energy + int(event_value) > 100:
           gained_energy = 100 - energy
        else:
            gained_energy = int(event_value)

        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    
    elif event_id == "order":
        if energy >= 30:
            coins += int(event_value)
            energy -= 30
            print(f"You earned {event_value} coins.")
        else:
           energy += 50
           print("You had to rest!")
           continue
    
    else:
        if coins >= int(event_value):
            coins -= int(event_value)
            print(f"You bought {event_id}.")
        else:
            print(f"Closed! Cannot afford {event_id}.")
            break

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
            