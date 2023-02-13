user_input = input().split(", ")

groups_low_range = 1
groups_high_range = 10

while user_input:
    print(f"Group of {groups_high_range}'s:  {[int(x) for x in user_input if groups_low_range <= int(x) <= groups_high_range]}")
    
    
    for x in range(len(user_input)):
        if groups_low_range <= int(user_input[x]) <= groups_high_range:
            user_input.remove(user_input[x])

    groups_low_range += 10
    groups_high_range += 10
    