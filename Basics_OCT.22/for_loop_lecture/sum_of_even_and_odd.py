num_of_i = int(input())

even_result = 0
odd_result = 0

for i in range(0, num_of_i):
    number = int(input())
    if i % 2 == 0:
        even_result += number
    else:
        odd_result += number

if even_result == odd_result:
    print(f'Yes')
    print(f'Sum = {even_result}')

else: 
    print(f'No')
    print(f'Diff = {abs(even_result - odd_result)}')

