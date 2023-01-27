factor = int(input())
count = int(input())

resulting_list = []

for i in range(factor, (count * factor) + 1):
    if i % factor == 0:
        resulting_list.append(i)

print(resulting_list)
