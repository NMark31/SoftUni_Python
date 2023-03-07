import sys

divisor = int(input())
boundary = int(input())
max_number = -sys.maxsize

for i in range(1, boundary + 1):
    if i % divisor == 0 and i <= boundary:
        if i > max_number:
            max_number = i

print(max_number)
