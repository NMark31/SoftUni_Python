user_input = input().split()
palindrome_string = [pal for pal in user_input if pal[::] == pal[::-1]]
look_for = input()

print(palindrome_string)
print(f"Found palindrome {palindrome_string.count(look_for)} times")
