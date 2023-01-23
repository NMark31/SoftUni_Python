coffee_count = 0
energy_consuming_commands = ["coding", "dog", "cat", "movie"]

while True:
    command = input()

    if command == "END":
        break

    cmd_to_lower = command.lower()
    if any(cmd == cmd_to_lower for cmd in energy_consuming_commands):
        coffee_count += 1
        if command.isupper():
            coffee_count += 1

if coffee_count <= 5:
    print(coffee_count)
else:
    print("You need extra sleep")
