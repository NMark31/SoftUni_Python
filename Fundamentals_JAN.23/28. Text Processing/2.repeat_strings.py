strings = input().split()

repeat_string = [word * len(word) for word in strings]
print(*repeat_string, sep="")
