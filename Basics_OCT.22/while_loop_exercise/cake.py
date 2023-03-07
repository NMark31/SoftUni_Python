a = int(input())
b = int(input())
pieces_count = a * b
total_pieces_taken = 0

while total_pieces_taken < pieces_count:
    pieces_taken = input()

    if pieces_taken == 'STOP':
        print(f'{pieces_count - total_pieces_taken} pieces are left.')
        break

    total_pieces_taken += int(pieces_taken)

else:
    print(f'No more cake left! You need {total_pieces_taken - pieces_count} pieces more.')
