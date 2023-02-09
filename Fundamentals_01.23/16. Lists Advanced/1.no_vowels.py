def is_vowel(char):
    if char.lower() == "a" or char.lower() == "o" or char.lower() == "u" or char.lower() == "e" or char.lower() == "i":
        return True


user_input = input()

result_without_vowels = [c for c in user_input if not is_vowel(c)]

print("".join(result_without_vowels))
