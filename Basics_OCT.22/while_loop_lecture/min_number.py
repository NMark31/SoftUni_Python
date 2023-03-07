import sys

low_number = sys.maxsize
number = None

while True:
    number = input()

    if number == 'Stop':
        break

    if int(number) < low_number:
        low_number = int(number)
    
print(low_number)
