string = input()

result = 0
for i in range(0, len(string)):

    if string[i] == 'a':
        result += 1
    elif string[i] == 'e':
        result += 2
    elif string[i] == 'i':
        result += 3
    elif string[i] == 'o':
        result += 4
    elif string[i] == 'u':
        result += 5

print(result)
