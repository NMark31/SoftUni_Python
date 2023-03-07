pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(y) for y in input().split(">")]
max_health = int(input())

is_stalemate = True

while is_stalemate:
    line = input()

    if line == "Retire":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Fire":
        section = int(command_args[1])
        damage = int(command_args[2])
        if 0 <= section < len(war_ship):
            war_ship[section] -= damage
            if war_ship[section] <= 0:
                is_stalemate = False
                print("You won! The enemy ship has sunken.")

    elif command == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if 0 <= start_idx < len(pirate_ship) and 0 <= end_idx < (len(pirate_ship)):
            for idx in range(start_idx, end_idx + 1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_stalemate = False
                    break

    elif command == "Repair":
        section = int(command_args[1])
        damage = int(command_args[2])
        if 0 <= section < len(pirate_ship):
            pirate_ship[section] = min(max_health, damage + pirate_ship[section])

    elif command == "Status":
        threshold = max_health * 0.2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1
        print(f"{counter} sections need repair.")

if is_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
