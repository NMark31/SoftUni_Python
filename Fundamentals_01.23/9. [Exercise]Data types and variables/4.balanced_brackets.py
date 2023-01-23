n = int(input())

open_count = 0
closed_count = 0
is_balanced = True

for _ in range(n):
    symbol = input()

    if symbol == "(":
        open_count += 1
    
    elif symbol == ")":
        closed_count += 1
    
    if open_count - closed_count == 2 or closed_count - open_count == 2 or closed_count > open_count:
        is_balanced = False

if open_count == closed_count and is_balanced == True:
    print("BALANCED")
else:
    print("UNBALANCED")

