# Input
junior_cyclists = int(input())
senior_cyclists = int(input())
race_type = input()

# Logic
if race_type == 'trail':
    total_money_gathered = junior_cyclists * 5.5 + senior_cyclists * 7

elif race_type == 'cross-country':
    total_money_gathered = junior_cyclists * 8 + senior_cyclists * 9.50
    
    if junior_cyclists + senior_cyclists >= 50:
        total_money_gathered *= 0.75

elif race_type == 'downhill':
    total_money_gathered = junior_cyclists * 12.25 + senior_cyclists * 13.75

else:
    total_money_gathered = junior_cyclists * 20 + senior_cyclists * 21.50

total_money_gathered *= 0.95
print(f'{total_money_gathered:.2f}')    

