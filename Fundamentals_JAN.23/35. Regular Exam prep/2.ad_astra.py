import re

text = input()
regex = r"(#|\|)(?P<Product>[A-Za-z ]+)\1(?P<Date>\d{2}/\d{2}/\d{2})\1(?P<Calories>[0-9][0-9][0-9][0-9]{0,4}|10000])\1"

matches = re.finditer(regex, text)

total_calories = 0
items = []

for match in matches:
    total_calories += int(match.group("Calories"))
    items.append(match.groupdict())

print(f"You have food to last you for: {total_calories // 2000} days!")

for item in items:
    print(f"Item: {item['Product']}, Best before: {item['Date']}, Nutrition: {item['Calories']}")
