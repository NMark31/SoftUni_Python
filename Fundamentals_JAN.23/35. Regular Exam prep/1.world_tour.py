destinations = input()

while True:
    line = input()

    if line == "Travel":
        break

    command_args = line.split(":")
    command = command_args[0]

    if command == "Add Stop":
        index = int(command_args[1])
        string = command_args[2]

        if 0 <= index <= len(destinations):
            destinations = destinations[:index] + string + destinations[index:]

    elif command == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        string_to_remove = destinations[start_index:end_index + 1]

        if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations):
            destinations = destinations.replace(string_to_remove, "")

    else:
        old_string = command_args[1]
        new_string = command_args[2]

        destinations = destinations.replace(old_string, new_string)
    print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")
