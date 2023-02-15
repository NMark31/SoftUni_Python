def is_in_list(el, seq):
    return el in seq


shopping_list = input().split("!")

while True:
    user_input = input()

    if user_input == "Go Shopping!":
        break
    command_arguments = user_input.split()
    command = command_arguments[0]
    value = command_arguments[1]

    if command == "Urgent":
        if not is_in_list(value, shopping_list):
            shopping_list.insert(0, value)

    elif command == "Unnecessary":
        if is_in_list(value, shopping_list):
            shopping_list.remove(value)

    elif command == "Correct":
        new_value = command_arguments[2]
        if is_in_list(value, shopping_list):
            shopping_list[shopping_list.index(value)] = new_value

    elif command == "Rearrange":
        if is_in_list(value, shopping_list):
            shopping_list.remove(value)
            shopping_list.append(value)

print(", ".join(shopping_list))

