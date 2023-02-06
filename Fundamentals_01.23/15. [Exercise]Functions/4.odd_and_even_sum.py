def odd_even_sum(numbers):
    numbers = [int(digit) for digit in numbers]
    even_sum, odd_sum = 0, 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum


num_input = input()
even, odd = odd_even_sum(num_input)
print(f"Odd sum = {odd}, Even sum = {even}")
