user_input = input().split()
some_string = input()

message = ""

for seq in user_input:
    index = sum(int(el) for el in seq)

    if index >= len(some_string):
        index -= len(some_string)
    
    message += some_string[index]
    some_string = some_string[:index] + some_string[index + 1:]

print(message)
