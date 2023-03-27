encrypted_message = input()
decrypted_message = encrypted_message

while True:
    line = input()

    if line == "Decode":
        break

    args = line.split("|")
    command = args[0]

    if command == "Move":
        count_letters = int(args[1])

        decrypted_message = decrypted_message[count_letters:] + decrypted_message[:count_letters]
    
    elif command == "Insert":
        index = int(args[1])
        value = args[2]

        decrypted_message = decrypted_message[:index] + f"{value}" + decrypted_message[index:]
    
    elif command == "ChangeAll":
        letter = args[1]
        replacement = args[2]

        decrypted_message = decrypted_message.replace(letter, replacement)


print(f"The decrypted message is: {decrypted_message}")


