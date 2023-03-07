team_name = input()
number_of_matches = int(input())

win_count, draw_count, loss_count = 0, 0, 0
total_points = 0

if number_of_matches == 0:
    print(f"{team_name} hasn't played any games during this season.")

else:

    for i in range(1, number_of_matches + 1):
        result = input()

        if result == "W":
            total_points += 3
            win_count += 1
        elif result == 'D':
            total_points += 1
            draw_count += 1
        elif result == 'L':
            loss_count += 1

    print(f"{team_name} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {win_count}")
    print(f"## D: {draw_count}")
    print(f"## L: {loss_count}")
    print(f"Win rate: {win_count / number_of_matches * 100:.2f}%")
