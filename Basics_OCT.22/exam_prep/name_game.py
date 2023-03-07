import sys

winning_points = -sys.maxsize

winner_name = None

while True:
    name = input()

    if name == 'Stop':
        break
    
    current_points = 0
    for i in range(0, len(name)):
        number = int(input())

        if number == ord(name[i]):
            current_points += 10
        
        else:
            current_points += 2
    
    if current_points >= winning_points:
        winning_points = current_points
        winner_name = name

print(f'The winner is {winner_name} with {winning_points} points!')
