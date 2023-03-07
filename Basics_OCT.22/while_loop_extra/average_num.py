total_sum = 0
iterations = int(input())
for i in range(iterations):
    number = int(input())
    total_sum += number

print(f'{(total_sum / iterations):.2f} ')
