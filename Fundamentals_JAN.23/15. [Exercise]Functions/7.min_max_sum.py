def stats(numbers):

    min_number = min(numbers)
    max_number = max(numbers)
    sum_numbers = sum(numbers)
    return min_number, max_number, sum_numbers


sequence = [int(digit) for digit in input().split()]

min_num, max_num, sum_nums = stats(sequence)
print(f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_nums}")
    