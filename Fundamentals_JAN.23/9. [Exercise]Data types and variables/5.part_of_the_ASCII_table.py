start = int(input())
finish = int(input())

for char in range(start, finish + 1):
    print(f"{chr(char)}", end=" ")
