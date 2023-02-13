def is_vowel(char):
    return char.lower() in ['a', 'o', 'u', 'e', 'i']


user_input = input()

result_without_vowels = [c for c in user_input if not is_vowel(c)]

print("".join(result_without_vowels))
