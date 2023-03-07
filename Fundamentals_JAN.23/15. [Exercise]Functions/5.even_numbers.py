user_input = [int(digit) for digit in input().split()]
print(list(filter(lambda x: x % 2 == 0, user_input)))



