import math


def factorial(num):
    return math.factorial(num)


def factorial_division(a, b):
    return a / b


num1, num2 = int(input()), int(input())

factorial_num1 = factorial(num1)
factorial_num2 = factorial(num2)

print(f"{factorial_division(factorial_num1, factorial_num2):.2f}")

