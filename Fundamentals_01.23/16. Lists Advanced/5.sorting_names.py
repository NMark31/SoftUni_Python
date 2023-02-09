user_input = input().split(", ")
sorted_string = sorted(user_input, key=lambda x: (-len(x), x))

print(sorted_string)
