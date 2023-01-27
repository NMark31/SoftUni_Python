user_input = input().split(", ")

list_to_int = [int(i) for i in user_input]

for el in list_to_int:
    if el == 0:
        list_to_int.remove(el)
        list_to_int.append(el)

print(list_to_int)
