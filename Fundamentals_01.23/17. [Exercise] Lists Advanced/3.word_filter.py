user_input = input().split()

filtered_list = [x for x in user_input if len(x) % 2 == 0]
print("\n".join(filtered_list))
