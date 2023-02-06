def add(a, b):
    return a + b


def subtract(c, d):
    return c - d


num1, num2, num3 = int(input()), int(input()), int(input())
print(subtract(add(num1, num2), num3))
