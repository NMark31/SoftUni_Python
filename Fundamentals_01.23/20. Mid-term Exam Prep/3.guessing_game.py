def is_valid(idx_start, idx_end, seq):
    return 0 <= idx_start < len(seq) and 0 <= idx_end < len(seq) \
            and idx_start != idx_end


sequence = input().split()
number_of_moves = 0

while sequence:
    number_of_moves += 1
    command = input()

    if command == "end":
        print(f"Sorry you lose :(")
        print(*sequence, sep=" ")
        break
    else:
        args = command.split()
        idx_1 = int(args[0])
        idx_2 = int(args[1])
        if is_valid(idx_1, idx_2, sequence):
            if sequence[int(idx_1)] == sequence[int(idx_2)]:
                print(f"Congrats! You have found matching elements - {sequence[int(idx_1)]}!")
                element = sequence[idx_1]
                sequence.remove(element)
                sequence.remove(element)
            else:
                print(f"Try again!")

        else:
            sequence.insert(len(sequence) // 2, f"-{number_of_moves}a")
            sequence.insert(len(sequence) // 2, f"-{number_of_moves}a")
            print(f"Invalid input! Adding additional elements to the board")


else:
    print(f"You have won in {number_of_moves} turns!")
