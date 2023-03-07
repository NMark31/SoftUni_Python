rooms_list = input().split("|")
MAX_HEALTH = 100
health = MAX_HEALTH
gold = 0

for number, room in enumerate(rooms_list, start=1):
    arguments = room.split()
    encounter = arguments[0]
    amount = int(arguments[1])

    if encounter == "potion":
        print(f"You healed for {amount if health + amount <= MAX_HEALTH else MAX_HEALTH - health} hp.")
        health = min(health + amount, MAX_HEALTH)
        print(f"Current health: {health} hp.")

    elif encounter == "chest":
        gold += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount
        if health <= 0:
            print(f"You died! Killed by {encounter}.")
            print(f"Best room: {number}")
            break

        else:
            print(f"You slayed {encounter}.")
else:
    print("You've made it!")
    print(f"Bitcoins: {gold}")
    print(f"Health: {health}")
