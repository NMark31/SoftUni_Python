first_string = input()
second_string = input()

resulting_string = first_string

for ch in range(len(second_string)):

    mutated_string = second_string[:ch + 1] + first_string[ch + 1:]

    if mutated_string != resulting_string:
        resulting_string = mutated_string
        print(resulting_string)

