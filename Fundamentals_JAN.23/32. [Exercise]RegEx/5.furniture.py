import re

money_spent = 0
bought_furniture = []
regex = r">>([A-Za-z]+)<<(\d+\.*\d*)!(\d+)"

while True:
    user_input = input()

    if user_input == "Purchase":
        break

    matches = re.findall(regex, user_input)

    if matches:
        bought_furniture.append(matches[0][0])
        money_spent += float(matches[0][1]) * int(matches[0][2])


print("Bought furniture:")
for product in bought_furniture:
    print(product)
print(f"Total money spend: {money_spent:.2f}")
    