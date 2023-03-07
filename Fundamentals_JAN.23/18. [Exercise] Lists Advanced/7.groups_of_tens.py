user_input = [int(e) for e in input().split(", ")]

groups_low_range = 1
groups_high_range = 10

while user_input:
    list_to_print = []
    for x in user_input:
        if groups_low_range <= x <= groups_high_range:
            list_to_print.append(x)

    print(f"Group of {groups_high_range}'s: {list_to_print}")
    user_input = [x for x in user_input if x not in list_to_print]
    groups_low_range += 10
    groups_high_range += 10
    