gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command = command.split()
    if command[0] == "OutOfStock":
        gifts = [None if element == command[1] else element for element in gifts]

    elif command[0] == "Required":
        if int(command[2]) >= len(gifts) or int(command[2]) < 0:
            continue
        gifts[int(command[2])] = command[1]

    else:
        gifts[-1] = command[1]

gifts = [element for element in gifts if element is not None]
print(" ".join(gifts))

