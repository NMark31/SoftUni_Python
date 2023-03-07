N = int(input())

for number in range(1111, 10000):
    counter = 0
    for index, digit in enumerate(str(number)):

        if digit == '0':
            break
        
        elif N % int(digit) == 0:
            counter += 1
    
        if counter == 4:
            print(f'{number}', end=' ')

