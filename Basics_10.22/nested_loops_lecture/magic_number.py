start = int(input())
end = int(input())
magic_number = int(input())
combinations_counter = 0
successes = 0
first_number = 0
second_number = 0

for x in range(start, end+1, 1):
    first_number = x

    for y in range(start, end+1, 1):
        combinations_counter += 1
        second_number = y
        if x + y == magic_number:
            successes += 1
            break

    if successes > 0:
        print(f'Combination N:{combinations_counter} ({first_number} + {second_number} = {magic_number})')
        break

if successes == 0:
    print(f'{combinations_counter} combinations - neither equals {magic_number}')
