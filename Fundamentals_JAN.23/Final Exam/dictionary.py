user_input = input()

dictionary = {}


#'programmer: an animal, which turns coffee into code | developer: a magician'
args = user_input.split(" | ")
for item in args:
    word, definition = item.split(": ")
    if word in dictionary:
        dictionary[word].append(definition)
    
    else:
        dictionary[word] = [definition]

test_words = input().split(" | ")
command = input()

if command == "Test":
    for word in test_words:
        if word in dictionary:
            print(f"{word}:")
            print(f"-"+"\n-".join(dictionary[word]))

else:
    for key in dictionary.keys():
        print(f"{key}", end=" ")
