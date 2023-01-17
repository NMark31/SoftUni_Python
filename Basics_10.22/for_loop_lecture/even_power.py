import math
power = int(input())

result = 0

for i in range(0, power + 1, 2):
    result = math.pow(2, i)
    print(int(result))
