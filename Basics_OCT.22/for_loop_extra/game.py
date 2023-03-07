rounds = int(input())
under_ten_count = 0
under_twenty_count = 0
under_thirty_count = 0
under_forty_count = 0
under_fifty_count = 0
invalid_count = 0
total_score = 0

for _ in range(rounds):
    number = int(input())

    if 0 <= number <= 9:
        under_ten_count += 1
        total_score += number * 0.2

    elif 10 <= number <= 19:
        under_twenty_count += 1
        total_score += number * 0.3

    elif 20 <= number <= 29:
        under_thirty_count += 1
        total_score += number * 0.4

    elif 30 <= number <= 39:
        under_forty_count += 1
        total_score += 50
    
    elif 40 <= number <= 50:
        under_fifty_count += 1
        total_score += 100
    
    else:
        invalid_count += 1
        total_score /= 2

print(f"{total_score:.2f}")
print(f"From 0 to 9: {(under_ten_count / rounds) * 100:.2f}%")
print(f"From 10 to 19: {(under_twenty_count / rounds) * 100:.2f}%")
print(f"From 20 to 29: {(under_thirty_count / rounds) * 100:.2f}%")
print(f"From 30 to 39: {(under_forty_count / rounds) * 100:.2f}%")
print(f"From 40 to 50: {(under_fifty_count / rounds) * 100:.2f}%")
print(f"Invalid numbers: {(invalid_count / rounds) * 100:.2f}%")
