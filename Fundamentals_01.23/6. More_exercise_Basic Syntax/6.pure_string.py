number_of_strings = int(input())
forbidden_chars = ",._"

for _ in range(number_of_strings):
    string = input()

    if any(ch in string for ch in forbidden_chars):
        print(f"{string} is not pure!")

    else:
        print(f"{string} is pure.")
