word = input()
list_of_capitals = []

for i in range(len(word)):
    if word[i].isupper():
        list_of_capitals.append(i)

print(list_of_capitals)
