def chars_in_range(char1, char2):
    char_list = []
    for ch in range(ord(char1) + 1, ord(char2)):
        char_list.append(chr(ch))

    return char_list


char_start = input()
char_end = input()

print(" ".join(chars_in_range(char_start, char_end)))
