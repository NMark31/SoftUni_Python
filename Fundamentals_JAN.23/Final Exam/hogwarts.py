spell = input()

while True:
    line = input()

    if line == "Abracadabra":
        break

    args = line.split()
    command = args[0]

    if command == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif command == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif command == "Illusion":
        index = int(args[1])
        letter = args[2]

        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index+1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif command == "Divination":
        first_substr = args[1]
        second_substr = args[2]

        if first_substr in spell:
            spell = spell.replace(first_substr, second_substr)
            print(spell)

    elif command == "Alteration":
        substring = args[1]

        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
        
    else:
        print("The spell did not work!")
