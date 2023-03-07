words = input().split()
occurances = {}

for word in words:
    word = word.lower()

    if word not in occurances:
        occurances[word] = 0
    
    occurances[word] += 1

for key, value in occurances.items():
    if value % 2 != 0:
        print(f"{key}", end=" ")
    