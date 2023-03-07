import sys

n = int(input())
pairs = 2 * n
first_number = 0
second_number = 0
previous_value = 0
current_value = 0
max_diff = -sys.maxsize
equals_count = 0

for i in range(1, pairs + 1):
    current_number = int(input())

    if i == 1:
        first_number = current_number
          
    elif i == 2:
        second_number = current_number
        previous_value = first_number + second_number
    
    elif not i % 2 == 0:
        current_value = current_number
    
    else:
        current_value += current_number

        if previous_value == current_value:
            equals_count += 1
        
        else:
            if max_diff < abs(previous_value - current_value):
                max_diff = abs(previous_value - current_value)

        previous_value = current_value

if equals_count == n - 1:
    print(f'Yes, value={previous_value}')

else:
    print(f'No, maxdiff={max_diff}')
