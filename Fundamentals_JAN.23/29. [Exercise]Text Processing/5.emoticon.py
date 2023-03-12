text = input()
emoticons = []

for idx, char in enumerate(text):
    if char == ":":
        emoticons.append(text[idx] + text[idx+1])

print(*emoticons, sep="\n")
