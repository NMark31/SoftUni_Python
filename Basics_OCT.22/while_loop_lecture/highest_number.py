import sys

high_number = -sys.maxsize
number = None

while True:
    number = input()

    if number == 'Stop':
        break

    if int(number) > high_number:
        high_number = int(number)
    
print(high_number)
