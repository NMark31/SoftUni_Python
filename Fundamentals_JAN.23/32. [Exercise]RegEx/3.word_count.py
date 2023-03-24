import re

text = input().lower()
word = input().lower()

regex = f"\\b({word})\\b"

matches = re.findall(regex, text)
print(len(matches))