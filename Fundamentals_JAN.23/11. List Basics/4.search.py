n = int(input())
key_word = input()
initial_list = []
filtered_list = []

for _ in range(n):
    user_input = input()
    initial_list.append(user_input)

    if key_word in user_input:
        filtered_list.append(user_input)

print(initial_list)
print(filtered_list)
