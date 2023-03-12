usernames = input().split(", ")
allowed_symbols = "-_"
valid_usernames = []

for username in usernames:
    is_invalid = False
    if not 3 <= len(username) <= 16:
        continue

    for chr in username:
        if not chr.isalpha() and not chr.isnumeric():
            if chr not in allowed_symbols:
                is_invalid = True
                break

    if is_invalid:
        continue

    valid_usernames.append(username)

print(*valid_usernames, sep="\n")


