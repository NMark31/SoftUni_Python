floors = int(input())
apartaments = int(input())

for f in range(floors, 0, -1):
    for a in range(0, apartaments):

        if f == floors:
            print(f'L{f}{a}', end=" ")
        
        elif f % 2 == 0:
            print(f'O{f}{a}', end=" ")
        
        else:
            print(f'A{f}{a}', end=" ")
    print("")