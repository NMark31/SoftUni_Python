key = int(input())
n = int(input())
message = ""

for _ in range(n):
    char = ord(input()) + key
    message += chr(char)

print(message)

