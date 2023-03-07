start = int(input())
end = int(input())

for i in range(start, end + 1):
    odd_sum, even_sum = 0, 0

    for index, digit in enumerate(str(i)):

        if index % 2 == 0:
            even_sum += int(digit)
        
        else:
            odd_sum += int(digit)
    
    if even_sum == odd_sum:
        print(f'{i}', end=" ")
