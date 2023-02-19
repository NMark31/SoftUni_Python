def valid_index(idx, seq):
    return 0 <= idx < len(seq)


list_of_friends = input().split(", ")
blacklist_count = 0
lost_count = 0

while True:
    input_line = input()

    if input_line == "Report":
        print(f"Blacklisted names: {blacklist_count}")
        print(f"Lost names: {lost_count}")
        print(" ".join(list_of_friends))
        break

    args = input_line.split()
    command = args[0]

    if command == "Blacklist":
        if args[1] in list_of_friends:
            list_of_friends[list_of_friends.index(f"{args[1]}")] = "Blacklisted"
            blacklist_count += 1
            print(f"{args[1]} was blacklisted.")
        else:
            print(f"{args[1]} was not found.")

    elif command == "Error":
        idx = int(args[1])
        if valid_index(idx, list_of_friends) and list_of_friends[idx] != "Blacklisted" and list_of_friends[idx] != "Lost":
            print(f"{list_of_friends[idx]} was lost due to an error.")
            list_of_friends[idx] = "Lost"
            lost_count += 1

    elif command == "Change":
        idx = int(args[1])
        new_name = args[2]
        if valid_index(idx, list_of_friends):
            print(f"{list_of_friends[idx]} changed his username to {new_name}")
            list_of_friends[idx] = new_name