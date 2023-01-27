user_input = input()
shuffles = int(input())
##################LOGIC#######################
deck = user_input.split()

for _ in range(shuffles):
    side_a = deck[:int(len(deck) / 2)]
    side_b = deck[int(len(deck) / 2):]

    for i in range(len(deck)):
        if i == 0:
            deck[i] = side_a[0]
            side_a.pop(0)

        elif i % 2 != 0:
            deck[i] = side_b[0]
            side_b.pop(0)

        elif i % 2 == 0:
            deck[i] = side_a[0]
            side_a.pop(0)
print(deck)
