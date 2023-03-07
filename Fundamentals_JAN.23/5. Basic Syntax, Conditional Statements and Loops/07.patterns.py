number = int(input())
count = 0

for j in range(number):
    count += 1
    print("*" * count)
    

for i in range(number-1, 0, -1):
    count -= 1
    print("*" * (count))

