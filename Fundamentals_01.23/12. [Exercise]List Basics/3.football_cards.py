team_a = []
team_b = []

for i in range(1, 12):
    team_a.append(f"A-{i}")
    team_b.append(f"B-{i}")

red_cards = input().split()     # red_cards is a list.
is_terminated = False

for card in red_cards:
    if card in team_a:
        team_a.remove(card)

    elif card in team_b:
        team_b.remove(card)

    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if is_terminated:
    print("Game was terminated")


