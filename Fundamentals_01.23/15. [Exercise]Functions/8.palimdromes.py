def is_palindrome(number):

    return number == number[::-1]


user_input = input().split(", ")

for element in user_input:

    print(is_palindrome(element))
