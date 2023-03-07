while True:
    string = input()

    if string == "End":
        break

    elif string == "SoftUni":
        continue

    for ch in string:
        print(f"{ch}{ch}", end="")

    print()
