user_input = [int(num) for num in input().split(", ")]

even_numbers = [x for x in range(len(user_input)) if user_input[x] % 2 == 0]

print(even_numbers)



