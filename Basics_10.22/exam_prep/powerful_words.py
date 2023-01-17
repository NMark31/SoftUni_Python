import sys
import math

score = -sys.maxsize
strongest_word = None

while True:
    word = input()

    if word == 'End of words':
        break

    current_score = 0

    for i in range(0, len(word)):
        current_score += ord(word[i])

    
    if word[0] == 'a'or \
        word[0] == 'A' or \
        word[0] == 'e' or \
        word[0] == 'E' or \
        word[0] == 'i' or \
        word[0] == 'I' or \
        word[0] == 'o' or \
        word[0] == 'O' or \
        word[0] == 'u' or \
        word[0] == 'U' or \
        word[0] == 'y' or \
        word[0] == 'Y':
        current_score *= len(word)
    
    else:
        current_score /= math.floor(len(word))
    
    if current_score > score:
        score = current_score
        strongest_word = word

print(f'The most powerful word is {strongest_word} - {score}')
