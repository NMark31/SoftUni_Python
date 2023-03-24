import re

text = []

while True:
    user_input = input()

    if user_input == "":
        break
    else:
        text.append(user_input)

strings = "".join(text)
regex = r"\d+"
matches = re.findall(regex, strings)
print(*matches, sep=" ")
