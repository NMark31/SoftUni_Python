text = input()
cipher = ''

for char in text:
    cipher += chr(ord(char) + 3)

print(cipher)
