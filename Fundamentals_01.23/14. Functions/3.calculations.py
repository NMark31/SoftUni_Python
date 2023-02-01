operator_value = input()
num1, num2, = int(input()), int(input())

def calculus(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result

print(calculus(num1, num2, operator_value))
