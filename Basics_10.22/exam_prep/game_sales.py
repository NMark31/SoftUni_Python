total_games = int(input())
hs_count, fn_count, ow_count, others_count = 0, 0, 0, 0

for g in range(1, total_games + 1):
    game_name = input()

    if game_name == 'Hearthstone':
        hs_count += 1

    elif game_name == 'Fornite':
        fn_count += 1
    
    elif game_name == 'Overwatch':
        ow_count += 1
    
    else:
        others_count += 1

print(f"Hearthstone - {hs_count / total_games * 100:.2f}%")
print(f"Fornite - {fn_count / total_games * 100:.2f}%")
print(f"Overwatch - {ow_count / total_games * 100:.2f}%")
print(f"Others - {others_count / total_games * 100:.2f}%")
