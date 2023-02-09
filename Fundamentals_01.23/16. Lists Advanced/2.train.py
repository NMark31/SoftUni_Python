num_of_wagons = int(input())

train = [0] * num_of_wagons

while True:
    command = input().split()

    if command[0] == "End":
        break

    elif command[0] == "add":
        train[len(train)-1] += int(command[1])

    elif command[0] == "insert":
        train.pop(int(command[1]))
        train.insert(int(command[1]), int(command[2]))

    elif command[0] == "leave":
        train[int(command[1])] -= int(command[2])

print(train)

