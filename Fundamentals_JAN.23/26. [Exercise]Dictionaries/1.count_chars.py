words = input().split()
letters_count = {}

for word in words:
    for letter in word:
        if letter not in letters_count:
            letters_count[letter] = 1
        
        else:
            letters_count[letter] += 1

for letter, count in letters_count.items():
    print(f"{letter} -> {count}")
    